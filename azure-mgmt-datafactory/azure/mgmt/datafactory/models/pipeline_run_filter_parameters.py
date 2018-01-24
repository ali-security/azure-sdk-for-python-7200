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


class PipelineRunFilterParameters(Model):
    """Query parameters for listing pipeline runs.

    :param continuation_token: The continuation token for getting the next
     page of results. Null for first page.
    :type continuation_token: str
    :param last_updated_after: The time at or after which the pipeline run
     event was updated in 'ISO 8601' format.
    :type last_updated_after: datetime
    :param last_updated_before: The time at or before which the pipeline run
     event was updated in 'ISO 8601' format.
    :type last_updated_before: datetime
    :param filters: List of filters.
    :type filters: list[~azure.mgmt.datafactory.models.PipelineRunQueryFilter]
    :param order_by: List of OrderBy option.
    :type order_by:
     list[~azure.mgmt.datafactory.models.PipelineRunQueryOrderBy]
    """

    _validation = {
        'last_updated_after': {'required': True},
        'last_updated_before': {'required': True},
    }

    _attribute_map = {
        'continuation_token': {'key': 'continuationToken', 'type': 'str'},
        'last_updated_after': {'key': 'lastUpdatedAfter', 'type': 'iso-8601'},
        'last_updated_before': {'key': 'lastUpdatedBefore', 'type': 'iso-8601'},
        'filters': {'key': 'filters', 'type': '[PipelineRunQueryFilter]'},
        'order_by': {'key': 'orderBy', 'type': '[PipelineRunQueryOrderBy]'},
    }

    def __init__(self, last_updated_after, last_updated_before, continuation_token=None, filters=None, order_by=None):
        self.continuation_token = continuation_token
        self.last_updated_after = last_updated_after
        self.last_updated_before = last_updated_before
        self.filters = filters
        self.order_by = order_by
