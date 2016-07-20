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


class JobRecurrence(Model):
    """JobRecurrence.

    :param frequency: Gets or sets the frequency of recurrence (second,
     minute, hour, day, week, month). Possible values include: 'Minute',
     'Hour', 'Day', 'Week', 'Month'
    :type frequency: str or :class:`RecurrenceFrequency
     <azure.mgmt.scheduler.models.RecurrenceFrequency>`
    :param interval: Gets or sets the interval between retries.
    :type interval: int
    :param count: Gets or sets the maximum number of times that the job
     should run.
    :type count: int
    :param end_time: Gets or sets the time at which the job will complete.
    :type end_time: datetime
    :param schedule:
    :type schedule: :class:`JobRecurrenceSchedule
     <azure.mgmt.scheduler.models.JobRecurrenceSchedule>`
    """ 

    _attribute_map = {
        'frequency': {'key': 'frequency', 'type': 'RecurrenceFrequency'},
        'interval': {'key': 'interval', 'type': 'int'},
        'count': {'key': 'count', 'type': 'int'},
        'end_time': {'key': 'endTime', 'type': 'iso-8601'},
        'schedule': {'key': 'schedule', 'type': 'JobRecurrenceSchedule'},
    }

    def __init__(self, frequency=None, interval=None, count=None, end_time=None, schedule=None):
        self.frequency = frequency
        self.interval = interval
        self.count = count
        self.end_time = end_time
        self.schedule = schedule
