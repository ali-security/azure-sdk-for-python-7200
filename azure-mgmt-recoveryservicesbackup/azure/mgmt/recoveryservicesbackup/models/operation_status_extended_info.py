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


class OperationStatusExtendedInfo(Model):
    """Base class for additional information of operation status.

    :param object_type: Polymorphic Discriminator
    :type object_type: str
    """

    _validation = {
        'object_type': {'required': True},
    }

    _attribute_map = {
        'object_type': {'key': 'objectType', 'type': 'str'},
    }

    _subtype_map = {
        'object_type': {'OperationStatusJobExtendedInfo': 'OperationStatusJobExtendedInfo', 'OperationStatusJobsExtendedInfo': 'OperationStatusJobsExtendedInfo', 'OperationStatusProvisionILRExtendedInfo': 'OperationStatusProvisionILRExtendedInfo'}
    }

    def __init__(self):
        self.object_type = None
