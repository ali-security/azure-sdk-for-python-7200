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


class USqlDistributionInfo(Model):
    """A Data Lake Analytics catalog U-SQL distribution information object.

    :param type: the type of this distribution.
    :type type: int
    :param keys: the list of directed columns in the distribution
    :type keys: list of :class:`USqlDirectedColumn
     <azure.mgmt.datalake.analytics.catalog.models.USqlDirectedColumn>`
    :param count: the count of indices using this distribution.
    :type count: int
    :param dynamic_count: the dynamic count of indices using this
     distribution.
    :type dynamic_count: int
    """ 

    _attribute_map = {
        'type': {'key': 'type', 'type': 'int'},
        'keys': {'key': 'keys', 'type': '[USqlDirectedColumn]'},
        'count': {'key': 'count', 'type': 'int'},
        'dynamic_count': {'key': 'dynamicCount', 'type': 'int'},
    }

    def __init__(self, type=None, keys=None, count=None, dynamic_count=None):
        self.type = type
        self.keys = keys
        self.count = count
        self.dynamic_count = dynamic_count
