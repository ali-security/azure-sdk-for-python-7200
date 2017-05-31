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

from .protection_container import ProtectionContainer


class MabContainer(ProtectionContainer):
    """Container with items backed up using MAB backup engine.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :param friendly_name: Friendly name of the container.
    :type friendly_name: str
    :param backup_management_type: Type of backup managemenent for the
     container. Possible values include: 'Invalid', 'AzureIaasVM', 'MAB',
     'DPM', 'AzureBackupServer', 'AzureSql'
    :type backup_management_type: str or :class:`BackupManagementType
     <azure.mgmt.recoveryservicesbackup.models.BackupManagementType>`
    :param registration_status: Status of registration of the container with
     the Recovery Services Vault.
    :type registration_status: str
    :param health_status: Status of health of the container.
    :type health_status: str
    :ivar container_type: Type of the container. The value of this property
     for: 1. Compute Azure VM is Microsoft.Compute/virtualMachines 2. Classic
     Compute Azure VM is Microsoft.ClassicCompute/virtualMachines 3. Windows
     machines (like MAB, DPM etc) is Windows 4. Azure SQL instance is
     AzureSqlContainer. Possible values include: 'Invalid', 'Unknown',
     'IaasVMContainer', 'IaasVMServiceContainer', 'DPMContainer',
     'AzureBackupServerContainer', 'MABContainer', 'Cluster',
     'AzureSqlContainer', 'Windows', 'VCenter'
    :vartype container_type: str or :class:`ContainerType
     <azure.mgmt.recoveryservicesbackup.models.ContainerType>`
    :param protectable_object_type: Polymorphic Discriminator
    :type protectable_object_type: str
    :param can_re_register: Can the container be registered one more time.
    :type can_re_register: bool
    :param container_id: ContainerID represents the container.
    :type container_id: long
    :param protected_item_count: Number of items backed up in this container.
    :type protected_item_count: long
    :param agent_version: Agent version of this container.
    :type agent_version: str
    :param extended_info: Additional information for this container
    :type extended_info: :class:`MabContainerExtendedInfo
     <azure.mgmt.recoveryservicesbackup.models.MabContainerExtendedInfo>`
    """

    _validation = {
        'container_type': {'readonly': True},
        'protectable_object_type': {'required': True},
    }

    _attribute_map = {
        'friendly_name': {'key': 'friendlyName', 'type': 'str'},
        'backup_management_type': {'key': 'backupManagementType', 'type': 'str'},
        'registration_status': {'key': 'registrationStatus', 'type': 'str'},
        'health_status': {'key': 'healthStatus', 'type': 'str'},
        'container_type': {'key': 'containerType', 'type': 'str'},
        'protectable_object_type': {'key': 'protectableObjectType', 'type': 'str'},
        'can_re_register': {'key': 'canReRegister', 'type': 'bool'},
        'container_id': {'key': 'containerId', 'type': 'long'},
        'protected_item_count': {'key': 'protectedItemCount', 'type': 'long'},
        'agent_version': {'key': 'agentVersion', 'type': 'str'},
        'extended_info': {'key': 'extendedInfo', 'type': 'MabContainerExtendedInfo'},
    }

    def __init__(self, friendly_name=None, backup_management_type=None, registration_status=None, health_status=None, can_re_register=None, container_id=None, protected_item_count=None, agent_version=None, extended_info=None):
        super(MabContainer, self).__init__(friendly_name=friendly_name, backup_management_type=backup_management_type, registration_status=registration_status, health_status=health_status)
        self.can_re_register = can_re_register
        self.container_id = container_id
        self.protected_item_count = protected_item_count
        self.agent_version = agent_version
        self.extended_info = extended_info
        self.protectable_object_type = 'MABWindowsContainer'
