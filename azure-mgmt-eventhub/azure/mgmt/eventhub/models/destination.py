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


class Destination(Model):
    """Capture storage details for capture description.

    :param name: Name for capture destination
    :type name: str
    :param storage_account_resource_id: Resource id of the storage account to
     be used to create the blobs
    :type storage_account_resource_id: str
    :param blob_container: Blob container Name
    :type blob_container: str
    :param archive_name_format: Blob naming convention for archive, e.g.
     {Namespace}/{EventHub}/{PartitionId}/{Year}/{Month}/{Day}/{Hour}/{Minute}/{Second}.
     Here all the parameters (Namespace,EventHub .. etc) are mandatory
     irrespective of order
    :type archive_name_format: str
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'storage_account_resource_id': {'key': 'properties.storageAccountResourceId', 'type': 'str'},
        'blob_container': {'key': 'properties.blobContainer', 'type': 'str'},
        'archive_name_format': {'key': 'properties.archiveNameFormat', 'type': 'str'},
    }

    def __init__(self, name=None, storage_account_resource_id=None, blob_container=None, archive_name_format=None):
        super(Destination, self).__init__()
        self.name = name
        self.storage_account_resource_id = storage_account_resource_id
        self.blob_container = blob_container
        self.archive_name_format = archive_name_format
