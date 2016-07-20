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


class PublicIPAddress(Resource):
    """PublicIPAddress resource.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :param id: Resource Id
    :type id: str
    :ivar name: Resource name
    :vartype name: str
    :ivar type: Resource type
    :vartype type: str
    :param location: Resource location
    :type location: str
    :param tags: Resource tags
    :type tags: dict
    :param public_ip_allocation_method: Gets or sets PublicIP allocation
     method (Static/Dynamic). Possible values include: 'Static', 'Dynamic'
    :type public_ip_allocation_method: str or :class:`IPAllocationMethod
     <azure.mgmt.network.models.IPAllocationMethod>`
    :param public_ip_address_version: Gets or sets PublicIP address version
     (IPv4/IPv6). Possible values include: 'IPv4', 'IPv6'
    :type public_ip_address_version: str or :class:`IPVersion
     <azure.mgmt.network.models.IPVersion>`
    :ivar ip_configuration:
    :vartype ip_configuration: :class:`IPConfiguration
     <azure.mgmt.network.models.IPConfiguration>`
    :param dns_settings: Gets or sets FQDN of the DNS record associated with
     the public IP address
    :type dns_settings: :class:`PublicIPAddressDnsSettings
     <azure.mgmt.network.models.PublicIPAddressDnsSettings>`
    :param ip_address:
    :type ip_address: str
    :param idle_timeout_in_minutes: Gets or sets the Idletimeout of the
     public IP address
    :type idle_timeout_in_minutes: int
    :param resource_guid: Gets or sets resource guid property of the PublicIP
     resource
    :type resource_guid: str
    :param provisioning_state: Gets provisioning state of the PublicIP
     resource Updating/Deleting/Failed
    :type provisioning_state: str
    :param etag: Gets a unique read-only string that changes whenever the
     resource is updated
    :type etag: str
    """ 

    _validation = {
        'name': {'readonly': True},
        'type': {'readonly': True},
        'ip_configuration': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'public_ip_allocation_method': {'key': 'properties.publicIPAllocationMethod', 'type': 'str'},
        'public_ip_address_version': {'key': 'properties.publicIPAddressVersion', 'type': 'str'},
        'ip_configuration': {'key': 'properties.ipConfiguration', 'type': 'IPConfiguration'},
        'dns_settings': {'key': 'properties.dnsSettings', 'type': 'PublicIPAddressDnsSettings'},
        'ip_address': {'key': 'properties.ipAddress', 'type': 'str'},
        'idle_timeout_in_minutes': {'key': 'properties.idleTimeoutInMinutes', 'type': 'int'},
        'resource_guid': {'key': 'properties.resourceGuid', 'type': 'str'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'etag': {'key': 'etag', 'type': 'str'},
    }

    def __init__(self, id=None, location=None, tags=None, public_ip_allocation_method=None, public_ip_address_version=None, dns_settings=None, ip_address=None, idle_timeout_in_minutes=None, resource_guid=None, provisioning_state=None, etag=None):
        super(PublicIPAddress, self).__init__(id=id, location=location, tags=tags)
        self.public_ip_allocation_method = public_ip_allocation_method
        self.public_ip_address_version = public_ip_address_version
        self.ip_configuration = None
        self.dns_settings = dns_settings
        self.ip_address = ip_address
        self.idle_timeout_in_minutes = idle_timeout_in_minutes
        self.resource_guid = resource_guid
        self.provisioning_state = provisioning_state
        self.etag = etag
