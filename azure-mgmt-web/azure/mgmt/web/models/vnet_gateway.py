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


class VnetGateway(Resource):
    """The Virtual Network gateway contract. This is used to give the Virtual
    Network gateway access to the VPN package.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Resource Id.
    :vartype id: str
    :param name: Resource Name.
    :type name: str
    :param kind: Kind of resource.
    :type kind: str
    :param location: Resource Location.
    :type location: str
    :param type: Resource type.
    :type type: str
    :param tags: Resource tags.
    :type tags: dict
    :param vnet_name: The Virtual Network name.
    :type vnet_name: str
    :param vpn_package_uri: The URI where the VPN package can be downloaded.
    :type vpn_package_uri: str
    """

    _validation = {
        'id': {'readonly': True},
        'location': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'kind': {'key': 'kind', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'vnet_name': {'key': 'properties.vnetName', 'type': 'str'},
        'vpn_package_uri': {'key': 'properties.vpnPackageUri', 'type': 'str'},
    }

    def __init__(self, location, name=None, kind=None, type=None, tags=None, vnet_name=None, vpn_package_uri=None):
        super(VnetGateway, self).__init__(name=name, kind=kind, location=location, type=type, tags=tags)
        self.vnet_name = vnet_name
        self.vpn_package_uri = vpn_package_uri
