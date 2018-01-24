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


class DatasetCompression(Model):
    """The compression method used on a dataset.

    You probably want to use the sub-classes and not this class directly. Known
    sub-classes are: DatasetZipDeflateCompression, DatasetDeflateCompression,
    DatasetGZipCompression, DatasetBZip2Compression

    :param additional_properties: Unmatched properties from the message are
     deserialized this collection
    :type additional_properties: dict[str, object]
    :param type: Constant filled by server.
    :type type: str
    """

    _validation = {
        'type': {'required': True},
    }

    _attribute_map = {
        'additional_properties': {'key': '', 'type': '{object}'},
        'type': {'key': 'type', 'type': 'str'},
    }

    _subtype_map = {
        'type': {'ZipDeflate': 'DatasetZipDeflateCompression', 'Deflate': 'DatasetDeflateCompression', 'GZip': 'DatasetGZipCompression', 'BZip2': 'DatasetBZip2Compression'}
    }

    def __init__(self, additional_properties=None):
        self.additional_properties = additional_properties
        self.type = None
