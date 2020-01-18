# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.service_client import SDKClient
from msrest import Serializer, Deserializer

from ._configuration import AppConfigurationManagementClientConfiguration
from .operations import ConfigurationStoresOperations
from .operations import Operations
from .operations import PrivateEndpointConnectionsOperations
from .operations import PrivateLinkResourcesOperations
from . import models


class AppConfigurationManagementClient(SDKClient):
    """AppConfigurationManagementClient

    :ivar config: Configuration for client.
    :vartype config: AppConfigurationManagementClientConfiguration

    :ivar configuration_stores: ConfigurationStores operations
    :vartype configuration_stores: azure.mgmt.appconfiguration.operations.ConfigurationStoresOperations
    :ivar operations: Operations operations
    :vartype operations: azure.mgmt.appconfiguration.operations.Operations
    :ivar private_endpoint_connections: PrivateEndpointConnections operations
    :vartype private_endpoint_connections: azure.mgmt.appconfiguration.operations.PrivateEndpointConnectionsOperations
    :ivar private_link_resources: PrivateLinkResources operations
    :vartype private_link_resources: azure.mgmt.appconfiguration.operations.PrivateLinkResourcesOperations

    :param credentials: Credentials needed for the client to connect to Azure.
    :type credentials: :mod:`A msrestazure Credentials
     object<msrestazure.azure_active_directory>`
    :param subscription_id: The Microsoft Azure subscription ID.
    :type subscription_id: str
    :param str base_url: Service URL
    """

    def __init__(
            self, credentials, subscription_id, base_url=None):

        self.config = AppConfigurationManagementClientConfiguration(credentials, subscription_id, base_url)
        super(AppConfigurationManagementClient, self).__init__(self.config.credentials, self.config)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self.api_version = '2019-11-01-preview'
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.configuration_stores = ConfigurationStoresOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.operations = Operations(
            self._client, self.config, self._serialize, self._deserialize)
        self.private_endpoint_connections = PrivateEndpointConnectionsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.private_link_resources = PrivateLinkResourcesOperations(
            self._client, self.config, self._serialize, self._deserialize)
