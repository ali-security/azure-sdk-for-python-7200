# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import sys
from typing import Any, Callable, Dict, IO, Optional, TypeVar, Union, overload

from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    ResourceNotModifiedError,
    map_error,
)
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator_async import distributed_trace_async
from azure.core.utils import case_insensitive_dict
from azure.mgmt.core.exceptions import ARMErrorFormat

from ... import models as _models
from ..._vendor import _convert_request
from ...operations._scope_role_assignment_approval_step_operations import (
    build_get_by_id_request,
    build_patch_request,
    build_put_request,
)

if sys.version_info >= (3, 8):
    from typing import Literal  # pylint: disable=no-name-in-module, ungrouped-imports
else:
    from typing_extensions import Literal  # type: ignore  # pylint: disable=ungrouped-imports
T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class ScopeRoleAssignmentApprovalStepOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.mgmt.authorization.v2021_01_01_preview.aio.AuthorizationManagementClient`'s
        :attr:`scope_role_assignment_approval_step` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs) -> None:
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @distributed_trace_async
    async def get_by_id(
        self, approval_id: str, stage_id: str, scope: str, **kwargs: Any
    ) -> _models.RoleAssignmentApprovalStep:
        """Get role assignment approval.

        :param approval_id: The id of the role assignment approval. Required.
        :type approval_id: str
        :param stage_id: The id of the role assignment approval stage. Required.
        :type stage_id: str
        :param scope: The scope of the resource. Required.
        :type scope: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: RoleAssignmentApprovalStep or the result of cls(response)
        :rtype: ~azure.mgmt.authorization.v2021_01_01_preview.models.RoleAssignmentApprovalStep
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: Literal["2021-01-01-preview"] = kwargs.pop(
            "api_version", _params.pop("api-version", "2021-01-01-preview")
        )
        cls: ClsType[_models.RoleAssignmentApprovalStep] = kwargs.pop("cls", None)

        request = build_get_by_id_request(
            approval_id=approval_id,
            stage_id=stage_id,
            scope=scope,
            api_version=api_version,
            template_url=self.get_by_id.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorDefinition, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize("RoleAssignmentApprovalStep", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_by_id.metadata = {
        "url": "/{scope}/providers/Microsoft.Authorization/roleAssignmentApprovals/{approvalId}/stages/{stageId}"
    }

    @overload
    async def patch(
        self,
        approval_id: str,
        stage_id: str,
        scope: str,
        properties: _models.RoleAssignmentApprovalStepProperties,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.RoleAssignmentApprovalStep:
        """Record a decision.

        :param approval_id: The id of the role assignment approval. Required.
        :type approval_id: str
        :param stage_id: The id of the role assignment approval stage. Required.
        :type stage_id: str
        :param scope: The scope of the resource. Required.
        :type scope: str
        :param properties: Role Assignment Approval stage properties to patch. Required.
        :type properties:
         ~azure.mgmt.authorization.v2021_01_01_preview.models.RoleAssignmentApprovalStepProperties
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: RoleAssignmentApprovalStep or the result of cls(response)
        :rtype: ~azure.mgmt.authorization.v2021_01_01_preview.models.RoleAssignmentApprovalStep
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def patch(
        self,
        approval_id: str,
        stage_id: str,
        scope: str,
        properties: IO,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.RoleAssignmentApprovalStep:
        """Record a decision.

        :param approval_id: The id of the role assignment approval. Required.
        :type approval_id: str
        :param stage_id: The id of the role assignment approval stage. Required.
        :type stage_id: str
        :param scope: The scope of the resource. Required.
        :type scope: str
        :param properties: Role Assignment Approval stage properties to patch. Required.
        :type properties: IO
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: RoleAssignmentApprovalStep or the result of cls(response)
        :rtype: ~azure.mgmt.authorization.v2021_01_01_preview.models.RoleAssignmentApprovalStep
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def patch(
        self,
        approval_id: str,
        stage_id: str,
        scope: str,
        properties: Union[_models.RoleAssignmentApprovalStepProperties, IO],
        **kwargs: Any
    ) -> _models.RoleAssignmentApprovalStep:
        """Record a decision.

        :param approval_id: The id of the role assignment approval. Required.
        :type approval_id: str
        :param stage_id: The id of the role assignment approval stage. Required.
        :type stage_id: str
        :param scope: The scope of the resource. Required.
        :type scope: str
        :param properties: Role Assignment Approval stage properties to patch. Is either a
         RoleAssignmentApprovalStepProperties type or a IO type. Required.
        :type properties:
         ~azure.mgmt.authorization.v2021_01_01_preview.models.RoleAssignmentApprovalStepProperties or IO
        :keyword content_type: Body Parameter content-type. Known values are: 'application/json'.
         Default value is None.
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: RoleAssignmentApprovalStep or the result of cls(response)
        :rtype: ~azure.mgmt.authorization.v2021_01_01_preview.models.RoleAssignmentApprovalStep
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: Literal["2021-01-01-preview"] = kwargs.pop(
            "api_version", _params.pop("api-version", "2021-01-01-preview")
        )
        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.RoleAssignmentApprovalStep] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(properties, (IO, bytes)):
            _content = properties
        else:
            _json = self._serialize.body(properties, "RoleAssignmentApprovalStepProperties")

        request = build_patch_request(
            approval_id=approval_id,
            stage_id=stage_id,
            scope=scope,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            content=_content,
            template_url=self.patch.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorDefinition, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize("RoleAssignmentApprovalStep", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    patch.metadata = {
        "url": "/{scope}/providers/Microsoft.Authorization/roleAssignmentApprovals/{approvalId}/stages/{stageId}"
    }

    @overload
    async def put(
        self,
        approval_id: str,
        stage_id: str,
        scope: str,
        properties: _models.RoleAssignmentApprovalStepProperties,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.RoleAssignmentApprovalStep:
        """Record a decision.

        :param approval_id: The id of the role assignment approval. Required.
        :type approval_id: str
        :param stage_id: The id of the role assignment approval stage. Required.
        :type stage_id: str
        :param scope: The scope of the resource. Required.
        :type scope: str
        :param properties: Role Assignment Approval stage properties to put. Required.
        :type properties:
         ~azure.mgmt.authorization.v2021_01_01_preview.models.RoleAssignmentApprovalStepProperties
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: RoleAssignmentApprovalStep or the result of cls(response)
        :rtype: ~azure.mgmt.authorization.v2021_01_01_preview.models.RoleAssignmentApprovalStep
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def put(
        self,
        approval_id: str,
        stage_id: str,
        scope: str,
        properties: IO,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.RoleAssignmentApprovalStep:
        """Record a decision.

        :param approval_id: The id of the role assignment approval. Required.
        :type approval_id: str
        :param stage_id: The id of the role assignment approval stage. Required.
        :type stage_id: str
        :param scope: The scope of the resource. Required.
        :type scope: str
        :param properties: Role Assignment Approval stage properties to put. Required.
        :type properties: IO
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: RoleAssignmentApprovalStep or the result of cls(response)
        :rtype: ~azure.mgmt.authorization.v2021_01_01_preview.models.RoleAssignmentApprovalStep
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def put(
        self,
        approval_id: str,
        stage_id: str,
        scope: str,
        properties: Union[_models.RoleAssignmentApprovalStepProperties, IO],
        **kwargs: Any
    ) -> _models.RoleAssignmentApprovalStep:
        """Record a decision.

        :param approval_id: The id of the role assignment approval. Required.
        :type approval_id: str
        :param stage_id: The id of the role assignment approval stage. Required.
        :type stage_id: str
        :param scope: The scope of the resource. Required.
        :type scope: str
        :param properties: Role Assignment Approval stage properties to put. Is either a
         RoleAssignmentApprovalStepProperties type or a IO type. Required.
        :type properties:
         ~azure.mgmt.authorization.v2021_01_01_preview.models.RoleAssignmentApprovalStepProperties or IO
        :keyword content_type: Body Parameter content-type. Known values are: 'application/json'.
         Default value is None.
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: RoleAssignmentApprovalStep or the result of cls(response)
        :rtype: ~azure.mgmt.authorization.v2021_01_01_preview.models.RoleAssignmentApprovalStep
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: Literal["2021-01-01-preview"] = kwargs.pop(
            "api_version", _params.pop("api-version", "2021-01-01-preview")
        )
        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.RoleAssignmentApprovalStep] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(properties, (IO, bytes)):
            _content = properties
        else:
            _json = self._serialize.body(properties, "RoleAssignmentApprovalStepProperties")

        request = build_put_request(
            approval_id=approval_id,
            stage_id=stage_id,
            scope=scope,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            content=_content,
            template_url=self.put.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorDefinition, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize("RoleAssignmentApprovalStep", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    put.metadata = {
        "url": "/{scope}/providers/Microsoft.Authorization/roleAssignmentApprovals/{approvalId}/stages/{stageId}"
    }
