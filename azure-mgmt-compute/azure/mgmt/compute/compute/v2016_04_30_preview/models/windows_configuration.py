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


class WindowsConfiguration(Model):
    """Describes Windows Configuration of the OS Profile.

    :param provision_vm_agent: Indicates whether the virtual machine agent
     should be provisioned on the Virtual Machine. If not specified, then the
     default behavior is to set it to true.
    :type provision_vm_agent: bool
    :param enable_automatic_updates: Indicates whether Windows updates are
     automatically installed on the VM.
    :type enable_automatic_updates: bool
    :param time_zone: The time zone of the VM
    :type time_zone: str
    :param additional_unattend_content: Additional base-64 encoded XML
     formatted information that can be included in the Unattend.xml file.
    :type additional_unattend_content: list of
     :class:`AdditionalUnattendContent
     <azure.mgmt.compute.compute.v20160430preview.models.AdditionalUnattendContent>`
    :param win_rm: The Windows Remote Management configuration of the VM
    :type win_rm: :class:`WinRMConfiguration
     <azure.mgmt.compute.compute.v20160430preview.models.WinRMConfiguration>`
    """

    _attribute_map = {
        'provision_vm_agent': {'key': 'provisionVMAgent', 'type': 'bool'},
        'enable_automatic_updates': {'key': 'enableAutomaticUpdates', 'type': 'bool'},
        'time_zone': {'key': 'timeZone', 'type': 'str'},
        'additional_unattend_content': {'key': 'additionalUnattendContent', 'type': '[AdditionalUnattendContent]'},
        'win_rm': {'key': 'winRM', 'type': 'WinRMConfiguration'},
    }

    def __init__(self, provision_vm_agent=None, enable_automatic_updates=None, time_zone=None, additional_unattend_content=None, win_rm=None):
        self.provision_vm_agent = provision_vm_agent
        self.enable_automatic_updates = enable_automatic_updates
        self.time_zone = time_zone
        self.additional_unattend_content = additional_unattend_content
        self.win_rm = win_rm
