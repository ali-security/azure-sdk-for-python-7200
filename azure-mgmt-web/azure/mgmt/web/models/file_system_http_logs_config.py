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


class FileSystemHttpLogsConfig(Model):
    """Http logs to file system configuration.

    :param retention_in_mb: Maximum size in megabytes that http log files can
     use.
     When reached old log files will be removed to make space for new ones.
     Value can range between 25 and 100.
    :type retention_in_mb: int
    :param retention_in_days: Retention in days.
     Remove files older than X days.
     0 or lower means no retention.
    :type retention_in_days: int
    :param enabled: True if configuration is enabled, false if it is disabled
     and null if configuration is not set.
    :type enabled: bool
    """

    _validation = {
        'retention_in_mb': {'maximum': 100, 'minimum': 25},
    }

    _attribute_map = {
        'retention_in_mb': {'key': 'retentionInMb', 'type': 'int'},
        'retention_in_days': {'key': 'retentionInDays', 'type': 'int'},
        'enabled': {'key': 'enabled', 'type': 'bool'},
    }

    def __init__(self, retention_in_mb=None, retention_in_days=None, enabled=None):
        self.retention_in_mb = retention_in_mb
        self.retention_in_days = retention_in_days
        self.enabled = enabled
