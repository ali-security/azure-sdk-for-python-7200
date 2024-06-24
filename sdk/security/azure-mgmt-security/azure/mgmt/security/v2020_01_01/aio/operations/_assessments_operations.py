# pylint: disable=too-many-lines,too-many-statements
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from io import IOBase
import sys
from typing import Any, AsyncIterable, Callable, Dict, IO, Optional, Type, TypeVar, Union, overload
import urllib.parse

from azure.core.async_paging import AsyncItemPaged, AsyncList
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
from azure.core.tracing.decorator import distributed_trace
from azure.core.tracing.decorator_async import distributed_trace_async
from azure.core.utils import case_insensitive_dict
from azure.mgmt.core.exceptions import ARMErrorFormat

from ... import models as _models
from ..._vendor import _convert_request
from ...operations._assessments_operations import (
    build_create_or_update_request,
    build_delete_request,
    build_get_request,
    build_list_request,
)

if sys.version_info >= (3, 9):
    from collections.abc import MutableMapping
else:
    from typing import MutableMapping  # type: ignore  # pylint: disable=ungrouped-imports
T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class AssessmentsOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.mgmt.security.v2020_01_01.aio.SecurityCenter`'s
        :attr:`assessments` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs) -> None:
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")
        self._api_version = input_args.pop(0) if input_args else kwargs.pop("api_version")

    @distributed_trace
    def list(self, scope: str, **kwargs: Any) -> AsyncIterable["_models.SecurityAssessment"]:
        """Get security assessments on all your scanned resources inside a scope.

        :param scope: Scope of the query, can be subscription
         (/subscriptions/0b06d9ea-afe6-4779-bd59-30e5c2d9d13f) or management group
         (/providers/Microsoft.Management/managementGroups/mgName). Required.
        :type scope: str
        :return: An iterator like instance of either SecurityAssessment or the result of cls(response)
        :rtype:
         ~azure.core.async_paging.AsyncItemPaged[~azure.mgmt.security.v2020_01_01.models.SecurityAssessment]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._api_version or "2020-01-01"))
        cls: ClsType[_models.SecurityAssessmentList] = kwargs.pop("cls", None)

        error_map: MutableMapping[int, Type[HttpResponseError]] = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        def prepare_request(next_link=None):
            if not next_link:

                _request = build_list_request(
                    scope=scope,
                    api_version=api_version,
                    headers=_headers,
                    params=_params,
                )
                _request = _convert_request(_request)
                _request.url = self._client.format_url(_request.url)

            else:
                # make call to next link with the client's api-version
                _parsed_next_link = urllib.parse.urlparse(next_link)
                _next_request_params = case_insensitive_dict(
                    {
                        key: [urllib.parse.quote(v) for v in value]
                        for key, value in urllib.parse.parse_qs(_parsed_next_link.query).items()
                    }
                )
                _next_request_params["api-version"] = self._api_version
                _request = HttpRequest(
                    "GET", urllib.parse.urljoin(next_link, _parsed_next_link.path), params=_next_request_params
                )
                _request = _convert_request(_request)
                _request.url = self._client.format_url(_request.url)
                _request.method = "GET"
            return _request

        async def extract_data(pipeline_response):
            deserialized = self._deserialize("SecurityAssessmentList", pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)  # type: ignore
            return deserialized.next_link or None, AsyncList(list_of_elem)

        async def get_next(next_link=None):
            _request = prepare_request(next_link)

            _stream = False
            pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
                _request, stream=_stream, **kwargs
            )
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response, error_format=ARMErrorFormat)

            return pipeline_response

        return AsyncItemPaged(get_next, extract_data)

    @distributed_trace_async
    async def get(
        self,
        resource_id: str,
        assessment_name: str,
        expand: Optional[Union[str, _models.ExpandEnum]] = None,
        **kwargs: Any
    ) -> _models.SecurityAssessment:
        """Get a security assessment on your scanned resource.

        :param resource_id: The identifier of the resource. Required.
        :type resource_id: str
        :param assessment_name: The Assessment Key - Unique key for the assessment type. Required.
        :type assessment_name: str
        :param expand: OData expand. Optional. Known values are: "links" and "metadata". Default value
         is None.
        :type expand: str or ~azure.mgmt.security.v2020_01_01.models.ExpandEnum
        :return: SecurityAssessment or the result of cls(response)
        :rtype: ~azure.mgmt.security.v2020_01_01.models.SecurityAssessment
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map: MutableMapping[int, Type[HttpResponseError]] = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._api_version or "2020-01-01"))
        cls: ClsType[_models.SecurityAssessment] = kwargs.pop("cls", None)

        _request = build_get_request(
            resource_id=resource_id,
            assessment_name=assessment_name,
            expand=expand,
            api_version=api_version,
            headers=_headers,
            params=_params,
        )
        _request = _convert_request(_request)
        _request.url = self._client.format_url(_request.url)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize("SecurityAssessment", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    @overload
    async def create_or_update(
        self,
        resource_id: str,
        assessment_name: str,
        assessment: _models.SecurityAssessment,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.SecurityAssessment:
        """Create a security assessment on your resource. An assessment metadata that describes this
        assessment must be predefined with the same name before inserting the assessment result.

        :param resource_id: The identifier of the resource. Required.
        :type resource_id: str
        :param assessment_name: The Assessment Key - Unique key for the assessment type. Required.
        :type assessment_name: str
        :param assessment: Calculated assessment on a pre-defined assessment metadata. Required.
        :type assessment: ~azure.mgmt.security.v2020_01_01.models.SecurityAssessment
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: SecurityAssessment or the result of cls(response)
        :rtype: ~azure.mgmt.security.v2020_01_01.models.SecurityAssessment
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def create_or_update(
        self,
        resource_id: str,
        assessment_name: str,
        assessment: IO[bytes],
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.SecurityAssessment:
        """Create a security assessment on your resource. An assessment metadata that describes this
        assessment must be predefined with the same name before inserting the assessment result.

        :param resource_id: The identifier of the resource. Required.
        :type resource_id: str
        :param assessment_name: The Assessment Key - Unique key for the assessment type. Required.
        :type assessment_name: str
        :param assessment: Calculated assessment on a pre-defined assessment metadata. Required.
        :type assessment: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: SecurityAssessment or the result of cls(response)
        :rtype: ~azure.mgmt.security.v2020_01_01.models.SecurityAssessment
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def create_or_update(
        self,
        resource_id: str,
        assessment_name: str,
        assessment: Union[_models.SecurityAssessment, IO[bytes]],
        **kwargs: Any
    ) -> _models.SecurityAssessment:
        """Create a security assessment on your resource. An assessment metadata that describes this
        assessment must be predefined with the same name before inserting the assessment result.

        :param resource_id: The identifier of the resource. Required.
        :type resource_id: str
        :param assessment_name: The Assessment Key - Unique key for the assessment type. Required.
        :type assessment_name: str
        :param assessment: Calculated assessment on a pre-defined assessment metadata. Is either a
         SecurityAssessment type or a IO[bytes] type. Required.
        :type assessment: ~azure.mgmt.security.v2020_01_01.models.SecurityAssessment or IO[bytes]
        :return: SecurityAssessment or the result of cls(response)
        :rtype: ~azure.mgmt.security.v2020_01_01.models.SecurityAssessment
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map: MutableMapping[int, Type[HttpResponseError]] = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._api_version or "2020-01-01"))
        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.SecurityAssessment] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(assessment, (IOBase, bytes)):
            _content = assessment
        else:
            _json = self._serialize.body(assessment, "SecurityAssessment")

        _request = build_create_or_update_request(
            resource_id=resource_id,
            assessment_name=assessment_name,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            content=_content,
            headers=_headers,
            params=_params,
        )
        _request = _convert_request(_request)
        _request.url = self._client.format_url(_request.url)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200, 201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        if response.status_code == 200:
            deserialized = self._deserialize("SecurityAssessment", pipeline_response)

        if response.status_code == 201:
            deserialized = self._deserialize("SecurityAssessment", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    @distributed_trace_async
    async def delete(  # pylint: disable=inconsistent-return-statements
        self, resource_id: str, assessment_name: str, **kwargs: Any
    ) -> None:
        """Delete a security assessment on your resource. An assessment metadata that describes this
        assessment must be predefined with the same name before inserting the assessment result.

        :param resource_id: The identifier of the resource. Required.
        :type resource_id: str
        :param assessment_name: The Assessment Key - Unique key for the assessment type. Required.
        :type assessment_name: str
        :return: None or the result of cls(response)
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map: MutableMapping[int, Type[HttpResponseError]] = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._api_version or "2020-01-01"))
        cls: ClsType[None] = kwargs.pop("cls", None)

        _request = build_delete_request(
            resource_id=resource_id,
            assessment_name=assessment_name,
            api_version=api_version,
            headers=_headers,
            params=_params,
        )
        _request = _convert_request(_request)
        _request.url = self._client.format_url(_request.url)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200, 204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})  # type: ignore
