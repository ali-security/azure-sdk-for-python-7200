# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum
from azure.core import CaseInsensitiveEnumMeta


class Action(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """A string property that indicates the action to be performed on the Flink job. It can have one
    of the following enum values => NEW, UPDATE, STATELESS_UPDATE, STOP, START, CANCEL, SAVEPOINT,
    LIST_SAVEPOINT, or DELETE.
    """

    NEW = "NEW"
    UPDATE = "UPDATE"
    STATELESS_UPDATE = "STATELESS_UPDATE"
    STOP = "STOP"
    START = "START"
    CANCEL = "CANCEL"
    SAVEPOINT = "SAVEPOINT"
    LIST_SAVEPOINT = "LIST_SAVEPOINT"
    DELETE = "DELETE"
    LAST_STATE_UPDATE = "LAST_STATE_UPDATE"
    RE_LAUNCH = "RE_LAUNCH"


class ActionType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Enum. Indicates the action type. "Internal" refers to actions that are for internal only APIs."""

    INTERNAL = "Internal"


class AutoscaleType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """User to specify which type of Autoscale to be implemented - Scheduled Based or Load Based."""

    SCHEDULE_BASED = "ScheduleBased"
    LOAD_BASED = "LoadBased"


class ClusterAvailableUpgradeType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Type of upgrade."""

    AKS_PATCH_UPGRADE = "AKSPatchUpgrade"
    HOTFIX_UPGRADE = "HotfixUpgrade"


class ClusterPoolAvailableUpgradeType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Type of upgrade."""

    AKS_PATCH_UPGRADE = "AKSPatchUpgrade"
    NODE_OS_UPGRADE = "NodeOsUpgrade"


class ClusterPoolUpgradeType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Type of upgrade."""

    AKS_PATCH_UPGRADE = "AKSPatchUpgrade"
    NODE_OS_UPGRADE = "NodeOsUpgrade"


class ClusterUpgradeType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Type of upgrade."""

    AKS_PATCH_UPGRADE = "AKSPatchUpgrade"
    HOTFIX_UPGRADE = "HotfixUpgrade"


class ComparisonOperator(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The comparison operator."""

    GREATER_THAN = "greaterThan"
    GREATER_THAN_OR_EQUAL = "greaterThanOrEqual"
    LESS_THAN = "lessThan"
    LESS_THAN_OR_EQUAL = "lessThanOrEqual"


class ContentEncoding(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """This property indicates if the content is encoded and is case-insensitive. Please set the value
    to base64 if the content is base64 encoded. Set it to none or skip it if the content is plain
    text.
    """

    BASE64 = "Base64"
    NONE = "None"


class CreatedByType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The type of identity that created the resource."""

    USER = "User"
    APPLICATION = "Application"
    MANAGED_IDENTITY = "ManagedIdentity"
    KEY = "Key"


class CurrentClusterAksVersionStatus(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Current AKS version's status: whether it is deprecated or supported."""

    DEPRECATED = "Deprecated"
    SUPPORTED = "Supported"


class CurrentClusterPoolAksVersionStatus(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Current AKS version's status: whether it is deprecated or supported."""

    DEPRECATED = "Deprecated"
    SUPPORTED = "Supported"


class DataDiskType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Managed Disk Type."""

    STANDARD_HDD_LRS = "Standard_HDD_LRS"
    STANDARD_SSD_LRS = "Standard_SSD_LRS"
    STANDARD_SSD_ZRS = "Standard_SSD_ZRS"
    PREMIUM_SSD_LRS = "Premium_SSD_LRS"
    PREMIUM_SSD_ZRS = "Premium_SSD_ZRS"
    PREMIUM_SSD_V2_LRS = "Premium_SSD_v2_LRS"


class DbConnectionAuthenticationMode(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The authentication mode to connect to your Hive metastore database. More details:
    https://learn.microsoft.com/en-us/azure/azure-sql/database/logins-create-manage?view=azuresql#authentication-and-authorization.
    """

    SQL_AUTH = "SqlAuth"
    """The password-based authentication to connect to your Hive metastore database."""
    IDENTITY_AUTH = "IdentityAuth"
    """The managed-identity-based authentication to connect to your Hive metastore database."""


class DeploymentMode(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """A string property that indicates the deployment mode of Flink cluster. It can have one of the
    following enum values => Application, Session. Default value is Session.
    """

    APPLICATION = "Application"
    SESSION = "Session"


class JobType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Type of cluster job."""

    FLINK_JOB = "FlinkJob"


class KeyVaultObjectType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Type of key vault object: secret, key or certificate."""

    KEY = "Key"
    SECRET = "Secret"
    CERTIFICATE = "Certificate"


class MetastoreDbConnectionAuthenticationMode(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The authentication mode to connect to your Hive metastore database. More details:
    https://learn.microsoft.com/en-us/azure/azure-sql/database/logins-create-manage?view=azuresql#authentication-and-authorization.
    """

    SQL_AUTH = "SqlAuth"
    """The password-based authentication to connect to your Hive metastore database."""
    IDENTITY_AUTH = "IdentityAuth"
    """The managed-identity-based authentication to connect to your Hive metastore database."""


class Origin(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The intended executor of the operation; as in Resource Based Access Control (RBAC) and audit
    logs UX. Default value is "user,system".
    """

    USER = "user"
    SYSTEM = "system"
    USER_SYSTEM = "user,system"


class OutboundType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """This can only be set at cluster pool creation time and cannot be changed later."""

    LOAD_BALANCER = "loadBalancer"
    """The load balancer is used for egress through an AKS assigned public IP. This supports
    Kubernetes services of type 'loadBalancer'."""
    USER_DEFINED_ROUTING = "userDefinedRouting"
    """Egress paths must be defined by the user. This is an advanced scenario and requires proper
    network configuration."""


class ProvisioningStatus(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Provisioning state of the resource."""

    ACCEPTED = "Accepted"
    SUCCEEDED = "Succeeded"
    CANCELED = "Canceled"
    FAILED = "Failed"


class RangerUsersyncMode(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """User & groups can be synced automatically or via a static list that's refreshed."""

    STATIC = "static"
    AUTOMATIC = "automatic"


class ScaleActionType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The action type."""

    SCALEUP = "scaleup"
    SCALEDOWN = "scaledown"


class ScheduleDay(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """ScheduleDay."""

    SUNDAY = "Sunday"
    MONDAY = "Monday"
    TUESDAY = "Tuesday"
    WEDNESDAY = "Wednesday"
    THURSDAY = "Thursday"
    FRIDAY = "Friday"
    SATURDAY = "Saturday"


class Severity(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Severity of this upgrade."""

    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"


class UpgradeMode(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """A string property that indicates the upgrade mode to be performed on the Flink job. It can have
    one of the following enum values => STATELESS_UPDATE, UPDATE, LAST_STATE_UPDATE.
    """

    STATELESS_UPDATE = "STATELESS_UPDATE"
    UPDATE = "UPDATE"
    LAST_STATE_UPDATE = "LAST_STATE_UPDATE"
