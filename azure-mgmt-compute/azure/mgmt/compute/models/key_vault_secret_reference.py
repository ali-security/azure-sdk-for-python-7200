# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft and contributors.  All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class KeyVaultSecretReference(Model):
    """Describes a reference to Key Vault Secret.

    :param secret_url: the URL referencing a secret in a Key Vault.
    :type secret_url: str
    :param source_vault: the Relative URL of the Key Vault containing the
     secret.
    :type source_vault: :class:`SubResource
     <azure.mgmt.compute.models.SubResource>`
    """ 

    _validation = {
        'secret_url': {'required': True},
        'source_vault': {'required': True},
    }

    _attribute_map = {
        'secret_url': {'key': 'secretUrl', 'type': 'str'},
        'source_vault': {'key': 'sourceVault', 'type': 'SubResource'},
    }

    def __init__(self, secret_url, source_vault):
        self.secret_url = secret_url
        self.source_vault = source_vault
