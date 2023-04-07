# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from ._models_py3 import Agent
from ._models_py3 import AgentList
from ._models_py3 import AgentPropertiesErrorDetails
from ._models_py3 import AgentUpdateParameters
from ._models_py3 import AzureStorageBlobContainerEndpointProperties
from ._models_py3 import AzureStorageBlobContainerEndpointUpdateProperties
from ._models_py3 import Endpoint
from ._models_py3 import EndpointBaseProperties
from ._models_py3 import EndpointBaseUpdateParameters
from ._models_py3 import EndpointBaseUpdateProperties
from ._models_py3 import EndpointList
from ._models_py3 import ErrorAdditionalInfo
from ._models_py3 import ErrorDetail
from ._models_py3 import ErrorResponse
from ._models_py3 import JobDefinition
from ._models_py3 import JobDefinitionList
from ._models_py3 import JobDefinitionUpdateParameters
from ._models_py3 import JobRun
from ._models_py3 import JobRunError
from ._models_py3 import JobRunList
from ._models_py3 import JobRunResourceId
from ._models_py3 import NfsMountEndpointProperties
from ._models_py3 import NfsMountEndpointUpdateProperties
from ._models_py3 import Operation
from ._models_py3 import OperationDisplay
from ._models_py3 import OperationListResult
from ._models_py3 import Project
from ._models_py3 import ProjectList
from ._models_py3 import ProjectUpdateParameters
from ._models_py3 import ProxyResource
from ._models_py3 import Resource
from ._models_py3 import StorageMover
from ._models_py3 import StorageMoverList
from ._models_py3 import StorageMoverUpdateParameters
from ._models_py3 import SystemData
from ._models_py3 import TrackedResource

from ._storage_mover_mgmt_client_enums import ActionType
from ._storage_mover_mgmt_client_enums import AgentStatus
from ._storage_mover_mgmt_client_enums import CopyMode
from ._storage_mover_mgmt_client_enums import CreatedByType
from ._storage_mover_mgmt_client_enums import EndpointType
from ._storage_mover_mgmt_client_enums import JobRunScanStatus
from ._storage_mover_mgmt_client_enums import JobRunStatus
from ._storage_mover_mgmt_client_enums import NfsVersion
from ._storage_mover_mgmt_client_enums import Origin
from ._storage_mover_mgmt_client_enums import ProvisioningState
from ._patch import __all__ as _patch_all
from ._patch import *  # pylint: disable=unused-wildcard-import
from ._patch import patch_sdk as _patch_sdk

__all__ = [
    "Agent",
    "AgentList",
    "AgentPropertiesErrorDetails",
    "AgentUpdateParameters",
    "AzureStorageBlobContainerEndpointProperties",
    "AzureStorageBlobContainerEndpointUpdateProperties",
    "Endpoint",
    "EndpointBaseProperties",
    "EndpointBaseUpdateParameters",
    "EndpointBaseUpdateProperties",
    "EndpointList",
    "ErrorAdditionalInfo",
    "ErrorDetail",
    "ErrorResponse",
    "JobDefinition",
    "JobDefinitionList",
    "JobDefinitionUpdateParameters",
    "JobRun",
    "JobRunError",
    "JobRunList",
    "JobRunResourceId",
    "NfsMountEndpointProperties",
    "NfsMountEndpointUpdateProperties",
    "Operation",
    "OperationDisplay",
    "OperationListResult",
    "Project",
    "ProjectList",
    "ProjectUpdateParameters",
    "ProxyResource",
    "Resource",
    "StorageMover",
    "StorageMoverList",
    "StorageMoverUpdateParameters",
    "SystemData",
    "TrackedResource",
    "ActionType",
    "AgentStatus",
    "CopyMode",
    "CreatedByType",
    "EndpointType",
    "JobRunScanStatus",
    "JobRunStatus",
    "NfsVersion",
    "Origin",
    "ProvisioningState",
]
__all__.extend([p for p in _patch_all if p not in __all__])
_patch_sdk()
