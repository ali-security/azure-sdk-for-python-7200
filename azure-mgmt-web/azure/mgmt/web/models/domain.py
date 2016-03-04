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

from .resource import Resource


class Domain(Resource):
    """
    Represents a domain

    :param str id: Resource Id
    :param str name: Resource Name
    :param str location: Resource Location
    :param str type: Resource type
    :param dict tags: Resource tags
    :param Contact contact_admin: Admin contact information
    :param Contact contact_billing: Billing contact information
    :param Contact contact_registrant: Registrant contact information
    :param Contact contact_tech: Technical contact information
    :param str registration_status: Domain registration status. Possible
     values include: 'Active', 'Awaiting', 'Cancelled', 'Confiscated',
     'Disabled', 'Excluded', 'Expired', 'Failed', 'Held', 'Locked', 'Parked',
     'Pending', 'Reserved', 'Reverted', 'Suspended', 'Transferred',
     'Unknown', 'Unlocked', 'Unparked', 'Updated', 'JsonConverterFailed'
    :param str provisioning_state: Domain provisioning state. Possible values
     include: 'Succeeded', 'Failed', 'Canceled', 'InProgress', 'Deleting'
    :param list name_servers: Name servers
    :param bool privacy: If true then domain privacy is enabled for this
     domain
    :param datetime created_time: Domain creation timestamp
    :param datetime expiration_time: Domain expiration timestamp
    :param datetime last_renewed_time: Timestamp when the domain was renewed
     last time
    :param bool auto_renew: If true then domain will renewed automatically
    :param bool ready_for_dns_record_management: If true then Azure can
     assign this domain to Web Apps. This value will be true if domain
     registration status is active and it is hosted on name servers Azure has
     programmatic access to
    :param list managed_host_names: All hostnames derived from the domain and
     assigned to Azure resources
    :param DomainPurchaseConsent consent: Legal agreement consent
    """ 

    _validation = {
        'location': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'contact_admin': {'key': 'properties.contactAdmin', 'type': 'Contact'},
        'contact_billing': {'key': 'properties.contactBilling', 'type': 'Contact'},
        'contact_registrant': {'key': 'properties.contactRegistrant', 'type': 'Contact'},
        'contact_tech': {'key': 'properties.contactTech', 'type': 'Contact'},
        'registration_status': {'key': 'properties.registrationStatus', 'type': 'DomainStatus'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'ProvisioningState'},
        'name_servers': {'key': 'properties.nameServers', 'type': '[str]'},
        'privacy': {'key': 'properties.privacy', 'type': 'bool'},
        'created_time': {'key': 'properties.createdTime', 'type': 'iso-8601'},
        'expiration_time': {'key': 'properties.expirationTime', 'type': 'iso-8601'},
        'last_renewed_time': {'key': 'properties.lastRenewedTime', 'type': 'iso-8601'},
        'auto_renew': {'key': 'properties.autoRenew', 'type': 'bool'},
        'ready_for_dns_record_management': {'key': 'properties.readyForDnsRecordManagement', 'type': 'bool'},
        'managed_host_names': {'key': 'properties.managedHostNames', 'type': '[HostName]'},
        'consent': {'key': 'properties.consent', 'type': 'DomainPurchaseConsent'},
    }

    def __init__(self, location, id=None, name=None, type=None, tags=None, contact_admin=None, contact_billing=None, contact_registrant=None, contact_tech=None, registration_status=None, provisioning_state=None, name_servers=None, privacy=None, created_time=None, expiration_time=None, last_renewed_time=None, auto_renew=None, ready_for_dns_record_management=None, managed_host_names=None, consent=None, **kwargs):
        super(Domain, self).__init__(id=id, name=name, location=location, type=type, tags=tags, **kwargs)
        self.contact_admin = contact_admin
        self.contact_billing = contact_billing
        self.contact_registrant = contact_registrant
        self.contact_tech = contact_tech
        self.registration_status = registration_status
        self.provisioning_state = provisioning_state
        self.name_servers = name_servers
        self.privacy = privacy
        self.created_time = created_time
        self.expiration_time = expiration_time
        self.last_renewed_time = last_renewed_time
        self.auto_renew = auto_renew
        self.ready_for_dns_record_management = ready_for_dns_record_management
        self.managed_host_names = managed_host_names
        self.consent = consent
