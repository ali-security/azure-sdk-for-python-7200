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


class ActivityDependency(Model):
    """Activity dependency information.

    :param additional_properties: Unmatched properties from the message are
     deserialized this collection
    :type additional_properties: dict[str, object]
    :param activity: Activity name.
    :type activity: str
    :param dependency_conditions: Match-Condition for the dependency.
    :type dependency_conditions: list[str or
     ~azure.mgmt.datafactory.models.DependencyCondition]
    """

    _validation = {
        'activity': {'required': True},
        'dependency_conditions': {'required': True},
    }

    _attribute_map = {
        'additional_properties': {'key': '', 'type': '{object}'},
        'activity': {'key': 'activity', 'type': 'str'},
        'dependency_conditions': {'key': 'dependencyConditions', 'type': '[str]'},
    }

    def __init__(self, activity, dependency_conditions, additional_properties=None):
        self.additional_properties = additional_properties
        self.activity = activity
        self.dependency_conditions = dependency_conditions
