# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from ._models_py3 import AdministratorListResult
from ._models_py3 import Advisor
from ._models_py3 import AutoPauseDelayTimeRange
from ._models_py3 import AutomaticTuningOptions
from ._models_py3 import AutomaticTuningServerOptions
from ._models_py3 import AzureADOnlyAuthListResult
from ._models_py3 import BackupShortTermRetentionPolicy
from ._models_py3 import BackupShortTermRetentionPolicyListResult
from ._models_py3 import CheckNameAvailabilityRequest
from ._models_py3 import CheckNameAvailabilityResponse
from ._models_py3 import CompleteDatabaseRestoreDefinition
from ._models_py3 import CopyLongTermRetentionBackupParameters
from ._models_py3 import CreateDatabaseRestorePointDefinition
from ._models_py3 import DataMaskingPolicy
from ._models_py3 import DataMaskingRule
from ._models_py3 import DataMaskingRuleListResult
from ._models_py3 import DataWarehouseUserActivities
from ._models_py3 import DataWarehouseUserActivitiesListResult
from ._models_py3 import Database
from ._models_py3 import DatabaseAdvancedThreatProtection
from ._models_py3 import DatabaseAdvancedThreatProtectionListResult
from ._models_py3 import DatabaseAutomaticTuning
from ._models_py3 import DatabaseBlobAuditingPolicy
from ._models_py3 import DatabaseBlobAuditingPolicyListResult
from ._models_py3 import DatabaseColumn
from ._models_py3 import DatabaseColumnListResult
from ._models_py3 import DatabaseExtensions
from ._models_py3 import DatabaseIdentity
from ._models_py3 import DatabaseListResult
from ._models_py3 import DatabaseOperation
from ._models_py3 import DatabaseOperationListResult
from ._models_py3 import DatabaseSchema
from ._models_py3 import DatabaseSchemaListResult
from ._models_py3 import DatabaseSecurityAlertListResult
from ._models_py3 import DatabaseSecurityAlertPolicy
from ._models_py3 import DatabaseTable
from ._models_py3 import DatabaseTableListResult
from ._models_py3 import DatabaseUpdate
from ._models_py3 import DatabaseUsage
from ._models_py3 import DatabaseUsageListResult
from ._models_py3 import DatabaseUserIdentity
from ._models_py3 import DatabaseVulnerabilityAssessment
from ._models_py3 import DatabaseVulnerabilityAssessmentListResult
from ._models_py3 import DatabaseVulnerabilityAssessmentRuleBaseline
from ._models_py3 import DatabaseVulnerabilityAssessmentRuleBaselineItem
from ._models_py3 import DatabaseVulnerabilityAssessmentScansExport
from ._models_py3 import DeletedServer
from ._models_py3 import DeletedServerListResult
from ._models_py3 import DistributedAvailabilityGroup
from ._models_py3 import DistributedAvailabilityGroupsListResult
from ._models_py3 import EditionCapability
from ._models_py3 import ElasticPool
from ._models_py3 import ElasticPoolActivity
from ._models_py3 import ElasticPoolActivityListResult
from ._models_py3 import ElasticPoolDatabaseActivity
from ._models_py3 import ElasticPoolDatabaseActivityListResult
from ._models_py3 import ElasticPoolEditionCapability
from ._models_py3 import ElasticPoolListResult
from ._models_py3 import ElasticPoolOperation
from ._models_py3 import ElasticPoolOperationListResult
from ._models_py3 import ElasticPoolPerDatabaseMaxPerformanceLevelCapability
from ._models_py3 import ElasticPoolPerDatabaseMinPerformanceLevelCapability
from ._models_py3 import ElasticPoolPerDatabaseSettings
from ._models_py3 import ElasticPoolPerformanceLevelCapability
from ._models_py3 import ElasticPoolUpdate
from ._models_py3 import EncryptionProtector
from ._models_py3 import EncryptionProtectorListResult
from ._models_py3 import EndpointCertificate
from ._models_py3 import EndpointCertificateListResult
from ._models_py3 import ExportDatabaseDefinition
from ._models_py3 import ExtendedDatabaseBlobAuditingPolicy
from ._models_py3 import ExtendedDatabaseBlobAuditingPolicyListResult
from ._models_py3 import ExtendedServerBlobAuditingPolicy
from ._models_py3 import ExtendedServerBlobAuditingPolicyListResult
from ._models_py3 import FailoverGroup
from ._models_py3 import FailoverGroupListResult
from ._models_py3 import FailoverGroupReadOnlyEndpoint
from ._models_py3 import FailoverGroupReadWriteEndpoint
from ._models_py3 import FailoverGroupUpdate
from ._models_py3 import FirewallRule
from ._models_py3 import FirewallRuleList
from ._models_py3 import FirewallRuleListResult
from ._models_py3 import GeoBackupPolicy
from ._models_py3 import GeoBackupPolicyListResult
from ._models_py3 import IPv6FirewallRule
from ._models_py3 import IPv6FirewallRuleListResult
from ._models_py3 import ImportExistingDatabaseDefinition
from ._models_py3 import ImportExportExtensionsOperationListResult
from ._models_py3 import ImportExportExtensionsOperationResult
from ._models_py3 import ImportExportOperationResult
from ._models_py3 import ImportNewDatabaseDefinition
from ._models_py3 import InstanceFailoverGroup
from ._models_py3 import InstanceFailoverGroupListResult
from ._models_py3 import InstanceFailoverGroupReadOnlyEndpoint
from ._models_py3 import InstanceFailoverGroupReadWriteEndpoint
from ._models_py3 import InstancePool
from ._models_py3 import InstancePoolEditionCapability
from ._models_py3 import InstancePoolFamilyCapability
from ._models_py3 import InstancePoolListResult
from ._models_py3 import InstancePoolUpdate
from ._models_py3 import InstancePoolVcoresCapability
from ._models_py3 import Job
from ._models_py3 import JobAgent
from ._models_py3 import JobAgentListResult
from ._models_py3 import JobAgentUpdate
from ._models_py3 import JobCredential
from ._models_py3 import JobCredentialListResult
from ._models_py3 import JobExecution
from ._models_py3 import JobExecutionListResult
from ._models_py3 import JobExecutionTarget
from ._models_py3 import JobListResult
from ._models_py3 import JobSchedule
from ._models_py3 import JobStep
from ._models_py3 import JobStepAction
from ._models_py3 import JobStepExecutionOptions
from ._models_py3 import JobStepListResult
from ._models_py3 import JobStepOutput
from ._models_py3 import JobTarget
from ._models_py3 import JobTargetGroup
from ._models_py3 import JobTargetGroupListResult
from ._models_py3 import JobVersion
from ._models_py3 import JobVersionListResult
from ._models_py3 import LedgerDigestUploads
from ._models_py3 import LedgerDigestUploadsListResult
from ._models_py3 import LicenseTypeCapability
from ._models_py3 import LocationCapabilities
from ._models_py3 import LogSizeCapability
from ._models_py3 import LogicalDatabaseTransparentDataEncryption
from ._models_py3 import LogicalDatabaseTransparentDataEncryptionListResult
from ._models_py3 import LogicalServerAdvancedThreatProtectionListResult
from ._models_py3 import LogicalServerSecurityAlertPolicyListResult
from ._models_py3 import LongTermRetentionBackup
from ._models_py3 import LongTermRetentionBackupListResult
from ._models_py3 import LongTermRetentionBackupOperationResult
from ._models_py3 import LongTermRetentionPolicy
from ._models_py3 import LongTermRetentionPolicyListResult
from ._models_py3 import MaintenanceConfigurationCapability
from ._models_py3 import MaintenanceWindowOptions
from ._models_py3 import MaintenanceWindowTimeRange
from ._models_py3 import MaintenanceWindows
from ._models_py3 import ManagedBackupShortTermRetentionPolicy
from ._models_py3 import ManagedBackupShortTermRetentionPolicyListResult
from ._models_py3 import ManagedDatabase
from ._models_py3 import ManagedDatabaseListResult
from ._models_py3 import ManagedDatabaseRestoreDetailsResult
from ._models_py3 import ManagedDatabaseSecurityAlertPolicy
from ._models_py3 import ManagedDatabaseSecurityAlertPolicyListResult
from ._models_py3 import ManagedDatabaseUpdate
from ._models_py3 import ManagedInstance
from ._models_py3 import ManagedInstanceAdministrator
from ._models_py3 import ManagedInstanceAdministratorListResult
from ._models_py3 import ManagedInstanceAzureADOnlyAuthListResult
from ._models_py3 import ManagedInstanceAzureADOnlyAuthentication
from ._models_py3 import ManagedInstanceEditionCapability
from ._models_py3 import ManagedInstanceEncryptionProtector
from ._models_py3 import ManagedInstanceEncryptionProtectorListResult
from ._models_py3 import ManagedInstanceExternalAdministrator
from ._models_py3 import ManagedInstanceFamilyCapability
from ._models_py3 import ManagedInstanceKey
from ._models_py3 import ManagedInstanceKeyListResult
from ._models_py3 import ManagedInstanceListResult
from ._models_py3 import ManagedInstanceLongTermRetentionBackup
from ._models_py3 import ManagedInstanceLongTermRetentionBackupListResult
from ._models_py3 import ManagedInstanceLongTermRetentionPolicy
from ._models_py3 import ManagedInstanceLongTermRetentionPolicyListResult
from ._models_py3 import ManagedInstanceMaintenanceConfigurationCapability
from ._models_py3 import ManagedInstanceOperation
from ._models_py3 import ManagedInstanceOperationListResult
from ._models_py3 import ManagedInstanceOperationParametersPair
from ._models_py3 import ManagedInstanceOperationSteps
from ._models_py3 import ManagedInstancePairInfo
from ._models_py3 import ManagedInstancePecProperty
from ._models_py3 import ManagedInstancePrivateEndpointConnection
from ._models_py3 import ManagedInstancePrivateEndpointConnectionListResult
from ._models_py3 import ManagedInstancePrivateEndpointConnectionProperties
from ._models_py3 import ManagedInstancePrivateEndpointProperty
from ._models_py3 import ManagedInstancePrivateLink
from ._models_py3 import ManagedInstancePrivateLinkListResult
from ._models_py3 import ManagedInstancePrivateLinkProperties
from ._models_py3 import ManagedInstancePrivateLinkServiceConnectionStateProperty
from ._models_py3 import ManagedInstanceQuery
from ._models_py3 import ManagedInstanceQueryStatistics
from ._models_py3 import ManagedInstanceUpdate
from ._models_py3 import ManagedInstanceVcoresCapability
from ._models_py3 import ManagedInstanceVersionCapability
from ._models_py3 import ManagedInstanceVulnerabilityAssessment
from ._models_py3 import ManagedInstanceVulnerabilityAssessmentListResult
from ._models_py3 import ManagedServerDnsAlias
from ._models_py3 import ManagedServerDnsAliasAcquisition
from ._models_py3 import ManagedServerDnsAliasCreation
from ._models_py3 import ManagedServerDnsAliasListResult
from ._models_py3 import ManagedServerSecurityAlertPolicy
from ._models_py3 import ManagedServerSecurityAlertPolicyListResult
from ._models_py3 import ManagedTransparentDataEncryption
from ._models_py3 import ManagedTransparentDataEncryptionListResult
from ._models_py3 import MaxSizeCapability
from ._models_py3 import MaxSizeRangeCapability
from ._models_py3 import Metric
from ._models_py3 import MetricAvailability
from ._models_py3 import MetricDefinition
from ._models_py3 import MetricDefinitionListResult
from ._models_py3 import MetricListResult
from ._models_py3 import MetricName
from ._models_py3 import MetricValue
from ._models_py3 import MinCapacityCapability
from ._models_py3 import Name
from ._models_py3 import NetworkIsolationSettings
from ._models_py3 import Operation
from ._models_py3 import OperationDisplay
from ._models_py3 import OperationImpact
from ._models_py3 import OperationListResult
from ._models_py3 import OutboundFirewallRule
from ._models_py3 import OutboundFirewallRuleListResult
from ._models_py3 import PartnerInfo
from ._models_py3 import PartnerRegionInfo
from ._models_py3 import PerformanceLevelCapability
from ._models_py3 import PrivateEndpointConnection
from ._models_py3 import PrivateEndpointConnectionListResult
from ._models_py3 import PrivateEndpointConnectionProperties
from ._models_py3 import PrivateEndpointConnectionRequestStatus
from ._models_py3 import PrivateEndpointProperty
from ._models_py3 import PrivateLinkResource
from ._models_py3 import PrivateLinkResourceListResult
from ._models_py3 import PrivateLinkResourceProperties
from ._models_py3 import PrivateLinkServiceConnectionStateProperty
from ._models_py3 import ProxyResource
from ._models_py3 import ProxyResourceWithWritableName
from ._models_py3 import QueryMetricInterval
from ._models_py3 import QueryMetricProperties
from ._models_py3 import QueryStatistics
from ._models_py3 import QueryStatisticsProperties
from ._models_py3 import ReadScaleCapability
from ._models_py3 import RecommendedAction
from ._models_py3 import RecommendedActionErrorInfo
from ._models_py3 import RecommendedActionImpactRecord
from ._models_py3 import RecommendedActionImplementationInfo
from ._models_py3 import RecommendedActionMetricInfo
from ._models_py3 import RecommendedActionStateInfo
from ._models_py3 import RecommendedSensitivityLabelUpdate
from ._models_py3 import RecommendedSensitivityLabelUpdateList
from ._models_py3 import RecoverableDatabase
from ._models_py3 import RecoverableDatabaseListResult
from ._models_py3 import RecoverableManagedDatabase
from ._models_py3 import RecoverableManagedDatabaseListResult
from ._models_py3 import ReplicationLink
from ._models_py3 import ReplicationLinkListResult
from ._models_py3 import Resource
from ._models_py3 import ResourceIdentity
from ._models_py3 import ResourceMoveDefinition
from ._models_py3 import ResourceWithWritableName
from ._models_py3 import RestorableDroppedDatabase
from ._models_py3 import RestorableDroppedDatabaseListResult
from ._models_py3 import RestorableDroppedManagedDatabase
from ._models_py3 import RestorableDroppedManagedDatabaseListResult
from ._models_py3 import RestorePoint
from ._models_py3 import RestorePointListResult
from ._models_py3 import SecurityEvent
from ._models_py3 import SecurityEventCollection
from ._models_py3 import SecurityEventSqlInjectionAdditionalProperties
from ._models_py3 import SecurityEventsFilterParameters
from ._models_py3 import SensitivityLabel
from ._models_py3 import SensitivityLabelListResult
from ._models_py3 import SensitivityLabelUpdate
from ._models_py3 import SensitivityLabelUpdateList
from ._models_py3 import Server
from ._models_py3 import ServerAdvancedThreatProtection
from ._models_py3 import ServerAutomaticTuning
from ._models_py3 import ServerAzureADAdministrator
from ._models_py3 import ServerAzureADOnlyAuthentication
from ._models_py3 import ServerBlobAuditingPolicy
from ._models_py3 import ServerBlobAuditingPolicyListResult
from ._models_py3 import ServerCommunicationLink
from ._models_py3 import ServerCommunicationLinkListResult
from ._models_py3 import ServerConnectionPolicy
from ._models_py3 import ServerConnectionPolicyListResult
from ._models_py3 import ServerDevOpsAuditSettingsListResult
from ._models_py3 import ServerDevOpsAuditingSettings
from ._models_py3 import ServerDnsAlias
from ._models_py3 import ServerDnsAliasAcquisition
from ._models_py3 import ServerDnsAliasListResult
from ._models_py3 import ServerExternalAdministrator
from ._models_py3 import ServerInfo
from ._models_py3 import ServerKey
from ._models_py3 import ServerKeyListResult
from ._models_py3 import ServerListResult
from ._models_py3 import ServerOperation
from ._models_py3 import ServerOperationListResult
from ._models_py3 import ServerPrivateEndpointConnection
from ._models_py3 import ServerSecurityAlertPolicy
from ._models_py3 import ServerTrustCertificate
from ._models_py3 import ServerTrustCertificatesListResult
from ._models_py3 import ServerTrustGroup
from ._models_py3 import ServerTrustGroupListResult
from ._models_py3 import ServerUpdate
from ._models_py3 import ServerUsage
from ._models_py3 import ServerUsageListResult
from ._models_py3 import ServerVersionCapability
from ._models_py3 import ServerVulnerabilityAssessment
from ._models_py3 import ServerVulnerabilityAssessmentListResult
from ._models_py3 import ServiceObjective
from ._models_py3 import ServiceObjectiveCapability
from ._models_py3 import ServiceObjectiveListResult
from ._models_py3 import ServicePrincipal
from ._models_py3 import Sku
from ._models_py3 import SloUsageMetric
from ._models_py3 import SqlAgentConfiguration
from ._models_py3 import StorageCapability
from ._models_py3 import SubscriptionUsage
from ._models_py3 import SubscriptionUsageListResult
from ._models_py3 import SyncAgent
from ._models_py3 import SyncAgentKeyProperties
from ._models_py3 import SyncAgentLinkedDatabase
from ._models_py3 import SyncAgentLinkedDatabaseListResult
from ._models_py3 import SyncAgentListResult
from ._models_py3 import SyncDatabaseIdListResult
from ._models_py3 import SyncDatabaseIdProperties
from ._models_py3 import SyncFullSchemaProperties
from ._models_py3 import SyncFullSchemaPropertiesListResult
from ._models_py3 import SyncFullSchemaTable
from ._models_py3 import SyncFullSchemaTableColumn
from ._models_py3 import SyncGroup
from ._models_py3 import SyncGroupListResult
from ._models_py3 import SyncGroupLogListResult
from ._models_py3 import SyncGroupLogProperties
from ._models_py3 import SyncGroupSchema
from ._models_py3 import SyncGroupSchemaTable
from ._models_py3 import SyncGroupSchemaTableColumn
from ._models_py3 import SyncMember
from ._models_py3 import SyncMemberListResult
from ._models_py3 import SystemData
from ._models_py3 import TdeCertificate
from ._models_py3 import TimeZone
from ._models_py3 import TimeZoneListResult
from ._models_py3 import TopQueries
from ._models_py3 import TopQueriesListResult
from ._models_py3 import TrackedResource
from ._models_py3 import UpdateLongTermRetentionBackupParameters
from ._models_py3 import UpdateManagedInstanceDnsServersOperation
from ._models_py3 import UpsertManagedServerOperationParameters
from ._models_py3 import UpsertManagedServerOperationStep
from ._models_py3 import Usage
from ._models_py3 import UsageListResult
from ._models_py3 import UserIdentity
from ._models_py3 import VirtualCluster
from ._models_py3 import VirtualClusterListResult
from ._models_py3 import VirtualClusterUpdate
from ._models_py3 import VirtualNetworkRule
from ._models_py3 import VirtualNetworkRuleListResult
from ._models_py3 import VulnerabilityAssessmentRecurringScansProperties
from ._models_py3 import VulnerabilityAssessmentScanError
from ._models_py3 import VulnerabilityAssessmentScanRecord
from ._models_py3 import VulnerabilityAssessmentScanRecordListResult
from ._models_py3 import WorkloadClassifier
from ._models_py3 import WorkloadClassifierListResult
from ._models_py3 import WorkloadGroup
from ._models_py3 import WorkloadGroupListResult


