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


class ErrorCode(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Human-readable error code.
    """

    INVALID_REQUEST = "InvalidRequest"
    INVALID_ARGUMENT = "InvalidArgument"
    UNAUTHORIZED = "Unauthorized"
    FORBIDDEN = "Forbidden"
    NOT_FOUND = "NotFound"
    PROJECT_NOT_FOUND = "ProjectNotFound"
    OPERATION_NOT_FOUND = "OperationNotFound"
    AZURE_COGNITIVE_SEARCH_NOT_FOUND = "AzureCognitiveSearchNotFound"
    AZURE_COGNITIVE_SEARCH_INDEX_NOT_FOUND = "AzureCognitiveSearchIndexNotFound"
    TOO_MANY_REQUESTS = "TooManyRequests"
    AZURE_COGNITIVE_SEARCH_THROTTLING = "AzureCognitiveSearchThrottling"
    AZURE_COGNITIVE_SEARCH_INDEX_LIMIT_REACHED = "AzureCognitiveSearchIndexLimitReached"
    INTERNAL_SERVER_ERROR = "InternalServerError"
    SERVICE_UNAVAILABLE = "ServiceUnavailable"

class InnerErrorCode(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Human-readable error code.
    """

    INVALID_REQUEST = "InvalidRequest"
    INVALID_PARAMETER_VALUE = "InvalidParameterValue"
    KNOWLEDGE_BASE_NOT_FOUND = "KnowledgeBaseNotFound"
    AZURE_COGNITIVE_SEARCH_NOT_FOUND = "AzureCognitiveSearchNotFound"
    AZURE_COGNITIVE_SEARCH_THROTTLING = "AzureCognitiveSearchThrottling"
    EXTRACTION_FAILURE = "ExtractionFailure"

class ProjectKind(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The type of the project.
    """

    CONVERSATION = "conversation"
    WORKFLOW = "workflow"

class TargetKind(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The type of a target service.
    """

    LUIS = "luis"
    CONVERSATION = "conversation"
    QUESTION_ANSWERING = "question_answering"
    NON_LINKED = "non_linked"
