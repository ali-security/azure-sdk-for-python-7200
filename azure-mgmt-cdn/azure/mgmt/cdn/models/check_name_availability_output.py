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


class CheckNameAvailabilityOutput(Model):
    """
    Output of check name availability API

    :param bool name_available: Indicates whether the name is available
    :param str reason: The reason why the name is not available
    :param str message: The detailed error message on why the name is not
     available
    """ 

    _attribute_map = {
        'name_available': {'key': 'NameAvailable', 'type': 'bool'},
        'reason': {'key': 'Reason', 'type': 'str'},
        'message': {'key': 'Message', 'type': 'str'},
    }

    def __init__(self, name_available=None, reason=None, message=None, **kwargs):
        self.name_available = name_available
        self.reason = reason
        self.message = message
