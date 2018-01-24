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


class IotDpsPropertiesDescription(Model):
    """the service specific properties of a provisoning service, including keys,
    linked iot hubs, current state, and system generated properties such as
    hostname and idScope.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :param state: Current state of the provisioning service. Possible values
     include: 'Activating', 'Active', 'Deleting', 'Deleted',
     'ActivationFailed', 'DeletionFailed', 'Transitioning', 'Suspending',
     'Suspended', 'Resuming', 'FailingOver', 'FailoverFailed'
    :type state: str or ~azure.mgmt.iothubprovisioningservices.models.State
    :param provisioning_state: The ARM provisioning state of the provisioning
     service.
    :type provisioning_state: str
    :param iot_hubs: List of IoT hubs assosciated with this provisioning
     service.
    :type iot_hubs:
     list[~azure.mgmt.iothubprovisioningservices.models.IotHubDefinitionDescription]
    :param allocation_policy: Allocation policy to be used by this
     provisioning service. Possible values include: 'Hashed', 'GeoLatency',
     'Static'
    :type allocation_policy: str or
     ~azure.mgmt.iothubprovisioningservices.models.AllocationPolicy
    :ivar service_operations_host_name: Service endpoint for provisioning
     service.
    :vartype service_operations_host_name: str
    :ivar device_provisioning_host_name: Device endpoint for this provisioning
     service.
    :vartype device_provisioning_host_name: str
    :ivar id_scope: Unique identifier of this provisioning service.
    :vartype id_scope: str
    :param authorization_policies: List of authorization keys for a
     provisioning service.
    :type authorization_policies:
     list[~azure.mgmt.iothubprovisioningservices.models.SharedAccessSignatureAuthorizationRuleAccessRightsDescription]
    """

    _validation = {
        'service_operations_host_name': {'readonly': True},
        'device_provisioning_host_name': {'readonly': True},
        'id_scope': {'readonly': True},
    }

    _attribute_map = {
        'state': {'key': 'state', 'type': 'str'},
        'provisioning_state': {'key': 'provisioningState', 'type': 'str'},
        'iot_hubs': {'key': 'iotHubs', 'type': '[IotHubDefinitionDescription]'},
        'allocation_policy': {'key': 'allocationPolicy', 'type': 'str'},
        'service_operations_host_name': {'key': 'serviceOperationsHostName', 'type': 'str'},
        'device_provisioning_host_name': {'key': 'deviceProvisioningHostName', 'type': 'str'},
        'id_scope': {'key': 'idScope', 'type': 'str'},
        'authorization_policies': {'key': 'authorizationPolicies', 'type': '[SharedAccessSignatureAuthorizationRuleAccessRightsDescription]'},
    }

    def __init__(self, state=None, provisioning_state=None, iot_hubs=None, allocation_policy=None, authorization_policies=None):
        super(IotDpsPropertiesDescription, self).__init__()
        self.state = state
        self.provisioning_state = provisioning_state
        self.iot_hubs = iot_hubs
        self.allocation_policy = allocation_policy
        self.service_operations_host_name = None
        self.device_provisioning_host_name = None
        self.id_scope = None
        self.authorization_policies = authorization_policies
