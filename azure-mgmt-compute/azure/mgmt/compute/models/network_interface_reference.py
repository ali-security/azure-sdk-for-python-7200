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

from .sub_resource import SubResource


class NetworkInterfaceReference(SubResource):
    """
    Describes a network interface reference.

    :param str id: Resource Id
    :param bool primary: Gets or sets whether this is a primary NIC on a
     virtual machine
    """

    _required = []

    _attribute_map = {
        'primary': {'key': 'properties.primary', 'type': 'bool', 'flatten': True},
    }

    def __init__(self, id=None, primary=None):
        super(NetworkInterfaceReference, self).__init__(id=id)
        self.primary = primary
