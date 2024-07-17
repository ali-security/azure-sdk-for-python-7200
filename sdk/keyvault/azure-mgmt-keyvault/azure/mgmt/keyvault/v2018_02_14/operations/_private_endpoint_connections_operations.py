# pylint: disable=too-many-lines,too-many-statements
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from io import IOBase
import sys
from typing import Any, Callable, Dict, IO, Iterator, Optional, Type, TypeVar, Union, cast, overload

from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    ResourceNotModifiedError,
    map_error,
)
from azure.core.pipeline import PipelineResponse
from azure.core.polling import LROPoller, NoPolling, PollingMethod
from azure.core.rest import HttpRequest, HttpResponse
from azure.core.tracing.decorator import distributed_trace
from azure.core.utils import case_insensitive_dict
from azure.mgmt.core.exceptions import ARMErrorFormat
from azure.mgmt.core.polling.arm_polling import ARMPolling

from .. import models as _models
from ..._serialization import Serializer

if sys.version_info >= (3, 9):
    from collections.abc import MutableMapping
else:
    from typing import MutableMapping  # type: ignore  # pylint: disable=ungrouped-imports
T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False


def build_get_request(
    resource_group_name: str,
    vault_name: str,
    private_endpoint_connection_name: str,
    subscription_id: str,
    **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2018-02-14"))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop(
        "template_url",
        "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.KeyVault/vaults/{vaultName}/privateEndpointConnections/{privateEndpointConnectionName}",
    )  # pylint: disable=line-too-long
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, "str"),
        "resourceGroupName": _SERIALIZER.url("resource_group_name", resource_group_name, "str"),
        "vaultName": _SERIALIZER.url("vault_name", vault_name, "str", pattern=r"^[a-zA-Z0-9-]{3,24}$"),
        "privateEndpointConnectionName": _SERIALIZER.url(
            "private_endpoint_connection_name", private_endpoint_connection_name, "str"
        ),
    }

    _url: str = _url.format(**path_format_arguments)  # type: ignore

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, params=_params, headers=_headers, **kwargs)


def build_put_request(
    resource_group_name: str,
    vault_name: str,
    private_endpoint_connection_name: str,
    subscription_id: str,
    **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2018-02-14"))
    content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop(
        "template_url",
        "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.KeyVault/vaults/{vaultName}/privateEndpointConnections/{privateEndpointConnectionName}",
    )  # pylint: disable=line-too-long
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, "str"),
        "resourceGroupName": _SERIALIZER.url("resource_group_name", resource_group_name, "str"),
        "vaultName": _SERIALIZER.url("vault_name", vault_name, "str", pattern=r"^[a-zA-Z0-9-]{3,24}$"),
        "privateEndpointConnectionName": _SERIALIZER.url(
            "private_endpoint_connection_name", private_endpoint_connection_name, "str"
        ),
    }

    _url: str = _url.format(**path_format_arguments)  # type: ignore

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    if content_type is not None:
        _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="PUT", url=_url, params=_params, headers=_headers, **kwargs)


def build_delete_request(
    resource_group_name: str,
    vault_name: str,
    private_endpoint_connection_name: str,
    subscription_id: str,
    **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2018-02-14"))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop(
        "template_url",
        "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.KeyVault/vaults/{vaultName}/privateEndpointConnections/{privateEndpointConnectionName}",
    )  # pylint: disable=line-too-long
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, "str"),
        "resourceGroupName": _SERIALIZER.url("resource_group_name", resource_group_name, "str"),
        "vaultName": _SERIALIZER.url("vault_name", vault_name, "str", pattern=r"^[a-zA-Z0-9-]{3,24}$"),
        "privateEndpointConnectionName": _SERIALIZER.url(
            "private_endpoint_connection_name", private_endpoint_connection_name, "str"
        ),
    }

    _url: str = _url.format(**path_format_arguments)  # type: ignore

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="DELETE", url=_url, params=_params, headers=_headers, **kwargs)


class PrivateEndpointConnectionsOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.mgmt.keyvault.v2018_02_14.KeyVaultManagementClient`'s
        :attr:`private_endpoint_connections` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs):
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")
        self._api_version = input_args.pop(0) if input_args else kwargs.pop("api_version")

    @distributed_trace
    def get(
        self, resource_group_name: str, vault_name: str, private_endpoint_connection_name: str, **kwargs: Any
    ) -> _models.PrivateEndpointConnection:
        """Gets the specified private endpoint connection associated with the key vault.

        :param resource_group_name: Name of the resource group that contains the key vault. Required.
        :type resource_group_name: str
        :param vault_name: The name of the key vault. Required.
        :type vault_name: str
        :param private_endpoint_connection_name: Name of the private endpoint connection associated
         with the key vault. Required.
        :type private_endpoint_connection_name: str
        :return: PrivateEndpointConnection or the result of cls(response)
        :rtype: ~azure.mgmt.keyvault.v2018_02_14.models.PrivateEndpointConnection
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map: MutableMapping[int, Type[HttpResponseError]] = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._api_version or "2018-02-14"))
        cls: ClsType[_models.PrivateEndpointConnection] = kwargs.pop("cls", None)

        _request = build_get_request(
            resource_group_name=resource_group_name,
            vault_name=vault_name,
            private_endpoint_connection_name=private_endpoint_connection_name,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            headers=_headers,
            params=_params,
        )
        _request.url = self._client.format_url(_request.url)

        _stream = False
        pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize("PrivateEndpointConnection", pipeline_response.http_response)

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    @overload
    def put(
        self,
        resource_group_name: str,
        vault_name: str,
        private_endpoint_connection_name: str,
        properties: _models.PrivateEndpointConnection,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.PrivateEndpointConnection:
        """Updates the specified private endpoint connection associated with the key vault.

        :param resource_group_name: Name of the resource group that contains the key vault. Required.
        :type resource_group_name: str
        :param vault_name: The name of the key vault. Required.
        :type vault_name: str
        :param private_endpoint_connection_name: Name of the private endpoint connection associated
         with the key vault. Required.
        :type private_endpoint_connection_name: str
        :param properties: The intended state of private endpoint connection. Required.
        :type properties: ~azure.mgmt.keyvault.v2018_02_14.models.PrivateEndpointConnection
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: PrivateEndpointConnection or the result of cls(response)
        :rtype: ~azure.mgmt.keyvault.v2018_02_14.models.PrivateEndpointConnection
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    def put(
        self,
        resource_group_name: str,
        vault_name: str,
        private_endpoint_connection_name: str,
        properties: IO[bytes],
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.PrivateEndpointConnection:
        """Updates the specified private endpoint connection associated with the key vault.

        :param resource_group_name: Name of the resource group that contains the key vault. Required.
        :type resource_group_name: str
        :param vault_name: The name of the key vault. Required.
        :type vault_name: str
        :param private_endpoint_connection_name: Name of the private endpoint connection associated
         with the key vault. Required.
        :type private_endpoint_connection_name: str
        :param properties: The intended state of private endpoint connection. Required.
        :type properties: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: PrivateEndpointConnection or the result of cls(response)
        :rtype: ~azure.mgmt.keyvault.v2018_02_14.models.PrivateEndpointConnection
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace
    def put(
        self,
        resource_group_name: str,
        vault_name: str,
        private_endpoint_connection_name: str,
        properties: Union[_models.PrivateEndpointConnection, IO[bytes]],
        **kwargs: Any
    ) -> _models.PrivateEndpointConnection:
        """Updates the specified private endpoint connection associated with the key vault.

        :param resource_group_name: Name of the resource group that contains the key vault. Required.
        :type resource_group_name: str
        :param vault_name: The name of the key vault. Required.
        :type vault_name: str
        :param private_endpoint_connection_name: Name of the private endpoint connection associated
         with the key vault. Required.
        :type private_endpoint_connection_name: str
        :param properties: The intended state of private endpoint connection. Is either a
         PrivateEndpointConnection type or a IO[bytes] type. Required.
        :type properties: ~azure.mgmt.keyvault.v2018_02_14.models.PrivateEndpointConnection or
         IO[bytes]
        :return: PrivateEndpointConnection or the result of cls(response)
        :rtype: ~azure.mgmt.keyvault.v2018_02_14.models.PrivateEndpointConnection
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map: MutableMapping[int, Type[HttpResponseError]] = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._api_version or "2018-02-14"))
        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.PrivateEndpointConnection] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(properties, (IOBase, bytes)):
            _content = properties
        else:
            _json = self._serialize.body(properties, "PrivateEndpointConnection")

        _request = build_put_request(
            resource_group_name=resource_group_name,
            vault_name=vault_name,
            private_endpoint_connection_name=private_endpoint_connection_name,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            content=_content,
            headers=_headers,
            params=_params,
        )
        _request.url = self._client.format_url(_request.url)

        _stream = False
        pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        response_headers = {}
        response_headers["Retry-After"] = self._deserialize("int", response.headers.get("Retry-After"))
        response_headers["Azure-AsyncOperation"] = self._deserialize(
            "str", response.headers.get("Azure-AsyncOperation")
        )

        deserialized = self._deserialize("PrivateEndpointConnection", pipeline_response.http_response)

        if cls:
            return cls(pipeline_response, deserialized, response_headers)  # type: ignore

        return deserialized  # type: ignore

    def _delete_initial(
        self, resource_group_name: str, vault_name: str, private_endpoint_connection_name: str, **kwargs: Any
    ) -> Iterator[bytes]:
        error_map: MutableMapping[int, Type[HttpResponseError]] = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._api_version or "2018-02-14"))
        cls: ClsType[Iterator[bytes]] = kwargs.pop("cls", None)

        _request = build_delete_request(
            resource_group_name=resource_group_name,
            vault_name=vault_name,
            private_endpoint_connection_name=private_endpoint_connection_name,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            headers=_headers,
            params=_params,
        )
        _request.url = self._client.format_url(_request.url)

        _stream = True
        pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200, 202, 204]:
            response.read()  # Load the body in memory and close the socket
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        response_headers = {}
        if response.status_code == 200:
            deserialized = response.stream_download(self._client._pipeline)

        if response.status_code == 202:
            response_headers["Retry-After"] = self._deserialize("int", response.headers.get("Retry-After"))
            response_headers["Location"] = self._deserialize("str", response.headers.get("Location"))

            deserialized = response.stream_download(self._client._pipeline)

        if response.status_code == 204:
            deserialized = response.stream_download(self._client._pipeline)

        if cls:
            return cls(pipeline_response, deserialized, response_headers)  # type: ignore

        return deserialized  # type: ignore

    @distributed_trace
    def begin_delete(
        self, resource_group_name: str, vault_name: str, private_endpoint_connection_name: str, **kwargs: Any
    ) -> LROPoller[_models.PrivateEndpointConnection]:
        """Deletes the specified private endpoint connection associated with the key vault.

        :param resource_group_name: Name of the resource group that contains the key vault. Required.
        :type resource_group_name: str
        :param vault_name: The name of the key vault. Required.
        :type vault_name: str
        :param private_endpoint_connection_name: Name of the private endpoint connection associated
         with the key vault. Required.
        :type private_endpoint_connection_name: str
        :return: An instance of LROPoller that returns either PrivateEndpointConnection or the result
         of cls(response)
        :rtype:
         ~azure.core.polling.LROPoller[~azure.mgmt.keyvault.v2018_02_14.models.PrivateEndpointConnection]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._api_version or "2018-02-14"))
        cls: ClsType[_models.PrivateEndpointConnection] = kwargs.pop("cls", None)
        polling: Union[bool, PollingMethod] = kwargs.pop("polling", True)
        lro_delay = kwargs.pop("polling_interval", self._config.polling_interval)
        cont_token: Optional[str] = kwargs.pop("continuation_token", None)
        if cont_token is None:
            raw_result = self._delete_initial(
                resource_group_name=resource_group_name,
                vault_name=vault_name,
                private_endpoint_connection_name=private_endpoint_connection_name,
                api_version=api_version,
                cls=lambda x, y, z: x,
                headers=_headers,
                params=_params,
                **kwargs
            )
            raw_result.http_response.read()  # type: ignore
        kwargs.pop("error_map", None)

        def get_long_running_output(pipeline_response):
            deserialized = self._deserialize("PrivateEndpointConnection", pipeline_response.http_response)
            if cls:
                return cls(pipeline_response, deserialized, {})  # type: ignore
            return deserialized

        if polling is True:
            polling_method: PollingMethod = cast(PollingMethod, ARMPolling(lro_delay, **kwargs))
        elif polling is False:
            polling_method = cast(PollingMethod, NoPolling())
        else:
            polling_method = polling
        if cont_token:
            return LROPoller[_models.PrivateEndpointConnection].from_continuation_token(
                polling_method=polling_method,
                continuation_token=cont_token,
                client=self._client,
                deserialization_callback=get_long_running_output,
            )
        return LROPoller[_models.PrivateEndpointConnection](
            self._client, raw_result, get_long_running_output, polling_method  # type: ignore
        )
