# coding=utf-8
# pylint: disable=too-many-lines
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Dict, List, Literal, TYPE_CHECKING, Union

from .. import _model_base
from .._model_base import rest_discriminator, rest_field
from ._enums import AuthType

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from .. import models as _models


class ConnectionDetails(_model_base.Model):
    """to do.


    :ivar properties: to do. Required.
    :vartype properties: ~azure.ai.client.models._models.ConnectionProperties
    """

    name: str = rest_field()

    properties: "_models._models.ConnectionProperties" = rest_field()
    """to do. Required."""


class ConnectionDetailsList(_model_base.Model):
    """to do.


    :ivar value: to do. Required.
    :vartype value: list[~azure.ai.client.models._models.ConnectionDetails]
    """

    value: List["_models._models.ConnectionDetails"] = rest_field()
    """to do. Required."""


class ConnectionProperties(_model_base.Model):
    """to do.

    You probably want to use the sub-classes and not this class directly. Known sub-classes are:
    ConnectionPropertiesAADAuth, ConnectionPropertiesApiKeyAuth, ConnectionPropertiesSASAuth


    :ivar auth_type: Authentication type of the connection target. Required. Known values are:
     "ApiKey", "AAD", and "SAS".
    :vartype auth_type: str or ~azure.ai.client.models.AuthType
    """

    __mapping__: Dict[str, _model_base.Model] = {}
    auth_type: str = rest_discriminator(name="authType")
    """Authentication type of the connection target. Required. Known values are: \"ApiKey\", \"AAD\",
     and \"SAS\"."""


class ConnectionPropertiesAADAuth(ConnectionProperties, discriminator="AAD"):
    """Connection properties for connections with AAD authentication (aka ``Entra ID passthrough``\\
    ).


    :ivar auth_type: Authentication type of the connection target. Required. to do
    :vartype auth_type: str or ~azure.ai.client.models.AAD
    :ivar category: Category of the connection. Required. Known values are: "AzureOpenAI" and
     "Serverless".
    :vartype category: str or ~azure.ai.client.models.ConnectionCategory
    :ivar target: to do. Required.
    :vartype target: str
    """

    auth_type: Literal[AuthType.AAD] = rest_discriminator(name="authType")  # type: ignore
    """Authentication type of the connection target. Required. to do"""
    category: Union[str, "_models._enums.ConnectionCategory"] = rest_field()
    """Category of the connection. Required. Known values are: \"AzureOpenAI\" and \"Serverless\"."""
    target: str = rest_field()
    """to do. Required."""


class ConnectionPropertiesApiKeyAuth(ConnectionProperties, discriminator="ApiKey"):
    """Connection properties for connections with API key authentication.


    :ivar auth_type: Authentication type of the connection target. Required. to do
    :vartype auth_type: str or ~azure.ai.client.models.API_KEY
    :ivar category: Category of the connection. Required. Known values are: "AzureOpenAI" and
     "Serverless".
    :vartype category: str or ~azure.ai.client.models.ConnectionCategory
    :ivar credentials: Credentials will only be present for authType=ApiKey. Required.
    :vartype credentials: ~azure.ai.client.models._models.CredentialsApiKeyAuth
    :ivar target: to do. Required.
    :vartype target: str
    """

    auth_type: Literal[AuthType.API_KEY] = rest_discriminator(name="authType")  # type: ignore
    """Authentication type of the connection target. Required. to do"""
    category: Union[str, "_models._enums.ConnectionCategory"] = rest_field()
    """Category of the connection. Required. Known values are: \"AzureOpenAI\" and \"Serverless\"."""
    credentials: "_models._models.CredentialsApiKeyAuth" = rest_field()
    """Credentials will only be present for authType=ApiKey. Required."""
    target: str = rest_field()
    """to do. Required."""


class ConnectionPropertiesSASAuth(ConnectionProperties, discriminator="SAS"):
    """Connection properties for connections with SAS authentication.


    :ivar auth_type: Authentication type of the connection target. Required. to do
    :vartype auth_type: str or ~azure.ai.client.models.SAS
    :ivar category: Category of the connection. Required. Known values are: "AzureOpenAI" and
     "Serverless".
    :vartype category: str or ~azure.ai.client.models.ConnectionCategory
    :ivar credentials: Credentials will only be present for authType=ApiKey. Required.
    :vartype credentials: ~azure.ai.client.models._models.CredentialsSASAuth
    :ivar target: to do. Required.
    :vartype target: str
    """

    auth_type: Literal[AuthType.SAS] = rest_discriminator(name="authType")  # type: ignore
    """Authentication type of the connection target. Required. to do"""
    category: Union[str, "_models._enums.ConnectionCategory"] = rest_field()
    """Category of the connection. Required. Known values are: \"AzureOpenAI\" and \"Serverless\"."""
    credentials: "_models._models.CredentialsSASAuth" = rest_field()
    """Credentials will only be present for authType=ApiKey. Required."""
    target: str = rest_field()
    """to do. Required."""


class CredentialsApiKeyAuth(_model_base.Model):
    """to do.


    :ivar key: to do. Required.
    :vartype key: str
    """

    key: str = rest_field()
    """to do. Required."""


class CredentialsSASAuth(_model_base.Model):
    """to do.


    :ivar sas: to do. Required.
    :vartype sas: str
    """

    sas: str = rest_field(name="SAS")
    """to do. Required."""
