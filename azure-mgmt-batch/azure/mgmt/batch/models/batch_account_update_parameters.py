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


class BatchAccountUpdateParameters(Model):
    """Parameters supplied to the Update operation.

    :param tags: The user specified tags associated with the account.
    :type tags: dict
    :param auto_storage: The properties related to auto storage account.
    :type auto_storage: :class:`AutoStorageBaseProperties
     <azure.mgmt.batch.models.AutoStorageBaseProperties>`
    """ 

    _attribute_map = {
        'tags': {'key': 'tags', 'type': '{str}'},
        'auto_storage': {'key': 'properties.autoStorage', 'type': 'AutoStorageBaseProperties'},
    }

    def __init__(self, tags=None, auto_storage=None):
        self.tags = tags
        self.auto_storage = auto_storage
