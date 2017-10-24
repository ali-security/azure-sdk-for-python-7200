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


class GlobalCsmSkuDescription(Model):
    """A Global SKU Description.

    :param name: Name of the resource SKU.
    :type name: str
    :param tier: Service Tier of the resource SKU.
    :type tier: str
    :param size: Size specifier of the resource SKU.
    :type size: str
    :param family: Family code of the resource SKU.
    :type family: str
    :param capacity: Min, max, and default scale values of the SKU.
    :type capacity: ~azure.mgmt.web.models.SkuCapacity
    :param locations: Locations of the SKU.
    :type locations: list[str]
    :param capabilities: Capabilities of the SKU, e.g., is traffic manager
     enabled?
    :type capabilities: list[~azure.mgmt.web.models.Capability]
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'tier': {'key': 'tier', 'type': 'str'},
        'size': {'key': 'size', 'type': 'str'},
        'family': {'key': 'family', 'type': 'str'},
        'capacity': {'key': 'capacity', 'type': 'SkuCapacity'},
        'locations': {'key': 'locations', 'type': '[str]'},
        'capabilities': {'key': 'capabilities', 'type': '[Capability]'},
    }

    def __init__(self, name=None, tier=None, size=None, family=None, capacity=None, locations=None, capabilities=None):
        self.name = name
        self.tier = tier
        self.size = size
        self.family = family
        self.capacity = capacity
        self.locations = locations
        self.capabilities = capabilities
