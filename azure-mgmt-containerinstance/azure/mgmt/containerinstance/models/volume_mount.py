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


class VolumeMount(Model):
    """The volume mount.

    :param name: The volume mount name.
    :type name: str
    :param mount_path: The path with in the container at which the volume
     should be mounted. Must not contain ':'.
    :type mount_path: str
    :param read_only: The flag indicating whether the volume mount is read
     only.
    :type read_only: bool
    """

    _validation = {
        'name': {'required': True},
        'mount_path': {'required': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'mount_path': {'key': 'mountPath', 'type': 'str'},
        'read_only': {'key': 'readOnly', 'type': 'bool'},
    }

    def __init__(self, name, mount_path, read_only=None):
        self.name = name
        self.mount_path = mount_path
        self.read_only = read_only
