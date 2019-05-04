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


class QueryComparisonExpression(Model):
    """The comparison expression to be used in the query.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :param name: Required. The name of the column to use in comparison.
    :type name: str
    :ivar operator: Required. The operator to use for comparison. Default
     value: "In" .
    :vartype operator: str
    :param values: Required. Array of values to use for comparison
    :type values: list[str]
    """

    _validation = {
        'name': {'required': True},
        'operator': {'required': True, 'constant': True},
        'values': {'required': True, 'min_items': 1},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'operator': {'key': 'operator', 'type': 'str'},
        'values': {'key': 'values', 'type': '[str]'},
    }

    operator = "In"

    def __init__(self, *, name: str, values, **kwargs) -> None:
        super(QueryComparisonExpression, self).__init__(**kwargs)
        self.name = name
        self.values = values
