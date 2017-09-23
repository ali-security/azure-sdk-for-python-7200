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

from .partition_information import PartitionInformation


class NamedPartitionInformation(PartitionInformation):
    """Describes the partition information for the name as a string that is based
    on partition schemes.

    :param id:
    :type id: str
    :param service_partition_kind: Polymorphic Discriminator
    :type service_partition_kind: str
    :param name: Name of the partition.
    :type name: str
    """

    _validation = {
        'service_partition_kind': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'Id', 'type': 'str'},
        'service_partition_kind': {'key': 'ServicePartitionKind', 'type': 'str'},
        'name': {'key': 'Name', 'type': 'str'},
    }

    def __init__(self, id=None, name=None):
        super(NamedPartitionInformation, self).__init__(id=id)
        self.name = name
        self.service_partition_kind = 'Named'
