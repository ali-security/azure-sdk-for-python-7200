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

from msrest.serialization import Model


class FlowLogInformation(Model):
    """Information on the configuration of flow log and traffic analytics
    (optional) .

    All required parameters must be populated in order to send to Azure.

    :param target_resource_id: Required. The ID of the resource to configure
     for flow log and traffic analytics (optional) .
    :type target_resource_id: str
    :param storage_id: Required. ID of the storage account which is used to
     store the flow log.
    :type storage_id: str
    :param enabled: Required. Flag to enable/disable flow logging.
    :type enabled: bool
    :param retention_policy:
    :type retention_policy:
     ~azure.mgmt.network.v2018_10_01.models.RetentionPolicyParameters
    :param format:
    :type format:
     ~azure.mgmt.network.v2018_10_01.models.FlowLogFormatParameters
    :param flow_analytics_configuration:
    :type flow_analytics_configuration:
     ~azure.mgmt.network.v2018_10_01.models.TrafficAnalyticsProperties
    """

    _validation = {
        'target_resource_id': {'required': True},
        'storage_id': {'required': True},
        'enabled': {'required': True},
    }

    _attribute_map = {
        'target_resource_id': {'key': 'targetResourceId', 'type': 'str'},
        'storage_id': {'key': 'properties.storageId', 'type': 'str'},
        'enabled': {'key': 'properties.enabled', 'type': 'bool'},
        'retention_policy': {'key': 'properties.retentionPolicy', 'type': 'RetentionPolicyParameters'},
        'format': {'key': 'properties.format', 'type': 'FlowLogFormatParameters'},
        'flow_analytics_configuration': {'key': 'flowAnalyticsConfiguration', 'type': 'TrafficAnalyticsProperties'},
    }

    def __init__(self, *, target_resource_id: str, storage_id: str, enabled: bool, retention_policy=None, format=None, flow_analytics_configuration=None, **kwargs) -> None:
        super(FlowLogInformation, self).__init__(**kwargs)
        self.target_resource_id = target_resource_id
        self.storage_id = storage_id
        self.enabled = enabled
        self.retention_policy = retention_policy
        self.format = format
        self.flow_analytics_configuration = flow_analytics_configuration
