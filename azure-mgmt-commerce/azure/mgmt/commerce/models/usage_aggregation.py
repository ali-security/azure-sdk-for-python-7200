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


class UsageAggregation(Model):
    """
    Describes the usageAggregation.

    :param id: Unique Id for the usage aggregate.
    :type id: str
    :param name: Name of the usage aggregate.
    :type name: str
    :param type: Type of the resource being returned.
    :type type: str
    :param subscription_id: The subscription identifier for the Azure user.
    :type subscription_id: str
    :param meter_id: Unique ID for the resource that was consumed (aka
     ResourceID).
    :type meter_id: str
    :param usage_start_time: UTC start time for the usage bucket to which
     this usage aggregate belongs.
    :type usage_start_time: datetime
    :param usage_end_time: UTC end time for the usage bucket to which this
     usage aggregate belongs.
    :type usage_end_time: datetime
    :param quantity: The amount of the resource consumption that occurred in
     this time frame.
    :type quantity: object
    :param unit: The unit in which the usage for this resource is being
     counted, e.g. Hours, GB.
    :type unit: str
    :param meter_name: Friendly name of the resource being consumed.
    :type meter_name: str
    :param meter_category: Category of the consumed resource.
    :type meter_category: str
    :param meter_sub_category: Sub-category of the consumed resource.
    :type meter_sub_category: str
    :param meter_region: Region of the meterId used for billing purposes
    :type meter_region: str
    :param info_fields: Key-value pairs of instance details (legacy format).
    :type info_fields: :class:`InfoField
     <azure.mgmt.commerce.models.InfoField>`
    :param instance_data: Key-value pairs of instance details represented as
     a string.
    :type instance_data: str
    """ 

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'subscription_id': {'key': 'properties.subscriptionId', 'type': 'str'},
        'meter_id': {'key': 'properties.meterId', 'type': 'str'},
        'usage_start_time': {'key': 'properties.usageStartTime', 'type': 'iso-8601'},
        'usage_end_time': {'key': 'properties.usageEndTime', 'type': 'iso-8601'},
        'quantity': {'key': 'properties.quantity', 'type': 'object'},
        'unit': {'key': 'properties.unit', 'type': 'str'},
        'meter_name': {'key': 'properties.meterName', 'type': 'str'},
        'meter_category': {'key': 'properties.meterCategory', 'type': 'str'},
        'meter_sub_category': {'key': 'properties.meterSubCategory', 'type': 'str'},
        'meter_region': {'key': 'properties.meterRegion', 'type': 'str'},
        'info_fields': {'key': 'properties.infoFields', 'type': 'InfoField'},
        'instance_data': {'key': 'properties.instanceData', 'type': 'str'},
    }

    def __init__(self, id=None, name=None, type=None, subscription_id=None, meter_id=None, usage_start_time=None, usage_end_time=None, quantity=None, unit=None, meter_name=None, meter_category=None, meter_sub_category=None, meter_region=None, info_fields=None, instance_data=None):
        self.id = id
        self.name = name
        self.type = type
        self.subscription_id = subscription_id
        self.meter_id = meter_id
        self.usage_start_time = usage_start_time
        self.usage_end_time = usage_end_time
        self.quantity = quantity
        self.unit = unit
        self.meter_name = meter_name
        self.meter_category = meter_category
        self.meter_sub_category = meter_sub_category
        self.meter_region = meter_region
        self.info_fields = info_fields
        self.instance_data = instance_data
