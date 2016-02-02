# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft and contributors.  All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .sub_resource import SubResource


class VirtualMachineScaleSetExtension(SubResource):
    """
    Describes a Virtual Machine Scale Set Extension.

    :param str id: Resource Id
    :param str name: Gets or sets the name of the extension.
    :param str publisher: Gets or sets the name of the extension handler
     publisher.
    :param str virtual_machine_scale_set_extension_type: Gets or sets the
     type of the extension handler.
    :param str type_handler_version: Gets or sets the type version of the
     extension handler.
    :param bool auto_upgrade_minor_version: Gets or sets whether the
     extension handler should be automatically upgraded across minor versions.
    :param object settings: Gets or sets Json formatted public settings for
     the extension.
    :param object protected_settings: Gets or sets Json formatted protected
     settings for the extension.
    :param str provisioning_state: Gets the provisioning state, which only
     appears in the response.
    """

    _required = []

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'publisher': {'key': 'properties.publisher', 'type': 'str', 'flatten': True},
        'virtual_machine_scale_set_extension_type': {'key': 'properties.type', 'type': 'str', 'flatten': True},
        'type_handler_version': {'key': 'properties.typeHandlerVersion', 'type': 'str', 'flatten': True},
        'auto_upgrade_minor_version': {'key': 'properties.autoUpgradeMinorVersion', 'type': 'bool', 'flatten': True},
        'settings': {'key': 'properties.settings', 'type': 'object', 'flatten': True},
        'protected_settings': {'key': 'properties.protectedSettings', 'type': 'object', 'flatten': True},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str', 'flatten': True},
    }

    def __init__(self, id=None, name=None, publisher=None, virtual_machine_scale_set_extension_type=None, type_handler_version=None, auto_upgrade_minor_version=None, settings=None, protected_settings=None, provisioning_state=None):
        super(VirtualMachineScaleSetExtension, self).__init__(id=id)
        self.name = name
        self.publisher = publisher
        self.virtual_machine_scale_set_extension_type = virtual_machine_scale_set_extension_type
        self.type_handler_version = type_handler_version
        self.auto_upgrade_minor_version = auto_upgrade_minor_version
        self.settings = settings
        self.protected_settings = protected_settings
        self.provisioning_state = provisioning_state
