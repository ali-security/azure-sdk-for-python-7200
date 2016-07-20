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

from .resource import Resource


class TopLevelDomain(Resource):
    """A top level domain object.

    :param id: Resource Id
    :type id: str
    :param name: Resource Name
    :type name: str
    :param kind: Kind of resource
    :type kind: str
    :param location: Resource Location
    :type location: str
    :param type: Resource type
    :type type: str
    :param tags: Resource tags
    :type tags: dict
    :param top_level_domain_name: Name of the top level domain
    :type top_level_domain_name: str
    :param privacy: If true then the top level domain supports domain privacy
    :type privacy: bool
    """ 

    _validation = {
        'location': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'kind': {'key': 'kind', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'top_level_domain_name': {'key': 'properties.name', 'type': 'str'},
        'privacy': {'key': 'properties.privacy', 'type': 'bool'},
    }

    def __init__(self, location, id=None, name=None, kind=None, type=None, tags=None, top_level_domain_name=None, privacy=None):
        super(TopLevelDomain, self).__init__(id=id, name=name, kind=kind, location=location, type=type, tags=tags)
        self.top_level_domain_name = top_level_domain_name
        self.privacy = privacy
