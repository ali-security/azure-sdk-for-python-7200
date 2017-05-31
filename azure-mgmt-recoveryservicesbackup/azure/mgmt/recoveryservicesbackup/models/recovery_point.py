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


class RecoveryPoint(Model):
    """Base class for backup copies. Workload-specific backup copies are derived
    from this class.

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
        'object_type': {'GenericRecoveryPoint': 'GenericRecoveryPoint', 'IaasVMRecoveryPoint': 'IaasVMRecoveryPoint'}
    }

    def __init__(self):
        self.object_type = None
