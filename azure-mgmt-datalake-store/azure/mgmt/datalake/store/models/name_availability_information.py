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


class NameAvailabilityInformation(Model):
    """Data Lake Store account name availability result information.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar name_available: the Boolean value of true or false to indicate
     whether the Data Lake Store account name is available or not.
    :vartype name_available: bool
    :ivar reason: the reason why the Data Lake Store account name is not
     available, if nameAvailable is false.
    :vartype reason: str
    :ivar message: the message describing why the Data Lake Store account name
     is not available, if nameAvailable is false.
    :vartype message: str
    """

    _validation = {
        'name_available': {'readonly': True},
        'reason': {'readonly': True},
        'message': {'readonly': True},
    }

    _attribute_map = {
        'name_available': {'key': 'nameAvailable', 'type': 'bool'},
        'reason': {'key': 'reason', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
    }

    def __init__(self):
        super(NameAvailabilityInformation, self).__init__()
        self.name_available = None
        self.reason = None
        self.message = None
