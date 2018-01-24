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


class RunCommandDocumentBase(Model):
    """Describes the properties of a Run Command metadata.

    :param schema: The VM run command schema.
    :type schema: str
    :param id: The VM run command id.
    :type id: str
    :param os_type: The Operating System type. Possible values include:
     'Windows', 'Linux'
    :type os_type: str or
     ~azure.mgmt.compute.v2017_03_30.models.OperatingSystemTypes
    :param label: The VM run command label.
    :type label: str
    :param description: The VM run command description.
    :type description: str
    """

    _validation = {
        'schema': {'required': True},
        'id': {'required': True},
        'os_type': {'required': True},
        'label': {'required': True},
        'description': {'required': True},
    }

    _attribute_map = {
        'schema': {'key': '$schema', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'os_type': {'key': 'osType', 'type': 'OperatingSystemTypes'},
        'label': {'key': 'label', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
    }

    def __init__(self, schema, id, os_type, label, description):
        super(RunCommandDocumentBase, self).__init__()
        self.schema = schema
        self.id = id
        self.os_type = os_type
        self.label = label
        self.description = description
