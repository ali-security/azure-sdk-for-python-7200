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


class Operation(Model):
    """Represents an operation that can be performed on the service.

    :param name: The name of the operation.
    :type name: str
    :param display: The display name of the operation.
    :type display: ~azure.mgmt.deploymentmanager.models.OperationDetail
    :param origin: The origin of the operation.
    :type origin: str
    :param properties: The properties of the operation.
    :type properties: object
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'display': {'key': 'display', 'type': 'OperationDetail'},
        'origin': {'key': 'origin', 'type': 'str'},
        'properties': {'key': 'properties', 'type': 'object'},
    }

    def __init__(self, *, name: str=None, display=None, origin: str=None, properties=None, **kwargs) -> None:
        super(Operation, self).__init__(**kwargs)
        self.name = name
        self.display = display
        self.origin = origin
        self.properties = properties
