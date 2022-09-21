# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, Callable, Dict, List, Optional, TypeVar

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
from ...operations._virtual_machine_extension_images_operations import (
    build_get_request,
    build_list_types_request,
    build_list_versions_request,
)

T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class VirtualMachineExtensionImagesOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.mgmt.compute.v2021_11_01.aio.ComputeManagementClient`'s
        :attr:`virtual_machine_extension_images` attribute.
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
        self, location: str, publisher_name: str, type: str, version: str, **kwargs: Any
    ) -> _models.VirtualMachineExtensionImage:
        """Gets a virtual machine extension image.

        :param location: The name of a supported Azure region. Required.
        :type location: str
        :param publisher_name: Required.
        :type publisher_name: str
        :param type: Required.
        :type type: str
        :param version: Required.
        :type version: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: VirtualMachineExtensionImage or the result of cls(response)
        :rtype: ~azure.mgmt.compute.v2021_11_01.models.VirtualMachineExtensionImage
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

        api_version = kwargs.pop("api_version", _params.pop("api-version", "2021-11-01"))  # type: str
        cls = kwargs.pop("cls", None)  # type: ClsType[_models.VirtualMachineExtensionImage]

        request = build_get_request(
            location=location,
            publisher_name=publisher_name,
            type=type,
            version=version,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            template_url=self.get.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize("VirtualMachineExtensionImage", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get.metadata = {"url": "/subscriptions/{subscriptionId}/providers/Microsoft.Compute/locations/{location}/publishers/{publisherName}/artifacttypes/vmextension/types/{type}/versions/{version}"}  # type: ignore

    @distributed_trace_async
    async def list_types(
        self, location: str, publisher_name: str, **kwargs: Any
    ) -> List[_models.VirtualMachineExtensionImage]:
        """Gets a list of virtual machine extension image types.

        :param location: The name of a supported Azure region. Required.
        :type location: str
        :param publisher_name: Required.
        :type publisher_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: list of VirtualMachineExtensionImage or the result of cls(response)
        :rtype: list[~azure.mgmt.compute.v2021_11_01.models.VirtualMachineExtensionImage]
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

        api_version = kwargs.pop("api_version", _params.pop("api-version", "2021-11-01"))  # type: str
        cls = kwargs.pop("cls", None)  # type: ClsType[List[_models.VirtualMachineExtensionImage]]

        request = build_list_types_request(
            location=location,
            publisher_name=publisher_name,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            template_url=self.list_types.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize("[VirtualMachineExtensionImage]", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    list_types.metadata = {"url": "/subscriptions/{subscriptionId}/providers/Microsoft.Compute/locations/{location}/publishers/{publisherName}/artifacttypes/vmextension/types"}  # type: ignore

    @distributed_trace_async
    async def list_versions(
        self,
        location: str,
        publisher_name: str,
        type: str,
        filter: Optional[str] = None,
        top: Optional[int] = None,
        orderby: Optional[str] = None,
        **kwargs: Any
    ) -> List[_models.VirtualMachineExtensionImage]:
        """Gets a list of virtual machine extension image versions.

        :param location: The name of a supported Azure region. Required.
        :type location: str
        :param publisher_name: Required.
        :type publisher_name: str
        :param type: Required.
        :type type: str
        :param filter: The filter to apply on the operation. Default value is None.
        :type filter: str
        :param top: Default value is None.
        :type top: int
        :param orderby: Default value is None.
        :type orderby: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: list of VirtualMachineExtensionImage or the result of cls(response)
        :rtype: list[~azure.mgmt.compute.v2021_11_01.models.VirtualMachineExtensionImage]
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

        api_version = kwargs.pop("api_version", _params.pop("api-version", "2021-11-01"))  # type: str
        cls = kwargs.pop("cls", None)  # type: ClsType[List[_models.VirtualMachineExtensionImage]]

        request = build_list_versions_request(
            location=location,
            publisher_name=publisher_name,
            type=type,
            subscription_id=self._config.subscription_id,
            filter=filter,
            top=top,
            orderby=orderby,
            api_version=api_version,
            template_url=self.list_versions.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize("[VirtualMachineExtensionImage]", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    list_versions.metadata = {"url": "/subscriptions/{subscriptionId}/providers/Microsoft.Compute/locations/{location}/publishers/{publisherName}/artifacttypes/vmextension/types/{type}/versions"}  # type: ignore
