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


class AdditionalUnattendContent(Model):
    """Additional XML formatted information that can be included in the
    Unattend.xml file, which is used by Windows Setup. Contents are defined
    by setting name, component name, and the pass in which the content is a
    applied.

    :param pass_name: The pass name. Currently, the only allowable value is
     oobeSystem. Possible values include: 'oobeSystem'
    :type pass_name: str or :class:`PassNames
     <azure.mgmt.compute.models.PassNames>`
    :param component_name: The component name. Currently, the only allowable
     value is Microsoft-Windows-Shell-Setup. Possible values include:
     'Microsoft-Windows-Shell-Setup'
    :type component_name: str or :class:`ComponentNames
     <azure.mgmt.compute.models.ComponentNames>`
    :param setting_name: setting name (e.g. FirstLogonCommands, AutoLogon ).
     Possible values include: 'AutoLogon', 'FirstLogonCommands'
    :type setting_name: str or :class:`SettingNames
     <azure.mgmt.compute.models.SettingNames>`
    :param content: XML formatted content that is added to the unattend.xml
     file in the specified pass and component. The XML must be less than 4 KB
     and must include the root element for the setting or feature that is
     being inserted.
    :type content: str
    """ 

    _attribute_map = {
        'pass_name': {'key': 'passName', 'type': 'PassNames'},
        'component_name': {'key': 'componentName', 'type': 'ComponentNames'},
        'setting_name': {'key': 'settingName', 'type': 'SettingNames'},
        'content': {'key': 'content', 'type': 'str'},
    }

    def __init__(self, pass_name=None, component_name=None, setting_name=None, content=None):
        self.pass_name = pass_name
        self.component_name = component_name
        self.setting_name = setting_name
        self.content = content
