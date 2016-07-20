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


class CheckAvailabilityResource(Model):
    """Description of a CheckAvailibility resource.

    :param id: Gets or sets the id
    :type id: str
    :param location: Gets or sets datacenter location
    :type location: str
    :param name: Gets or sets name
    :type name: str
    :param type: Gets or sets resource type
    :type type: str
    :param tags: Gets or sets tags
    :type tags: dict
    :param is_availiable: Gets or sets true if the name is available and can
     be used to create new Namespace/NotificationHub. Otherwise false.
    :type is_availiable: bool
    """ 

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'is_availiable': {'key': 'isAvailiable', 'type': 'bool'},
    }

    def __init__(self, id=None, location=None, name=None, type=None, tags=None, is_availiable=None):
        self.id = id
        self.location = location
        self.name = name
        self.type = type
        self.tags = tags
        self.is_availiable = is_availiable
