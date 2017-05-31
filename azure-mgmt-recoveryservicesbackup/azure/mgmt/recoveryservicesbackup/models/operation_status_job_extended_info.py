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

from .operation_status_extended_info import OperationStatusExtendedInfo


class OperationStatusJobExtendedInfo(OperationStatusExtendedInfo):
    """Operation status job extended info.

    :param object_type: Polymorphic Discriminator
    :type object_type: str
    :param job_id: ID of the job created for this protected item.
    :type job_id: str
    """

    _validation = {
        'object_type': {'required': True},
    }

    _attribute_map = {
        'object_type': {'key': 'objectType', 'type': 'str'},
        'job_id': {'key': 'jobId', 'type': 'str'},
    }

    def __init__(self, job_id=None):
        super(OperationStatusJobExtendedInfo, self).__init__()
        self.job_id = job_id
        self.object_type = 'OperationStatusJobExtendedInfo'
