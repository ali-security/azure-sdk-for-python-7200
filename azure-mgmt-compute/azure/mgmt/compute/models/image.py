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


class Image(Resource):
    """Describes an Image.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Resource Id
    :vartype id: str
    :ivar name: Resource name
    :vartype name: str
    :ivar type: Resource type
    :vartype type: str
    :param location: Resource location
    :type location: str
    :param tags: Resource tags
    :type tags: dict
    :param source_virtual_machine: The source virtual machine from which Image
     is created.
    :type source_virtual_machine: :class:`SubResource
     <azure.mgmt.compute.models.SubResource>`
    :param storage_profile: The storage profile.
    :type storage_profile: :class:`ImageStorageProfile
     <azure.mgmt.compute.models.ImageStorageProfile>`
    :ivar provisioning_state: The provisioning state.
    :vartype provisioning_state: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'location': {'required': True},
        'provisioning_state': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'source_virtual_machine': {'key': 'properties.sourceVirtualMachine', 'type': 'SubResource'},
        'storage_profile': {'key': 'properties.storageProfile', 'type': 'ImageStorageProfile'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
    }

    def __init__(self, location, tags=None, source_virtual_machine=None, storage_profile=None):
        super(Image, self).__init__(location=location, tags=tags)
        self.source_virtual_machine = source_virtual_machine
        self.storage_profile = storage_profile
        self.provisioning_state = None
