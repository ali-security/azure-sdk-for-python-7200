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


class PacketCaptureStorageLocation(Model):
    """Describes the storage location for a packet capture session.

    :param storage_id: The ID of the storage account to save the packet
     capture session. Required if no local file path is provided.
    :type storage_id: str
    :param storage_path: The URI of the storage path to save the packet
     capture. Must be a well-formed URI describing the location to save the
     packet capture.
    :type storage_path: str
    :param file_path: A valid local path on the targeting VM. Must include the
     name of the capture file (*.cap). For linux virtual machine it must start
     with /var/captures. Required if no storage ID is provided, otherwise
     optional.
    :type file_path: str
    """

    _attribute_map = {
        'storage_id': {'key': 'storageId', 'type': 'str'},
        'storage_path': {'key': 'storagePath', 'type': 'str'},
        'file_path': {'key': 'filePath', 'type': 'str'},
    }

    def __init__(self, storage_id=None, storage_path=None, file_path=None):
        super(PacketCaptureStorageLocation, self).__init__()
        self.storage_id = storage_id
        self.storage_path = storage_path
        self.file_path = file_path
