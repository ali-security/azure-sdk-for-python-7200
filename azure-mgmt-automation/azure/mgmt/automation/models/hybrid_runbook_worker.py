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


class HybridRunbookWorker(Model):
    """Definition of hybrid runbook worker.

    :param name: Gets or sets the worker machine name.
    :type name: str
    :param ip: Gets or sets the assigned machine IP address.
    :type ip: str
    :param registration_time: Gets or sets the registration time of the worker
     machine.
    :type registration_time: datetime
    :param last_seen_date_time: Last Heartbeat from the Worker
    :type last_seen_date_time: datetime
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'ip': {'key': 'ip', 'type': 'str'},
        'registration_time': {'key': 'registrationTime', 'type': 'iso-8601'},
        'last_seen_date_time': {'key': 'lastSeenDateTime', 'type': 'iso-8601'},
    }

    def __init__(self, **kwargs):
        super(HybridRunbookWorker, self).__init__(**kwargs)
        self.name = kwargs.get('name', None)
        self.ip = kwargs.get('ip', None)
        self.registration_time = kwargs.get('registration_time', None)
        self.last_seen_date_time = kwargs.get('last_seen_date_time', None)
