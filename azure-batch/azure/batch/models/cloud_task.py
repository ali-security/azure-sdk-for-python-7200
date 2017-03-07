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


class CloudTask(Model):
    """An Azure Batch task.

    :param id: A string that uniquely identifies the task within the job. The
     ID can contain any combination of alphanumeric characters including
     hyphens and underscores, and cannot contain more than 64 characters.
    :type id: str
    :param display_name: A display name for the task. The display name need
     not be unique and can contain any Unicode characters up to a maximum
     length of 1024.
    :type display_name: str
    :param url: The URL of the task.
    :type url: str
    :param e_tag: The ETag of the task. This is an opaque string. You can use
     it to detect whether the task has changed between requests. In particular,
     you can be pass the ETag when updating a task to specify that your changes
     should take effect only if nobody else has modified the task in the
     meantime.
    :type e_tag: str
    :param last_modified: The last modified time of the task.
    :type last_modified: datetime
    :param creation_time: The creation time of the task.
    :type creation_time: datetime
    :param exit_conditions: How the Batch service should respond when the task
     completes.
    :type exit_conditions: :class:`ExitConditions
     <azure.batch.models.ExitConditions>`
    :param state: The current state of the task. Possible values include:
     'active', 'preparing', 'running', 'completed'
    :type state: str or :class:`TaskState <azure.batch.models.TaskState>`
    :param state_transition_time: The time at which the task entered its
     current state.
    :type state_transition_time: datetime
    :param previous_state: The previous state of the task. This property is
     not set if the task is in its initial Active state. Possible values
     include: 'active', 'preparing', 'running', 'completed'
    :type previous_state: str or :class:`TaskState
     <azure.batch.models.TaskState>`
    :param previous_state_transition_time: The time at which the task entered
     its previous state. This property is not set if the task is in its initial
     Active state.
    :type previous_state_transition_time: datetime
    :param command_line: The command line of the task. For multi-instance
     tasks, the command line is executed as the primary task, after the primary
     task and all subtasks have finished executing the coordination command
     line. The command line does not run under a shell, and therefore cannot
     take advantage of shell features such as environment variable expansion.
     If you want to take advantage of such features, you should invoke the
     shell in the command line, for example using "cmd /c MyCommand" in Windows
     or "/bin/sh -c MyCommand" in Linux.
    :type command_line: str
    :param resource_files: A list of files that the Batch service will
     download to the compute node before running the command line. For
     multi-instance tasks, the resource files will only be downloaded to the
     compute node on which the primary task is executed.
    :type resource_files: list of :class:`ResourceFile
     <azure.batch.models.ResourceFile>`
    :param environment_settings: A list of environment variable settings for
     the task.
    :type environment_settings: list of :class:`EnvironmentSetting
     <azure.batch.models.EnvironmentSetting>`
    :param affinity_info: A locality hint that can be used by the Batch
     service to select a compute node on which to start the new task.
    :type affinity_info: :class:`AffinityInformation
     <azure.batch.models.AffinityInformation>`
    :param constraints: The execution constraints that apply to this task.
    :type constraints: :class:`TaskConstraints
     <azure.batch.models.TaskConstraints>`
    :param user_identity: The user identity under which the task runs. If
     omitted, the task runs as a non-administrative user unique to the task.
    :type user_identity: :class:`UserIdentity
     <azure.batch.models.UserIdentity>`
    :param execution_info: Information about the execution of the task.
    :type execution_info: :class:`TaskExecutionInformation
     <azure.batch.models.TaskExecutionInformation>`
    :param node_info: Information about the compute node on which the task
     ran.
    :type node_info: :class:`ComputeNodeInformation
     <azure.batch.models.ComputeNodeInformation>`
    :param multi_instance_settings: An object that indicates that the task is
     a multi-instance task, and contains information about how to run the
     multi-instance task.
    :type multi_instance_settings: :class:`MultiInstanceSettings
     <azure.batch.models.MultiInstanceSettings>`
    :param stats: Resource usage statistics for the task.
    :type stats: :class:`TaskStatistics <azure.batch.models.TaskStatistics>`
    :param depends_on: The tasks that this task depends on. This task will not
     be scheduled until all tasks that it depends on have completed
     successfully. If any of those tasks fail and exhaust their retry counts,
     this task will never be scheduled.
    :type depends_on: :class:`TaskDependencies
     <azure.batch.models.TaskDependencies>`
    :param application_package_references: A list of application packages that
     the Batch service will deploy to the compute node before running the
     command line.
    :type application_package_references: list of
     :class:`ApplicationPackageReference
     <azure.batch.models.ApplicationPackageReference>`
    :param authentication_token_settings: The settings for an authentication
     token that the task can use to perform Batch service operations. If this
     property is set, the Batch service provides the task with an
     authentication token which can be used to authenticate Batch service
     operations without requiring an account access key. The token is provided
     via the AZ_BATCH_AUTHENTICATION_TOKEN environment variable. The operations
     that the task can carry out using the token depend on the settings. For
     example, a task can request job permissions in order to add other tasks to
     the job, or check the status of the job or of other tasks under the job.
    :type authentication_token_settings: :class:`AuthenticationTokenSettings
     <azure.batch.models.AuthenticationTokenSettings>`
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'display_name': {'key': 'displayName', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'},
        'e_tag': {'key': 'eTag', 'type': 'str'},
        'last_modified': {'key': 'lastModified', 'type': 'iso-8601'},
        'creation_time': {'key': 'creationTime', 'type': 'iso-8601'},
        'exit_conditions': {'key': 'exitConditions', 'type': 'ExitConditions'},
        'state': {'key': 'state', 'type': 'TaskState'},
        'state_transition_time': {'key': 'stateTransitionTime', 'type': 'iso-8601'},
        'previous_state': {'key': 'previousState', 'type': 'TaskState'},
        'previous_state_transition_time': {'key': 'previousStateTransitionTime', 'type': 'iso-8601'},
        'command_line': {'key': 'commandLine', 'type': 'str'},
        'resource_files': {'key': 'resourceFiles', 'type': '[ResourceFile]'},
        'environment_settings': {'key': 'environmentSettings', 'type': '[EnvironmentSetting]'},
        'affinity_info': {'key': 'affinityInfo', 'type': 'AffinityInformation'},
        'constraints': {'key': 'constraints', 'type': 'TaskConstraints'},
        'user_identity': {'key': 'userIdentity', 'type': 'UserIdentity'},
        'execution_info': {'key': 'executionInfo', 'type': 'TaskExecutionInformation'},
        'node_info': {'key': 'nodeInfo', 'type': 'ComputeNodeInformation'},
        'multi_instance_settings': {'key': 'multiInstanceSettings', 'type': 'MultiInstanceSettings'},
        'stats': {'key': 'stats', 'type': 'TaskStatistics'},
        'depends_on': {'key': 'dependsOn', 'type': 'TaskDependencies'},
        'application_package_references': {'key': 'applicationPackageReferences', 'type': '[ApplicationPackageReference]'},
        'authentication_token_settings': {'key': 'authenticationTokenSettings', 'type': 'AuthenticationTokenSettings'},
    }

    def __init__(self, id=None, display_name=None, url=None, e_tag=None, last_modified=None, creation_time=None, exit_conditions=None, state=None, state_transition_time=None, previous_state=None, previous_state_transition_time=None, command_line=None, resource_files=None, environment_settings=None, affinity_info=None, constraints=None, user_identity=None, execution_info=None, node_info=None, multi_instance_settings=None, stats=None, depends_on=None, application_package_references=None, authentication_token_settings=None):
        self.id = id
        self.display_name = display_name
        self.url = url
        self.e_tag = e_tag
        self.last_modified = last_modified
        self.creation_time = creation_time
        self.exit_conditions = exit_conditions
        self.state = state
        self.state_transition_time = state_transition_time
        self.previous_state = previous_state
        self.previous_state_transition_time = previous_state_transition_time
        self.command_line = command_line
        self.resource_files = resource_files
        self.environment_settings = environment_settings
        self.affinity_info = affinity_info
        self.constraints = constraints
        self.user_identity = user_identity
        self.execution_info = execution_info
        self.node_info = node_info
        self.multi_instance_settings = multi_instance_settings
        self.stats = stats
        self.depends_on = depends_on
        self.application_package_references = application_package_references
        self.authentication_token_settings = authentication_token_settings
