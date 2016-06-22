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


class TaskExecutionInformation(Model):
    """Information about the execution of a task.

    :param start_time: The time at which the task started running. If the
     task has been restarted or retried, this is the most recent time at
     which the task started running.
    :type start_time: datetime
    :param end_time: The time at which the task completed. This property is
     set only if the task is in the Completed state.
    :type end_time: datetime
    :param exit_code: The exit code of the task. This property is set only if
     the task is in completed state.
    :type exit_code: int
    :param scheduling_error: Details of any error encountered scheduling the
     task.
    :type scheduling_error: :class:`TaskSchedulingError
     <azure.batch.models.TaskSchedulingError>`
    :param retry_count: The number of times the task has been retried by the
     Batch service.
    :type retry_count: int
    :param last_retry_time: The most recent time at which a retry of the task
     started running.
    :type last_retry_time: datetime
    :param requeue_count: The number of times the task has been requeued by
     the Batch service as the result of a user request.
    :type requeue_count: int
    :param last_requeue_time: The most recent time at which the task has been
     requeued by the Batch service as the result of a user request.
    :type last_requeue_time: datetime
    """ 

    _validation = {
        'retry_count': {'required': True},
        'requeue_count': {'required': True},
    }

    _attribute_map = {
        'start_time': {'key': 'startTime', 'type': 'iso-8601'},
        'end_time': {'key': 'endTime', 'type': 'iso-8601'},
        'exit_code': {'key': 'exitCode', 'type': 'int'},
        'scheduling_error': {'key': 'schedulingError', 'type': 'TaskSchedulingError'},
        'retry_count': {'key': 'retryCount', 'type': 'int'},
        'last_retry_time': {'key': 'lastRetryTime', 'type': 'iso-8601'},
        'requeue_count': {'key': 'requeueCount', 'type': 'int'},
        'last_requeue_time': {'key': 'lastRequeueTime', 'type': 'iso-8601'},
    }

    def __init__(self, retry_count, requeue_count, start_time=None, end_time=None, exit_code=None, scheduling_error=None, last_retry_time=None, last_requeue_time=None):
        self.start_time = start_time
        self.end_time = end_time
        self.exit_code = exit_code
        self.scheduling_error = scheduling_error
        self.retry_count = retry_count
        self.last_retry_time = last_retry_time
        self.requeue_count = requeue_count
        self.last_requeue_time = last_requeue_time
