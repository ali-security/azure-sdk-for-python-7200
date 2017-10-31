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
    """Represents an operation returned by the GetOperations request.

    :param name: Name of the operation
    :type name: str
    :param display: Display name of the operation
    :type display: ~azure.mgmt.eventgrid.models.OperationInfo
    :param origin: Origin of the operation. Possible values include: 'User',
     'System', 'UserAndSystem'
    :type origin: str or ~azure.mgmt.eventgrid.models.OperationOrigin
    :param properties: Properties of the operation
    :type properties: object
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'display': {'key': 'display', 'type': 'OperationInfo'},
        'origin': {'key': 'origin', 'type': 'str'},
        'properties': {'key': 'properties', 'type': 'object'},
    }

    def __init__(self, name=None, display=None, origin=None, properties=None):
        self.name = name
        self.display = display
        self.origin = origin
        self.properties = properties
