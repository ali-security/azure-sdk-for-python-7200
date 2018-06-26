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


class JobPipelineInformation(Model):
    """Job Pipeline Information, showing the relationship of jobs and recurrences
    of those jobs in a pipeline.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar pipeline_id: The job relationship pipeline identifier (a GUID).
    :vartype pipeline_id: str
    :ivar pipeline_name: The friendly name of the job relationship pipeline,
     which does not need to be unique.
    :vartype pipeline_name: str
    :ivar pipeline_uri: The pipeline uri, unique, links to the originating
     service for this pipeline.
    :vartype pipeline_uri: str
    :ivar num_jobs_failed: The number of jobs in this pipeline that have
     failed.
    :vartype num_jobs_failed: int
    :ivar num_jobs_canceled: The number of jobs in this pipeline that have
     been canceled.
    :vartype num_jobs_canceled: int
    :ivar num_jobs_succeeded: The number of jobs in this pipeline that have
     succeeded.
    :vartype num_jobs_succeeded: int
    :ivar au_hours_failed: The number of job execution hours that resulted in
     failed jobs.
    :vartype au_hours_failed: float
    :ivar au_hours_canceled: The number of job execution hours that resulted
     in canceled jobs.
    :vartype au_hours_canceled: float
    :ivar au_hours_succeeded: The number of job execution hours that resulted
     in successful jobs.
    :vartype au_hours_succeeded: float
    :ivar last_submit_time: The last time a job in this pipeline was
     submitted.
    :vartype last_submit_time: datetime
    :ivar runs: The list of recurrence identifiers representing each run of
     this pipeline.
    :vartype runs:
     list[~azure.mgmt.datalake.analytics.job.models.JobPipelineRunInformation]
    :ivar recurrences: The list of recurrence identifiers representing each
     run of this pipeline.
    :vartype recurrences: list[str]
    """

    _validation = {
        'pipeline_id': {'readonly': True},
        'pipeline_name': {'readonly': True, 'max_length': 260},
        'pipeline_uri': {'readonly': True},
        'num_jobs_failed': {'readonly': True},
        'num_jobs_canceled': {'readonly': True},
        'num_jobs_succeeded': {'readonly': True},
        'au_hours_failed': {'readonly': True},
        'au_hours_canceled': {'readonly': True},
        'au_hours_succeeded': {'readonly': True},
        'last_submit_time': {'readonly': True},
        'runs': {'readonly': True},
        'recurrences': {'readonly': True},
    }

    _attribute_map = {
        'pipeline_id': {'key': 'pipelineId', 'type': 'str'},
        'pipeline_name': {'key': 'pipelineName', 'type': 'str'},
        'pipeline_uri': {'key': 'pipelineUri', 'type': 'str'},
        'num_jobs_failed': {'key': 'numJobsFailed', 'type': 'int'},
        'num_jobs_canceled': {'key': 'numJobsCanceled', 'type': 'int'},
        'num_jobs_succeeded': {'key': 'numJobsSucceeded', 'type': 'int'},
        'au_hours_failed': {'key': 'auHoursFailed', 'type': 'float'},
        'au_hours_canceled': {'key': 'auHoursCanceled', 'type': 'float'},
        'au_hours_succeeded': {'key': 'auHoursSucceeded', 'type': 'float'},
        'last_submit_time': {'key': 'lastSubmitTime', 'type': 'iso-8601'},
        'runs': {'key': 'runs', 'type': '[JobPipelineRunInformation]'},
        'recurrences': {'key': 'recurrences', 'type': '[str]'},
    }

    def __init__(self, **kwargs):
        super(JobPipelineInformation, self).__init__(**kwargs)
        self.pipeline_id = None
        self.pipeline_name = None
        self.pipeline_uri = None
        self.num_jobs_failed = None
        self.num_jobs_canceled = None
        self.num_jobs_succeeded = None
        self.au_hours_failed = None
        self.au_hours_canceled = None
        self.au_hours_succeeded = None
        self.last_submit_time = None
        self.runs = None
        self.recurrences = None
