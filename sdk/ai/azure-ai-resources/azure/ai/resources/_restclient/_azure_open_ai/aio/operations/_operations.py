# pylint: disable=too-many-lines,too-many-statements
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from io import IOBase
import sys
from typing import Any, Callable, Dict, IO, Optional, TypeVar, Union, cast, overload

from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    ResourceNotModifiedError,
    map_error,
)
from azure.core.pipeline import PipelineResponse
from azure.core.polling import AsyncLROPoller, AsyncNoPolling, AsyncPollingMethod
from azure.core.rest import AsyncHttpResponse, HttpRequest
from azure.core.tracing.decorator_async import distributed_trace_async
from azure.core.utils import case_insensitive_dict
from azure.mgmt.core.exceptions import ARMErrorFormat
from azure.mgmt.core.polling.async_arm_polling import AsyncARMPolling

from ... import models as _models
from ...operations._operations import (
    build_azure_open_ai_deployments_begin_create_or_update_request,
    build_azure_open_ai_deployments_delete_request,
    build_azure_open_ai_deployments_get_request,
    build_azure_open_ai_deployments_update_request,
)

if sys.version_info >= (3, 9):
    from collections.abc import MutableMapping
else:
    from typing import MutableMapping  # type: ignore  # pylint: disable=ungrouped-imports
