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


class IntegrationRuntimeAuthKeys(Model):
    """The integration runtime authentication keys.

    :param auth_key1: The primary integration runtime authentication key.
    :type auth_key1: str
    :param auth_key2: The secondary integration runtime authentication key.
    :type auth_key2: str
    """

    _attribute_map = {
        'auth_key1': {'key': 'authKey1', 'type': 'str'},
        'auth_key2': {'key': 'authKey2', 'type': 'str'},
    }

    def __init__(self, auth_key1=None, auth_key2=None):
        self.auth_key1 = auth_key1
        self.auth_key2 = auth_key2