from ._sql_management_client_enums import (
    AdministratorName,
    AdministratorType,
    AdvancedThreatProtectionName,
    AdvancedThreatProtectionState,
    AdvisorStatus,
    AggregationFunctionType,
    AuthenticationName,
    AutoExecuteStatus,
    AutoExecuteStatusInheritedFrom,
    AutomaticTuningDisabledReason,
    AutomaticTuningMode,
    AutomaticTuningOptionModeActual,
    AutomaticTuningOptionModeDesired,
    AutomaticTuningServerMode,
    AutomaticTuningServerReason,
    BackupStorageRedundancy,
    BlobAuditingPolicyState,
    CapabilityGroup,
    CapabilityStatus,
    CatalogCollationType,
    CheckNameAvailabilityReason,
    ColumnDataType,
    ConnectionPolicyName,
    CreateMode,
    CreatedByType,
    DataMaskingFunction,
    DataMaskingRuleState,
    DataMaskingState,
    DataWarehouseUserActivityName,
    DatabaseIdentityType,
    DatabaseLicenseType,
    DatabaseReadScale,
    DatabaseState,
    DatabaseStatus,
    DayOfWeek,
    DiffBackupIntervalInHours,
    DnsRefreshConfigurationPropertiesStatus,
    ElasticPoolLicenseType,
    ElasticPoolState,
    EncryptionProtectorName,
    FailoverGroupReplicationRole,
    GeoBackupPolicyName,
    GeoBackupPolicyState,
    IdentityType,
    ImplementationMethod,
    InstanceFailoverGroupReplicationRole,
    InstancePoolLicenseType,
    IsRetryable,
    JobAgentState,
    JobExecutionLifecycle,
    JobScheduleType,
    JobStepActionSource,
    JobStepActionType,
    JobStepOutputType,
    JobTargetGroupMembershipType,
    JobTargetType,
    LedgerDigestUploadsName,
    LedgerDigestUploadsState,
    LogSizeUnit,
    LongTermRetentionPolicyName,
    ManagedDatabaseCreateMode,
    ManagedDatabaseStatus,
    ManagedInstanceAdministratorType,
    ManagedInstanceLicenseType,
    ManagedInstanceLongTermRetentionPolicyName,
    ManagedInstancePropertiesProvisioningState,
    ManagedInstanceProxyOverride,
    ManagedServerCreateMode,
    ManagedShortTermRetentionPolicyName,
    ManagementOperationState,
    MaxSizeUnit,
    MetricType,
    OperationMode,
    OperationOrigin,
    PauseDelayTimeUnit,
    PerformanceLevelUnit,
    PrimaryAggregationType,
    PrincipalType,
    PrivateEndpointProvisioningState,
    PrivateLinkServiceConnectionStateActionsRequire,
    PrivateLinkServiceConnectionStateStatus,
    ProvisioningState,
    QueryMetricUnitType,
    QueryTimeGrainType,
    ReadOnlyEndpointFailoverPolicy,
    ReadWriteEndpointFailoverPolicy,
    RecommendedActionCurrentState,
    RecommendedActionInitiatedBy,
    RecommendedSensitivityLabelUpdateKind,
    ReplicaType,
    ReplicationLinkType,
    ReplicationMode,
    ReplicationRole,
    ReplicationState,
    RestoreDetailsName,
    RestorePointType,
    SampleName,
    SecondaryType,
    SecurityAlertPolicyName,
    SecurityAlertPolicyState,
    SecurityAlertsPolicyState,
    SecurityEventType,
    SensitivityLabelRank,
    SensitivityLabelSource,
    SensitivityLabelUpdateKind,
    ServerConnectionType,
    ServerKeyType,
    ServerNetworkAccessFlag,
    ServerTrustGroupPropertiesTrustScopesItem,
    ServerWorkspaceFeature,
    ServiceObjectiveName,
    ServicePrincipalType,
    ShortTermRetentionPolicyName,
    SqlAgentConfigurationPropertiesState,
    StorageCapabilityStorageAccountType,
    StorageKeyType,
    SyncAgentState,
    SyncConflictResolutionPolicy,
    SyncDirection,
    SyncGroupLogType,
    SyncGroupState,
    SyncGroupsType,
    SyncMemberDbType,
    SyncMemberState,
    TableTemporalType,
    TransparentDataEncryptionName,
    TransparentDataEncryptionState,
    UnitDefinitionType,
    UnitType,
    UpsertManagedServerOperationStepStatus,
    VirtualNetworkRuleState,
    VulnerabilityAssessmentName,
    VulnerabilityAssessmentPolicyBaselineName,
    VulnerabilityAssessmentScanState,
    VulnerabilityAssessmentScanTriggerType,
)
from ._patch import __all__ as _patch_all
from ._patch import *  # type: ignore # pylint: disable=unused-wildcard-import
from ._patch import patch_sdk as _patch_sdk
__all__ = [
    'AdministratorListResult',
    'Advisor',
    'AutoPauseDelayTimeRange',
    'AutomaticTuningOptions',
    'AutomaticTuningServerOptions',
    'AzureADOnlyAuthListResult',
    'BackupShortTermRetentionPolicy',
    'BackupShortTermRetentionPolicyListResult',
    'CheckNameAvailabilityRequest',
    'CheckNameAvailabilityResponse',
    'CompleteDatabaseRestoreDefinition',
    'CopyLongTermRetentionBackupParameters',
    'CreateDatabaseRestorePointDefinition',
    'DataMaskingPolicy',
    'DataMaskingRule',
    'DataMaskingRuleListResult',
    'DataWarehouseUserActivities',
    'DataWarehouseUserActivitiesListResult',
    'Database',
    'DatabaseAdvancedThreatProtection',
    'DatabaseAdvancedThreatProtectionListResult',
    'DatabaseAutomaticTuning',
    'DatabaseBlobAuditingPolicy',
    'DatabaseBlobAuditingPolicyListResult',
    'DatabaseColumn',
    'DatabaseColumnListResult',
    'DatabaseExtensions',
    'DatabaseIdentity',
    'DatabaseListResult',
    'DatabaseOperation',
    'DatabaseOperationListResult',
    'DatabaseSchema',
    'DatabaseSchemaListResult',
    'DatabaseSecurityAlertListResult',
    'DatabaseSecurityAlertPolicy',
    'DatabaseTable',
    'DatabaseTableListResult',
    'DatabaseUpdate',
    'DatabaseUsage',
    'DatabaseUsageListResult',
    'DatabaseUserIdentity',
    'DatabaseVulnerabilityAssessment',
    'DatabaseVulnerabilityAssessmentListResult',
    'DatabaseVulnerabilityAssessmentRuleBaseline',
    'DatabaseVulnerabilityAssessmentRuleBaselineItem',
    'DatabaseVulnerabilityAssessmentScansExport',
    'DeletedServer',
    'DeletedServerListResult',
    'DistributedAvailabilityGroup',
    'DistributedAvailabilityGroupsListResult',
    'EditionCapability',
    'ElasticPool',
    'ElasticPoolActivity',
    'ElasticPoolActivityListResult',
    'ElasticPoolDatabaseActivity',
    'ElasticPoolDatabaseActivityListResult',
    'ElasticPoolEditionCapability',
    'ElasticPoolListResult',
    'ElasticPoolOperation',
    'ElasticPoolOperationListResult',
    'ElasticPoolPerDatabaseMaxPerformanceLevelCapability',
    'ElasticPoolPerDatabaseMinPerformanceLevelCapability',
    'ElasticPoolPerDatabaseSettings',
    'ElasticPoolPerformanceLevelCapability',
    'ElasticPoolUpdate',
    'EncryptionProtector',
    'EncryptionProtectorListResult',
    'EndpointCertificate',
    'EndpointCertificateListResult',
    'ExportDatabaseDefinition',
    'ExtendedDatabaseBlobAuditingPolicy',
    'ExtendedDatabaseBlobAuditingPolicyListResult',
    'ExtendedServerBlobAuditingPolicy',
    'ExtendedServerBlobAuditingPolicyListResult',
    'FailoverGroup',
    'FailoverGroupListResult',
    'FailoverGroupReadOnlyEndpoint',
    'FailoverGroupReadWriteEndpoint',
    'FailoverGroupUpdate',
    'FirewallRule',
    'FirewallRuleList',
    'FirewallRuleListResult',
    'GeoBackupPolicy',
    'GeoBackupPolicyListResult',
    'IPv6FirewallRule',
    'IPv6FirewallRuleListResult',
    'ImportExistingDatabaseDefinition',
    'ImportExportExtensionsOperationListResult',
    'ImportExportExtensionsOperationResult',
    'ImportExportOperationResult',
    'ImportNewDatabaseDefinition',
    'InstanceFailoverGroup',
    'InstanceFailoverGroupListResult',
    'InstanceFailoverGroupReadOnlyEndpoint',
    'InstanceFailoverGroupReadWriteEndpoint',
    'InstancePool',
    'InstancePoolEditionCapability',
    'InstancePoolFamilyCapability',
    'InstancePoolListResult',
    'InstancePoolUpdate',
    'InstancePoolVcoresCapability',
    'Job',
    'JobAgent',
    'JobAgentListResult',
    'JobAgentUpdate',
    'JobCredential',
    'JobCredentialListResult',
    'JobExecution',
    'JobExecutionListResult',
    'JobExecutionTarget',
    'JobListResult',
    'JobSchedule',
    'JobStep',
    'JobStepAction',
    'JobStepExecutionOptions',
    'JobStepListResult',
    'JobStepOutput',
    'JobTarget',
    'JobTargetGroup',
    'JobTargetGroupListResult',
    'JobVersion',
    'JobVersionListResult',
    'LedgerDigestUploads',
    'LedgerDigestUploadsListResult',
    'LicenseTypeCapability',
    'LocationCapabilities',
    'LogSizeCapability',
    'LogicalDatabaseTransparentDataEncryption',
    'LogicalDatabaseTransparentDataEncryptionListResult',
    'LogicalServerAdvancedThreatProtectionListResult',
    'LogicalServerSecurityAlertPolicyListResult',
    'LongTermRetentionBackup',
    'LongTermRetentionBackupListResult',
    'LongTermRetentionBackupOperationResult',
    'LongTermRetentionPolicy',
    'LongTermRetentionPolicyListResult',
    'MaintenanceConfigurationCapability',
    'MaintenanceWindowOptions',
    'MaintenanceWindowTimeRange',
    'MaintenanceWindows',
    'ManagedBackupShortTermRetentionPolicy',
    'ManagedBackupShortTermRetentionPolicyListResult',
    'ManagedDatabase',
    'ManagedDatabaseListResult',
    'ManagedDatabaseRestoreDetailsResult',
    'ManagedDatabaseSecurityAlertPolicy',
    'ManagedDatabaseSecurityAlertPolicyListResult',
    'ManagedDatabaseUpdate',
    'ManagedInstance',
    'ManagedInstanceAdministrator',
    'ManagedInstanceAdministratorListResult',
    'ManagedInstanceAzureADOnlyAuthListResult',
    'ManagedInstanceAzureADOnlyAuthentication',
    'ManagedInstanceEditionCapability',
    'ManagedInstanceEncryptionProtector',
    'ManagedInstanceEncryptionProtectorListResult',
    'ManagedInstanceExternalAdministrator',
    'ManagedInstanceFamilyCapability',
    'ManagedInstanceKey',
    'ManagedInstanceKeyListResult',
    'ManagedInstanceListResult',
    'ManagedInstanceLongTermRetentionBackup',
    'ManagedInstanceLongTermRetentionBackupListResult',
    'ManagedInstanceLongTermRetentionPolicy',
    'ManagedInstanceLongTermRetentionPolicyListResult',
    'ManagedInstanceMaintenanceConfigurationCapability',
    'ManagedInstanceOperation',
    'ManagedInstanceOperationListResult',
    'ManagedInstanceOperationParametersPair',
    'ManagedInstanceOperationSteps',
    'ManagedInstancePairInfo',
    'ManagedInstancePecProperty',
    'ManagedInstancePrivateEndpointConnection',
    'ManagedInstancePrivateEndpointConnectionListResult',
    'ManagedInstancePrivateEndpointConnectionProperties',
    'ManagedInstancePrivateEndpointProperty',
    'ManagedInstancePrivateLink',
    'ManagedInstancePrivateLinkListResult',
    'ManagedInstancePrivateLinkProperties',
    'ManagedInstancePrivateLinkServiceConnectionStateProperty',
    'ManagedInstanceQuery',
    'ManagedInstanceQueryStatistics',
    'ManagedInstanceUpdate',
    'ManagedInstanceVcoresCapability',
    'ManagedInstanceVersionCapability',
    'ManagedInstanceVulnerabilityAssessment',
    'ManagedInstanceVulnerabilityAssessmentListResult',
    'ManagedServerDnsAlias',
    'ManagedServerDnsAliasAcquisition',
    'ManagedServerDnsAliasCreation',
    'ManagedServerDnsAliasListResult',
    'ManagedServerSecurityAlertPolicy',
    'ManagedServerSecurityAlertPolicyListResult',
    'ManagedTransparentDataEncryption',
    'ManagedTransparentDataEncryptionListResult',
    'MaxSizeCapability',
    'MaxSizeRangeCapability',
    'Metric',
    'MetricAvailability',
    'MetricDefinition',
    'MetricDefinitionListResult',
    'MetricListResult',
    'MetricName',
    'MetricValue',
    'MinCapacityCapability',
    'Name',
    'NetworkIsolationSettings',
    'Operation',
    'OperationDisplay',
    'OperationImpact',
    'OperationListResult',
    'OutboundFirewallRule',
    'OutboundFirewallRuleListResult',
    'PartnerInfo',
    'PartnerRegionInfo',
    'PerformanceLevelCapability',
    'PrivateEndpointConnection',
    'PrivateEndpointConnectionListResult',
    'PrivateEndpointConnectionProperties',
    'PrivateEndpointConnectionRequestStatus',
    'PrivateEndpointProperty',
    'PrivateLinkResource',
    'PrivateLinkResourceListResult',
    'PrivateLinkResourceProperties',
    'PrivateLinkServiceConnectionStateProperty',
    'ProxyResource',
    'ProxyResourceWithWritableName',
    'QueryMetricInterval',
    'QueryMetricProperties',
    'QueryStatistics',
    'QueryStatisticsProperties',
    'ReadScaleCapability',
    'RecommendedAction',
    'RecommendedActionErrorInfo',
    'RecommendedActionImpactRecord',
    'RecommendedActionImplementationInfo',
    'RecommendedActionMetricInfo',
    'RecommendedActionStateInfo',
    'RecommendedSensitivityLabelUpdate',
    'RecommendedSensitivityLabelUpdateList',
    'RecoverableDatabase',
    'RecoverableDatabaseListResult',
    'RecoverableManagedDatabase',
    'RecoverableManagedDatabaseListResult',
    'ReplicationLink',
    'ReplicationLinkListResult',
    'Resource',
    'ResourceIdentity',
    'ResourceMoveDefinition',
    'ResourceWithWritableName',
    'RestorableDroppedDatabase',
    'RestorableDroppedDatabaseListResult',
    'RestorableDroppedManagedDatabase',
    'RestorableDroppedManagedDatabaseListResult',
    'RestorePoint',
    'RestorePointListResult',
    'SecurityEvent',
    'SecurityEventCollection',
    'SecurityEventSqlInjectionAdditionalProperties',
    'SecurityEventsFilterParameters',
    'SensitivityLabel',
    'SensitivityLabelListResult',
    'SensitivityLabelUpdate',
    'SensitivityLabelUpdateList',
    'Server',
    'ServerAdvancedThreatProtection',
    'ServerAutomaticTuning',
    'ServerAzureADAdministrator',
    'ServerAzureADOnlyAuthentication',
    'ServerBlobAuditingPolicy',
    'ServerBlobAuditingPolicyListResult',
    'ServerCommunicationLink',
    'ServerCommunicationLinkListResult',
    'ServerConnectionPolicy',
    'ServerConnectionPolicyListResult',
    'ServerDevOpsAuditSettingsListResult',
    'ServerDevOpsAuditingSettings',
    'ServerDnsAlias',
    'ServerDnsAliasAcquisition',
    'ServerDnsAliasListResult',
    'ServerExternalAdministrator',
    'ServerInfo',
    'ServerKey',
    'ServerKeyListResult',
    'ServerListResult',
    'ServerOperation',
    'ServerOperationListResult',
    'ServerPrivateEndpointConnection',
    'ServerSecurityAlertPolicy',
    'ServerTrustCertificate',
    'ServerTrustCertificatesListResult',
    'ServerTrustGroup',
    'ServerTrustGroupListResult',
    'ServerUpdate',
    'ServerUsage',
    'ServerUsageListResult',
    'ServerVersionCapability',
    'ServerVulnerabilityAssessment',
    'ServerVulnerabilityAssessmentListResult',
    'ServiceObjective',
    'ServiceObjectiveCapability',
    'ServiceObjectiveListResult',
    'ServicePrincipal',
    'Sku',
    'SloUsageMetric',
    'SqlAgentConfiguration',
    'StorageCapability',
    'SubscriptionUsage',
    'SubscriptionUsageListResult',
    'SyncAgent',
    'SyncAgentKeyProperties',
    'SyncAgentLinkedDatabase',
    'SyncAgentLinkedDatabaseListResult',
    'SyncAgentListResult',
    'SyncDatabaseIdListResult',
    'SyncDatabaseIdProperties',
    'SyncFullSchemaProperties',
    'SyncFullSchemaPropertiesListResult',
    'SyncFullSchemaTable',
    'SyncFullSchemaTableColumn',
    'SyncGroup',
    'SyncGroupListResult',
    'SyncGroupLogListResult',
    'SyncGroupLogProperties',
    'SyncGroupSchema',
    'SyncGroupSchemaTable',
    'SyncGroupSchemaTableColumn',
    'SyncMember',
    'SyncMemberListResult',
    'SystemData',
    'TdeCertificate',
    'TimeZone',
    'TimeZoneListResult',
    'TopQueries',
    'TopQueriesListResult',
    'TrackedResource',
    'UpdateLongTermRetentionBackupParameters',
    'UpdateManagedInstanceDnsServersOperation',
    'UpsertManagedServerOperationParameters',
    'UpsertManagedServerOperationStep',
    'Usage',
    'UsageListResult',
    'UserIdentity',
    'VirtualCluster',
    'VirtualClusterListResult',
    'VirtualClusterUpdate',
    'VirtualNetworkRule',
    'VirtualNetworkRuleListResult',
    'VulnerabilityAssessmentRecurringScansProperties',
    'VulnerabilityAssessmentScanError',
    'VulnerabilityAssessmentScanRecord',
    'VulnerabilityAssessmentScanRecordListResult',
    'WorkloadClassifier',
    'WorkloadClassifierListResult',
    'WorkloadGroup',
    'WorkloadGroupListResult',
    'AdministratorName',
    'AdministratorType',
    'AdvancedThreatProtectionName',
    'AdvancedThreatProtectionState',
    'AdvisorStatus',
    'AggregationFunctionType',
    'AuthenticationName',
    'AutoExecuteStatus',
    'AutoExecuteStatusInheritedFrom',
    'AutomaticTuningDisabledReason',
    'AutomaticTuningMode',
    'AutomaticTuningOptionModeActual',
    'AutomaticTuningOptionModeDesired',
    'AutomaticTuningServerMode',
    'AutomaticTuningServerReason',
    'BackupStorageRedundancy',
    'BlobAuditingPolicyState',
    'CapabilityGroup',
    'CapabilityStatus',
    'CatalogCollationType',
    'CheckNameAvailabilityReason',
    'ColumnDataType',
    'ConnectionPolicyName',
    'CreateMode',
    'CreatedByType',
    'DataMaskingFunction',
    'DataMaskingRuleState',
    'DataMaskingState',
    'DataWarehouseUserActivityName',
    'DatabaseIdentityType',
    'DatabaseLicenseType',
    'DatabaseReadScale',
    'DatabaseState',
    'DatabaseStatus',
    'DayOfWeek',
    'DiffBackupIntervalInHours',
    'DnsRefreshConfigurationPropertiesStatus',
    'ElasticPoolLicenseType',
    'ElasticPoolState',
    'EncryptionProtectorName',
    'FailoverGroupReplicationRole',
    'GeoBackupPolicyName',
    'GeoBackupPolicyState',
    'IdentityType',
    'ImplementationMethod',
    'InstanceFailoverGroupReplicationRole',
    'InstancePoolLicenseType',
    'IsRetryable',
    'JobAgentState',
    'JobExecutionLifecycle',
    'JobScheduleType',
    'JobStepActionSource',
    'JobStepActionType',
    'JobStepOutputType',
    'JobTargetGroupMembershipType',
    'JobTargetType',
    'LedgerDigestUploadsName',
    'LedgerDigestUploadsState',
    'LogSizeUnit',
    'LongTermRetentionPolicyName',
    'ManagedDatabaseCreateMode',
    'ManagedDatabaseStatus',
    'ManagedInstanceAdministratorType',
    'ManagedInstanceLicenseType',
    'ManagedInstanceLongTermRetentionPolicyName',
    'ManagedInstancePropertiesProvisioningState',
    'ManagedInstanceProxyOverride',
    'ManagedServerCreateMode',
    'ManagedShortTermRetentionPolicyName',
    'ManagementOperationState',
    'MaxSizeUnit',
    'MetricType',
    'OperationMode',
    'OperationOrigin',
    'PauseDelayTimeUnit',
    'PerformanceLevelUnit',
    'PrimaryAggregationType',
    'PrincipalType',
    'PrivateEndpointProvisioningState',
    'PrivateLinkServiceConnectionStateActionsRequire',
    'PrivateLinkServiceConnectionStateStatus',
    'ProvisioningState',
    'QueryMetricUnitType',
    'QueryTimeGrainType',
    'ReadOnlyEndpointFailoverPolicy',
    'ReadWriteEndpointFailoverPolicy',
    'RecommendedActionCurrentState',
    'RecommendedActionInitiatedBy',
    'RecommendedSensitivityLabelUpdateKind',
    'ReplicaType',
    'ReplicationLinkType',
    'ReplicationMode',
    'ReplicationRole',
    'ReplicationState',
    'RestoreDetailsName',
    'RestorePointType',
    'SampleName',
    'SecondaryType',
    'SecurityAlertPolicyName',
    'SecurityAlertPolicyState',
    'SecurityAlertsPolicyState',
    'SecurityEventType',
    'SensitivityLabelRank',
    'SensitivityLabelSource',
    'SensitivityLabelUpdateKind',
    'ServerConnectionType',
    'ServerKeyType',
    'ServerNetworkAccessFlag',
    'ServerTrustGroupPropertiesTrustScopesItem',
    'ServerWorkspaceFeature',
    'ServiceObjectiveName',
    'ServicePrincipalType',
    'ShortTermRetentionPolicyName',
    'SqlAgentConfigurationPropertiesState',
    'StorageCapabilityStorageAccountType',
    'StorageKeyType',
    'SyncAgentState',
    'SyncConflictResolutionPolicy',
    'SyncDirection',
    'SyncGroupLogType',
    'SyncGroupState',
    'SyncGroupsType',
    'SyncMemberDbType',
    'SyncMemberState',
    'TableTemporalType',
    'TransparentDataEncryptionName',
    'TransparentDataEncryptionState',
    'UnitDefinitionType',
    'UnitType',
    'UpsertManagedServerOperationStepStatus',
    'VirtualNetworkRuleState',
    'VulnerabilityAssessmentName',
    'VulnerabilityAssessmentPolicyBaselineName',
    'VulnerabilityAssessmentScanState',
    'VulnerabilityAssessmentScanTriggerType',
]
__all__.extend([p for p in _patch_all if p not in __all__])
_patch_sdk()