# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

import sys
from typing import Any, Union

from azure.core.configuration import Configuration
from azure.core.credentials import AzureKeyCredential
from azure.core.pipeline import policies

from .._version import VERSION

if sys.version_info >= (3, 8):
    from typing import Literal  # pylint: disable=no-name-in-module, ungrouped-imports
else:
    from typing_extensions import Literal  # type: ignore  # pylint: disable=ungrouped-imports


class AnomalyDetectorClientConfiguration(Configuration):  # pylint: disable=too-many-instance-attributes
    """Configuration for AnomalyDetectorClient.

    Note that all parameters used to create this instance are saved as instance
    attributes.

    :param endpoint: Supported Cognitive Services endpoints (protocol and hostname, for example:
     https://westus2.api.cognitive.microsoft.com). Required.
    :type endpoint: str
    :param api_version: Api Version. "v1.1" Required.
    :type api_version: str or ~anomalydetector.models.APIVersion
    :param credential: Credential needed for the client to connect to Azure. Required.
    :type credential: ~azure.core.credentials.AzureKeyCredential
    :keyword api_version: Api Version. Default value is "v1.1". Note that overriding this default
     value may result in unsupported behavior.
    :paramtype api_version: str
    """

    def __init__(
        self, endpoint: str, api_version: Union[str, _models.APIVersion], credential: AzureKeyCredential, **kwargs: Any
    ) -> None:
        super(AnomalyDetectorClientConfiguration, self).__init__(**kwargs)
        api_version = kwargs.pop("api_version", "v1.1")  # type: Literal["v1.1"]

        if endpoint is None:
            raise ValueError("Parameter 'endpoint' must not be None.")
        if api_version is None:
            raise ValueError("Parameter 'api_version' must not be None.")
        if credential is None:
            raise ValueError("Parameter 'credential' must not be None.")

        self.endpoint = endpoint
        self.api_version = api_version
        self.credential = credential
        self.api_version = api_version
        kwargs.setdefault("sdk_moniker", "ai-anomalydetector/{}".format(VERSION))
        self._configure(**kwargs)

    def _configure(self, **kwargs: Any) -> None:
        self.user_agent_policy = kwargs.get("user_agent_policy") or policies.UserAgentPolicy(**kwargs)
        self.headers_policy = kwargs.get("headers_policy") or policies.HeadersPolicy(**kwargs)
        self.proxy_policy = kwargs.get("proxy_policy") or policies.ProxyPolicy(**kwargs)
        self.logging_policy = kwargs.get("logging_policy") or policies.NetworkTraceLoggingPolicy(**kwargs)
        self.http_logging_policy = kwargs.get("http_logging_policy") or policies.HttpLoggingPolicy(**kwargs)
        self.retry_policy = kwargs.get("retry_policy") or policies.AsyncRetryPolicy(**kwargs)
        self.custom_hook_policy = kwargs.get("custom_hook_policy") or policies.CustomHookPolicy(**kwargs)
        self.redirect_policy = kwargs.get("redirect_policy") or policies.AsyncRedirectPolicy(**kwargs)
        self.authentication_policy = kwargs.get("authentication_policy")
        if self.credential and not self.authentication_policy:
            self.authentication_policy = policies.AzureKeyCredentialPolicy(
                self.credential, "Ocp-Apim-Subscription-Key", **kwargs
            )