JSON = MutableMapping[str, Any]  # pylint: disable=unsubscriptable-object
T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class AzureOpenAIDeploymentsOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.ai.resources.autogen.aio.MachineLearningServicesClient`'s
        :attr:`azure_open_ai_deployments` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs) -> None:
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @distributed_trace_async
    async def get(
        self, resource_group_name: str, workspace_name: str, endpoint_name: str, deployment_name: str, **kwargs: Any
    ) -> _models.AzureOpenAIDeployment:
        """Get a AzureOpenAIDeployment.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param workspace_name: Name of the workspace. Required.
        :type workspace_name: str
        :param endpoint_name: The name of the online deployment. Required.
        :type endpoint_name: str
        :param deployment_name: The name of the deployment. Required.
        :type deployment_name: str
        :return: AzureOpenAIDeployment
        :rtype: ~azure.ai.resources.autogen.models.AzureOpenAIDeployment
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
        _params = kwargs.pop("params", {}) or {}

        cls: ClsType[_models.AzureOpenAIDeployment] = kwargs.pop("cls", None)

        _request = build_azure_open_ai_deployments_get_request(
            resource_group_name=resource_group_name,
            workspace_name=workspace_name,
            endpoint_name=endpoint_name,
            deployment_name=deployment_name,
            subscription_id=self._config.subscription_id,
            api_version=self._config.api_version,
            headers=_headers,
            params=_params,
        )
        _request.url = self._client.format_url(_request.url)

        _stream = kwargs.pop("stream", False)
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            if _stream:
                await response.read()  # Load the body in memory and close the socket
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if _stream:
            deserialized = response.iter_bytes()
        else:
            deserialized = self._deserialize("AzureOpenAIDeployment", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    @overload
    async def begin_create_or_update(
        self,
        resource_group_name: str,
        workspace_name: str,
        endpoint_name: str,
        deployment_name: str,
        resource: _models.AzureOpenAIDeployment,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.AzureOpenAIDeployment:
        """Create a AzureOpenAIDeployment.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param workspace_name: Name of the workspace. Required.
        :type workspace_name: str
        :param endpoint_name: The name of the online deployment. Required.
        :type endpoint_name: str
        :param deployment_name: The name of the deployment. Required.
        :type deployment_name: str
        :param resource: Resource create parameters. Required.
        :type resource: ~azure.ai.resources.autogen.models.AzureOpenAIDeployment
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: AzureOpenAIDeployment
        :rtype: ~azure.ai.resources.autogen.models.AzureOpenAIDeployment
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def begin_create_or_update(
        self,
        resource_group_name: str,
        workspace_name: str,
        endpoint_name: str,
        deployment_name: str,
        resource: IO[bytes],
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.AzureOpenAIDeployment:
        """Create a AzureOpenAIDeployment.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param workspace_name: Name of the workspace. Required.
        :type workspace_name: str
        :param endpoint_name: The name of the online deployment. Required.
        :type endpoint_name: str
        :param deployment_name: The name of the deployment. Required.
        :type deployment_name: str
        :param resource: Resource create parameters. Required.
        :type resource: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: AzureOpenAIDeployment
        :rtype: ~azure.ai.resources.autogen.models.AzureOpenAIDeployment
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def begin_create_or_update(
        self,
        resource_group_name: str,
        workspace_name: str,
        endpoint_name: str,
        deployment_name: str,
        resource: Union[_models.AzureOpenAIDeployment, IO[bytes]],
        **kwargs: Any
    ) -> _models.AzureOpenAIDeployment:
        """Create a AzureOpenAIDeployment.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param workspace_name: Name of the workspace. Required.
        :type workspace_name: str
        :param endpoint_name: The name of the online deployment. Required.
        :type endpoint_name: str
        :param deployment_name: The name of the deployment. Required.
        :type deployment_name: str
        :param resource: Resource create parameters. Is either a AzureOpenAIDeployment type or a
         IO[bytes] type. Required.
        :type resource: ~azure.ai.resources.autogen.models.AzureOpenAIDeployment or IO[bytes]
        :return: AzureOpenAIDeployment
        :rtype: ~azure.ai.resources.autogen.models.AzureOpenAIDeployment
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
        _params = kwargs.pop("params", {}) or {}

        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.AzureOpenAIDeployment] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(resource, (IOBase, bytes)):
            _content = resource
        else:
            _json = self._serialize.body(resource, "AzureOpenAIDeployment")

        _request = build_azure_open_ai_deployments_begin_create_or_update_request(
            resource_group_name=resource_group_name,
            workspace_name=workspace_name,
            endpoint_name=endpoint_name,
            deployment_name=deployment_name,
            subscription_id=self._config.subscription_id,
            api_version=self._config.api_version,
            content_type=content_type,
            json=_json,
            content=_content,
            headers=_headers,
            params=_params,
        )
        _request.url = self._client.format_url(_request.url)

        _stream = kwargs.pop("stream", False)
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200, 201]:
            if _stream:
                await response.read()  # Load the body in memory and close the socket
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        response_headers = {}
        if response.status_code == 200:
            if _stream:
                deserialized = response.iter_bytes()
            else:
                deserialized = self._deserialize("AzureOpenAIDeployment", pipeline_response)

        if response.status_code == 201:
            response_headers["Retry-After"] = self._deserialize("int", response.headers.get("Retry-After"))

            if _stream:
                deserialized = response.iter_bytes()
            else:
                deserialized = self._deserialize("AzureOpenAIDeployment", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, response_headers)  # type: ignore

        return deserialized  # type: ignore

    async def _update_initial(
        self,
        resource_group_name: str,
        workspace_name: str,
        endpoint_name: str,
        deployment_name: str,
        properties: Union[_models.AzureOpenAIDeploymentUpdate, IO[bytes]],
        **kwargs: Any
    ) -> Optional[JSON]:
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = kwargs.pop("params", {}) or {}

        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[Optional[JSON]] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(properties, (IOBase, bytes)):
            _content = properties
        else:
            _json = self._serialize.body(properties, "AzureOpenAIDeploymentUpdate")

        _request = build_azure_open_ai_deployments_update_request(
            resource_group_name=resource_group_name,
            workspace_name=workspace_name,
            endpoint_name=endpoint_name,
            deployment_name=deployment_name,
            subscription_id=self._config.subscription_id,
            api_version=self._config.api_version,
            content_type=content_type,
            json=_json,
            content=_content,
            headers=_headers,
            params=_params,
        )
        _request.url = self._client.format_url(_request.url)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200, 202]:
            if _stream:
                await response.read()  # Load the body in memory and close the socket
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = None
        response_headers = {}
        if response.status_code == 200:
            deserialized = self._deserialize("object", pipeline_response)

        if response.status_code == 202:
            response_headers["Retry-After"] = self._deserialize("int", response.headers.get("Retry-After"))
            response_headers["Location"] = self._deserialize("str", response.headers.get("Location"))

        if cls:
            return cls(pipeline_response, deserialized, response_headers)  # type: ignore

        return deserialized  # type: ignore

    @overload
    async def begin_update(
        self,
        resource_group_name: str,
        workspace_name: str,
        endpoint_name: str,
        deployment_name: str,
        properties: _models.AzureOpenAIDeploymentUpdate,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> AsyncLROPoller[_models.AzureOpenAIDeployment]:
        """Update a AzureOpenAIDeployment.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param workspace_name: Name of the workspace. Required.
        :type workspace_name: str
        :param endpoint_name: The name of the online deployment. Required.
        :type endpoint_name: str
        :param deployment_name: The name of the deployment. Required.
        :type deployment_name: str
        :param properties: The resource properties to be updated. Required.
        :type properties: ~azure.ai.resources.autogen.models.AzureOpenAIDeploymentUpdate
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of AsyncLROPoller that returns AzureOpenAIDeployment
        :rtype:
         ~azure.core.polling.AsyncLROPoller[~azure.ai.resources.autogen.models.AzureOpenAIDeployment]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def begin_update(
        self,
        resource_group_name: str,
        workspace_name: str,
        endpoint_name: str,
        deployment_name: str,
        properties: IO[bytes],
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> AsyncLROPoller[_models.AzureOpenAIDeployment]:
        """Update a AzureOpenAIDeployment.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param workspace_name: Name of the workspace. Required.
        :type workspace_name: str
        :param endpoint_name: The name of the online deployment. Required.
        :type endpoint_name: str
        :param deployment_name: The name of the deployment. Required.
        :type deployment_name: str
        :param properties: The resource properties to be updated. Required.
        :type properties: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of AsyncLROPoller that returns AzureOpenAIDeployment
        :rtype:
         ~azure.core.polling.AsyncLROPoller[~azure.ai.resources.autogen.models.AzureOpenAIDeployment]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def begin_update(
        self,
        resource_group_name: str,
        workspace_name: str,
        endpoint_name: str,
        deployment_name: str,
        properties: Union[_models.AzureOpenAIDeploymentUpdate, IO[bytes]],
        **kwargs: Any
    ) -> AsyncLROPoller[_models.AzureOpenAIDeployment]:
        """Update a AzureOpenAIDeployment.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param workspace_name: Name of the workspace. Required.
        :type workspace_name: str
        :param endpoint_name: The name of the online deployment. Required.
        :type endpoint_name: str
        :param deployment_name: The name of the deployment. Required.
        :type deployment_name: str
        :param properties: The resource properties to be updated. Is either a
         AzureOpenAIDeploymentUpdate type or a IO[bytes] type. Required.
        :type properties: ~azure.ai.resources.autogen.models.AzureOpenAIDeploymentUpdate or IO[bytes]
        :return: An instance of AsyncLROPoller that returns AzureOpenAIDeployment
        :rtype:
         ~azure.core.polling.AsyncLROPoller[~azure.ai.resources.autogen.models.AzureOpenAIDeployment]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = kwargs.pop("params", {}) or {}

        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.AzureOpenAIDeployment] = kwargs.pop("cls", None)
        polling: Union[bool, AsyncPollingMethod] = kwargs.pop("polling", True)
        lro_delay = kwargs.pop("polling_interval", self._config.polling_interval)
        cont_token: Optional[str] = kwargs.pop("continuation_token", None)
        if cont_token is None:
            raw_result = await self._update_initial(
                resource_group_name=resource_group_name,
                workspace_name=workspace_name,
                endpoint_name=endpoint_name,
                deployment_name=deployment_name,
                properties=properties,
                content_type=content_type,
                cls=lambda x, y, z: x,
                headers=_headers,
                params=_params,
                **kwargs
            )
        kwargs.pop("error_map", None)

        def get_long_running_output(pipeline_response):
            deserialized = self._deserialize("AzureOpenAIDeployment", pipeline_response)
            if cls:
                return cls(pipeline_response, deserialized, {})  # type: ignore
            return deserialized

        if polling is True:
            polling_method: AsyncPollingMethod = cast(AsyncPollingMethod, AsyncARMPolling(lro_delay, **kwargs))
        elif polling is False:
            polling_method = cast(AsyncPollingMethod, AsyncNoPolling())
        else:
            polling_method = polling
        if cont_token:
            return AsyncLROPoller[_models.AzureOpenAIDeployment].from_continuation_token(
                polling_method=polling_method,
                continuation_token=cont_token,
                client=self._client,
                deserialization_callback=get_long_running_output,
            )
        return AsyncLROPoller[_models.AzureOpenAIDeployment](
            self._client, raw_result, get_long_running_output, polling_method  # type: ignore
        )

    async def _delete_initial(  # pylint: disable=inconsistent-return-statements
        self, resource_group_name: str, workspace_name: str, endpoint_name: str, deployment_name: str, **kwargs: Any
    ) -> None:
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls: ClsType[None] = kwargs.pop("cls", None)

        _request = build_azure_open_ai_deployments_delete_request(
            resource_group_name=resource_group_name,
            workspace_name=workspace_name,
            endpoint_name=endpoint_name,
            deployment_name=deployment_name,
            subscription_id=self._config.subscription_id,
            api_version=self._config.api_version,
            headers=_headers,
            params=_params,
        )
        _request.url = self._client.format_url(_request.url)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200, 202, 204]:
            if _stream:
                await response.read()  # Load the body in memory and close the socket
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        response_headers = {}
        if response.status_code == 202:
            response_headers["Retry-After"] = self._deserialize("int", response.headers.get("Retry-After"))
            response_headers["Location"] = self._deserialize("str", response.headers.get("Location"))

        if cls:
            return cls(pipeline_response, None, response_headers)  # type: ignore

    @distributed_trace_async
    async def begin_delete(
        self, resource_group_name: str, workspace_name: str, endpoint_name: str, deployment_name: str, **kwargs: Any
    ) -> AsyncLROPoller[_models.ArmOperationStatus]:
        """Delete a AzureOpenAIDeployment.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param workspace_name: Name of the workspace. Required.
        :type workspace_name: str
        :param endpoint_name: The name of the online deployment. Required.
        :type endpoint_name: str
        :param deployment_name: The name of the deployment. Required.
        :type deployment_name: str
        :return: An instance of AsyncLROPoller that returns ArmOperationStatus
        :rtype:
         ~azure.core.polling.AsyncLROPoller[~azure.ai.resources.autogen.models.ArmOperationStatus]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls: ClsType[_models.ArmOperationStatus] = kwargs.pop("cls", None)
        polling: Union[bool, AsyncPollingMethod] = kwargs.pop("polling", True)
        lro_delay = kwargs.pop("polling_interval", self._config.polling_interval)
        cont_token: Optional[str] = kwargs.pop("continuation_token", None)
        if cont_token is None:
            raw_result = await self._delete_initial(  # type: ignore
                resource_group_name=resource_group_name,
                workspace_name=workspace_name,
                endpoint_name=endpoint_name,
                deployment_name=deployment_name,
                cls=lambda x, y, z: x,
                headers=_headers,
                params=_params,
                **kwargs
            )
        kwargs.pop("error_map", None)

        def get_long_running_output(pipeline_response):
            deserialized = self._deserialize("ArmOperationStatus", pipeline_response)
            if cls:
                return cls(pipeline_response, deserialized, {})  # type: ignore
            return deserialized

        if polling is True:
            polling_method: AsyncPollingMethod = cast(AsyncPollingMethod, AsyncARMPolling(lro_delay, **kwargs))
        elif polling is False:
            polling_method = cast(AsyncPollingMethod, AsyncNoPolling())
        else:
            polling_method = polling
        if cont_token:
            return AsyncLROPoller[_models.ArmOperationStatus].from_continuation_token(
                polling_method=polling_method,
                continuation_token=cont_token,
                client=self._client,
                deserialization_callback=get_long_running_output,
            )
        return AsyncLROPoller[_models.ArmOperationStatus](
            self._client, raw_result, get_long_running_output, polling_method  # type: ignore
        )
