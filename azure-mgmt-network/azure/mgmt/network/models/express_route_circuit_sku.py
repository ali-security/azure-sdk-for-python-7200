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


class ExpressRouteCircuitSku(Model):
    """Contains SKU in an ExpressRouteCircuit.

    :param name: The name of the SKU.
    :type name: str
    :param tier: The tier of the SKU. Possible values are 'Standard' and
     'Premium'. Possible values include: 'Standard', 'Premium'
    :type tier: str or :class:`ExpressRouteCircuitSkuTier
     <azure.mgmt.network.models.ExpressRouteCircuitSkuTier>`
    :param family: The family of the SKU. Possible values are:
     'UnlimitedData' and 'MeteredData'. Possible values include:
     'UnlimitedData', 'MeteredData'
    :type family: str or :class:`ExpressRouteCircuitSkuFamily
     <azure.mgmt.network.models.ExpressRouteCircuitSkuFamily>`
    """ 

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'tier': {'key': 'tier', 'type': 'str'},
        'family': {'key': 'family', 'type': 'str'},
    }

    def __init__(self, name=None, tier=None, family=None):
        self.name = name
        self.tier = tier
        self.family = family
