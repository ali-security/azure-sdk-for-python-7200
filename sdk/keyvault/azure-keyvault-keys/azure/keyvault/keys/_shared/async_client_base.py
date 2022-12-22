# ------------------------------------
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
# ------------------------------------
from typing import TYPE_CHECKING

from azure.core.pipeline.policies import HttpLoggingPolicy
from azure.core.tracing.decorator_async import distributed_trace_async

from . import AsyncChallengeAuthPolicy
from .client_base import ApiVersion, DEFAULT_VERSION, _format_api_version, _SERIALIZER
from .._sdk_moniker import SDK_MONIKER
from .._generated.aio import KeyVaultClient as _KeyVaultClient

if TYPE_CHECKING:
    try:
        # pylint:disable=unused-import
        from typing import Any
        from azure.core.credentials_async import AsyncTokenCredential
        from azure.core.rest import AsyncHttpResponse, HttpRequest
    except ImportError:
        # AsyncTokenCredential is a typing_extensions.Protocol; we don't depend on that package
        pass


class AsyncKeyVaultClientBase(object):
    # pylint:disable=protected-access
    def __init__(self, vault_url: str, credential: "AsyncTokenCredential", **kwargs: "Any") -> None:
        if not credential:
            raise ValueError(
                "credential should be an object supporting the AsyncTokenCredential protocol, "
                "such as a credential from azure-identity"
            )
        if not vault_url:
            raise ValueError("vault_url must be the URL of an Azure Key Vault")

        try:
            self.api_version = kwargs.pop("api_version", DEFAULT_VERSION)
            # If API version was provided as an enum value, need to make a plain string for 3.11 compatibility
            if hasattr(self.api_version, "value"):
                self.api_version = self.api_version.value
            self._vault_url = vault_url.strip(" /")

            client = kwargs.get("generated_client")
            if client:
                # caller provided a configured client -> only models left to initialize
                self._client = client
                models = kwargs.get("generated_models")
                self._models = models or _KeyVaultClient.models(api_version=self.api_version)
                return

            http_logging_policy = HttpLoggingPolicy(**kwargs)
            http_logging_policy.allowed_header_names.update(
                {"x-ms-keyvault-network-info", "x-ms-keyvault-region", "x-ms-keyvault-service-version"}
            )

            verify_challenge = kwargs.pop("verify_challenge_resource", True)
            self._client = _KeyVaultClient(
                api_version=self.api_version,
                authentication_policy=AsyncChallengeAuthPolicy(credential, verify_challenge_resource=verify_challenge),
                sdk_moniker=SDK_MONIKER,
                http_logging_policy=http_logging_policy,
                **kwargs
            )
            self._models = _KeyVaultClient.models(api_version=self.api_version)
        except ValueError:
            raise NotImplementedError(
                "This package doesn't support API version '{}'. ".format(self.api_version)
                + "Supported versions: {}".format(", ".join(v.value for v in ApiVersion))
            )

    @property
    def vault_url(self) -> str:
        return self._vault_url

    async def __aenter__(self) -> "AsyncKeyVaultClientBase":
        await self._client.__aenter__()
        return self

    async def __aexit__(self, *args: "Any") -> None:
        await self._client.__aexit__(*args)

    async def close(self) -> None:
        """Close sockets opened by the client.

        Calling this method is unnecessary when using the client as a context manager.
        """
        await self._client.close()

    @distributed_trace_async
    async def send_request(
        self, request: "HttpRequest", *, stream: bool = False, **kwargs: "Any"
    ) -> "AsyncHttpResponse":
        """Runs a network request using the client's existing pipeline.

        The request URL can be relative to the vault URL. The service API version used for the request is the same as
        the client's unless otherwise specified. This method does not raise if the response is an error; to raise an
        exception, call `raise_for_status()` on the returned response object. For more information about how to send
        custom requests with this method, see https://aka.ms/azsdk/dpcodegen/python/send_request.

        :param request: The network request you want to make.
        :type request: ~azure.core.rest.HttpRequest

        :return: The response of your network call. Does not do error handling on your response.
        :rtype: ~azure.core.rest.AsyncHttpResponse
        """
        request_copy = _format_api_version(request, self.api_version)
        path_format_arguments = {
            "vaultBaseUrl": _SERIALIZER.url("vault_base_url", self._vault_url, "str", skip_quote=True),
        }
        request_copy.url = self._client._client.format_url(request_copy.url, **path_format_arguments)
        return await self._client._client.send_request(request_copy, stream=stream, **kwargs)
