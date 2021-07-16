# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Any, Optional, TYPE_CHECKING

from azure.core.pipeline.transport import AsyncHttpResponse, HttpRequest
from azure.mgmt.core import AsyncARMPipelineClient
from msrest import Deserializer, Serializer

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from azure.core.credentials_async import AsyncTokenCredential

from ._configuration import MySQLManagementClientConfiguration
from .operations import ServersOperations
from .operations import ReplicasOperations
from .operations import BackupsOperations
from .operations import FirewallRulesOperations
from .operations import DatabasesOperations
from .operations import ConfigurationsOperations
from .operations import LocationBasedCapabilitiesOperations
from .operations import CheckVirtualNetworkSubnetUsageOperations
from .operations import CheckNameAvailabilityOperations
from .operations import GetPrivateDnsZoneSuffixOperations
from .operations import Operations
from .. import models


class MySQLManagementClient(object):
    """The Microsoft Azure management API provides create, read, update, and delete functionality for Azure MySQL resources including servers, databases, firewall rules, VNET rules, log files and configurations with new business model.

    :ivar servers: ServersOperations operations
    :vartype servers: azure.mgmt.rdbms.mysql_flexibleservers.aio.operations.ServersOperations
    :ivar replicas: ReplicasOperations operations
    :vartype replicas: azure.mgmt.rdbms.mysql_flexibleservers.aio.operations.ReplicasOperations
    :ivar backups: BackupsOperations operations
    :vartype backups: azure.mgmt.rdbms.mysql_flexibleservers.aio.operations.BackupsOperations
    :ivar firewall_rules: FirewallRulesOperations operations
    :vartype firewall_rules: azure.mgmt.rdbms.mysql_flexibleservers.aio.operations.FirewallRulesOperations
    :ivar databases: DatabasesOperations operations
    :vartype databases: azure.mgmt.rdbms.mysql_flexibleservers.aio.operations.DatabasesOperations
    :ivar configurations: ConfigurationsOperations operations
    :vartype configurations: azure.mgmt.rdbms.mysql_flexibleservers.aio.operations.ConfigurationsOperations
    :ivar location_based_capabilities: LocationBasedCapabilitiesOperations operations
    :vartype location_based_capabilities: azure.mgmt.rdbms.mysql_flexibleservers.aio.operations.LocationBasedCapabilitiesOperations
    :ivar check_virtual_network_subnet_usage: CheckVirtualNetworkSubnetUsageOperations operations
    :vartype check_virtual_network_subnet_usage: azure.mgmt.rdbms.mysql_flexibleservers.aio.operations.CheckVirtualNetworkSubnetUsageOperations
    :ivar check_name_availability: CheckNameAvailabilityOperations operations
    :vartype check_name_availability: azure.mgmt.rdbms.mysql_flexibleservers.aio.operations.CheckNameAvailabilityOperations
    :ivar get_private_dns_zone_suffix: GetPrivateDnsZoneSuffixOperations operations
    :vartype get_private_dns_zone_suffix: azure.mgmt.rdbms.mysql_flexibleservers.aio.operations.GetPrivateDnsZoneSuffixOperations
    :ivar operations: Operations operations
    :vartype operations: azure.mgmt.rdbms.mysql_flexibleservers.aio.operations.Operations
    :param credential: Credential needed for the client to connect to Azure.
    :type credential: ~azure.core.credentials_async.AsyncTokenCredential
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param str base_url: Service URL
    :keyword int polling_interval: Default waiting time between two polls for LRO operations if no Retry-After header is present.
    """

    def __init__(
        self,
        credential: "AsyncTokenCredential",
        subscription_id: str,
        base_url: Optional[str] = None,
        **kwargs: Any
    ) -> None:
        if not base_url:
            base_url = 'https://management.azure.com'
        self._config = MySQLManagementClientConfiguration(credential, subscription_id, **kwargs)
        self._client = AsyncARMPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._serialize.client_side_validation = False
        self._deserialize = Deserializer(client_models)

        self.servers = ServersOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.replicas = ReplicasOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.backups = BackupsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.firewall_rules = FirewallRulesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.databases = DatabasesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.configurations = ConfigurationsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.location_based_capabilities = LocationBasedCapabilitiesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.check_virtual_network_subnet_usage = CheckVirtualNetworkSubnetUsageOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.check_name_availability = CheckNameAvailabilityOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.get_private_dns_zone_suffix = GetPrivateDnsZoneSuffixOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.operations = Operations(
            self._client, self._config, self._serialize, self._deserialize)

    async def _send_request(self, http_request: HttpRequest, **kwargs: Any) -> AsyncHttpResponse:
        """Runs the network request through the client's chained policies.

        :param http_request: The network request you want to make. Required.
        :type http_request: ~azure.core.pipeline.transport.HttpRequest
        :keyword bool stream: Whether the response payload will be streamed. Defaults to True.
        :return: The response of your network call. Does not do error handling on your response.
        :rtype: ~azure.core.pipeline.transport.AsyncHttpResponse
        """
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str', min_length=1),
        }
        http_request.url = self._client.format_url(http_request.url, **path_format_arguments)
        stream = kwargs.pop("stream", True)
        pipeline_response = await self._client._pipeline.run(http_request, stream=stream, **kwargs)
        return pipeline_response.http_response

    async def close(self) -> None:
        await self._client.close()

    async def __aenter__(self) -> "MySQLManagementClient":
        await self._client.__aenter__()
        return self

    async def __aexit__(self, *exc_details) -> None:
        await self._client.__aexit__(*exc_details)
