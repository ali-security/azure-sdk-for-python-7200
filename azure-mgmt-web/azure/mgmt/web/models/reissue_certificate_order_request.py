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


class ReissueCertificateOrderRequest(Resource):
    """Class representing certificate reissue request.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Resource Id.
    :vartype id: str
    :ivar name: Resource Name.
    :vartype name: str
    :param kind: Kind of resource.
    :type kind: str
    :param location: Resource Location.
    :type location: str
    :ivar type: Resource type.
    :vartype type: str
    :param tags: Resource tags.
    :type tags: dict[str, str]
    :param identity: Identity for the resource.
    :type identity: ~azure.mgmt.web.models.ResourceIdentity
    :param key_size: Certificate Key Size.
    :type key_size: int
    :param delay_existing_revoke_in_hours: Delay in hours to revoke existing
     certificate after the new certificate is issued.
    :type delay_existing_revoke_in_hours: int
    :param csr: Csr to be used for re-key operation.
    :type csr: str
    :param is_private_key_external: Should we change the ASC type (from
     managed private key to external private key and vice versa).
    :type is_private_key_external: bool
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'location': {'required': True},
        'type': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'kind': {'key': 'kind', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'identity': {'key': 'identity', 'type': 'ResourceIdentity'},
        'key_size': {'key': 'properties.keySize', 'type': 'int'},
        'delay_existing_revoke_in_hours': {'key': 'properties.delayExistingRevokeInHours', 'type': 'int'},
        'csr': {'key': 'properties.csr', 'type': 'str'},
        'is_private_key_external': {'key': 'properties.isPrivateKeyExternal', 'type': 'bool'},
    }

    def __init__(self, location, kind=None, tags=None, identity=None, key_size=None, delay_existing_revoke_in_hours=None, csr=None, is_private_key_external=None):
        super(ReissueCertificateOrderRequest, self).__init__(kind=kind, location=location, tags=tags, identity=identity)
        self.key_size = key_size
        self.delay_existing_revoke_in_hours = delay_existing_revoke_in_hours
        self.csr = csr
        self.is_private_key_external = is_private_key_external
