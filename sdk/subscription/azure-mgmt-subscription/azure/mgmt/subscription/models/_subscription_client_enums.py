# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum
from six import with_metaclass
from azure.core import CaseInsensitiveEnumMeta


class AcceptOwnership(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The accept ownership state of the resource.
    """

    PENDING = "Pending"
    COMPLETED = "Completed"
    EXPIRED = "Expired"

class CreatedByType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The type of identity that created the resource.
    """

    USER = "User"
    APPLICATION = "Application"
    MANAGED_IDENTITY = "ManagedIdentity"
    KEY = "Key"

class ProvisioningState(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The provisioning state of the resource.
    """

    ACCEPTED = "Accepted"
    SUCCEEDED = "Succeeded"
    FAILED = "Failed"

class SpendingLimit(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The subscription spending limit.
    """

    ON = "On"
    OFF = "Off"
    CURRENT_PERIOD_OFF = "CurrentPeriodOff"

class SubscriptionState(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The subscription state. Possible values are Enabled, Warned, PastDue, Disabled, and Deleted.
    """

    ENABLED = "Enabled"
    WARNED = "Warned"
    PAST_DUE = "PastDue"
    DISABLED = "Disabled"
    DELETED = "Deleted"

class Workload(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The workload type of the subscription. It can be either Production or DevTest.
    """

    PRODUCTION = "Production"
    DEV_TEST = "DevTest"
