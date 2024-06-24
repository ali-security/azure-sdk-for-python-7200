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
from ...operations._blob_services_operations import (
    build_get_service_properties_request,
    build_list_request,
    build_set_service_properties_request,
)

if sys.version_info >= (3, 9):
    from collections.abc import MutableMapping
else:
    from typing import MutableMapping  # type: ignore  # pylint: disable=ungrouped-imports
T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class BlobServicesOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.mgmt.storage.v2019_06_01.aio.StorageManagementClient`'s
        :attr:`blob_services` attribute.
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
    def list(
        self, resource_group_name: str, account_name: str, **kwargs: Any
    ) -> AsyncIterable["_models.BlobServiceProperties"]:
        """List blob services of storage account. It returns a collection of one object named default.

        :param resource_group_name: The name of the resource group within the user's subscription. The
         name is case insensitive. Required.
        :type resource_group_name: str
        :param account_name: The name of the storage account within the specified resource group.
         Storage account names must be between 3 and 24 characters in length and use numbers and
         lower-case letters only. Required.
        :type account_name: str
        :return: An iterator like instance of either BlobServiceProperties or the result of
         cls(response)
        :rtype:
         ~azure.core.async_paging.AsyncItemPaged[~azure.mgmt.storage.v2019_06_01.models.BlobServiceProperties]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._api_version or "2019-06-01"))
        cls: ClsType[_models.BlobServiceItems] = kwargs.pop("cls", None)

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
                    resource_group_name=resource_group_name,
                    account_name=account_name,
                    subscription_id=self._config.subscription_id,
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
            deserialized = self._deserialize("BlobServiceItems", pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)  # type: ignore
            return None, AsyncList(list_of_elem)

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

    @overload
    async def set_service_properties(
        self,
        resource_group_name: str,
        account_name: str,
        blob_services_name: Union[str, _models.Enum27],
        parameters: _models.BlobServiceProperties,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.BlobServiceProperties:
        """Sets the properties of a storage account’s Blob service, including properties for Storage
        Analytics and CORS (Cross-Origin Resource Sharing) rules.

        :param resource_group_name: The name of the resource group within the user's subscription. The
         name is case insensitive. Required.
        :type resource_group_name: str
        :param account_name: The name of the storage account within the specified resource group.
         Storage account names must be between 3 and 24 characters in length and use numbers and
         lower-case letters only. Required.
        :type account_name: str
        :param blob_services_name: The name of the blob Service within the specified storage account.
         Blob Service Name must be 'default'. "default" Required.
        :type blob_services_name: str or ~azure.mgmt.storage.v2019_06_01.models.Enum27
        :param parameters: The properties of a storage account’s Blob service, including properties for
         Storage Analytics and CORS (Cross-Origin Resource Sharing) rules. Required.
        :type parameters: ~azure.mgmt.storage.v2019_06_01.models.BlobServiceProperties
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: BlobServiceProperties or the result of cls(response)
        :rtype: ~azure.mgmt.storage.v2019_06_01.models.BlobServiceProperties
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def set_service_properties(
        self,
        resource_group_name: str,
        account_name: str,
        blob_services_name: Union[str, _models.Enum27],
        parameters: IO[bytes],
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.BlobServiceProperties:
        """Sets the properties of a storage account’s Blob service, including properties for Storage
        Analytics and CORS (Cross-Origin Resource Sharing) rules.

        :param resource_group_name: The name of the resource group within the user's subscription. The
         name is case insensitive. Required.
        :type resource_group_name: str
        :param account_name: The name of the storage account within the specified resource group.
         Storage account names must be between 3 and 24 characters in length and use numbers and
         lower-case letters only. Required.
        :type account_name: str
        :param blob_services_name: The name of the blob Service within the specified storage account.
         Blob Service Name must be 'default'. "default" Required.
        :type blob_services_name: str or ~azure.mgmt.storage.v2019_06_01.models.Enum27
        :param parameters: The properties of a storage account’s Blob service, including properties for
         Storage Analytics and CORS (Cross-Origin Resource Sharing) rules. Required.
        :type parameters: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: BlobServiceProperties or the result of cls(response)
        :rtype: ~azure.mgmt.storage.v2019_06_01.models.BlobServiceProperties
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def set_service_properties(
        self,
        resource_group_name: str,
        account_name: str,
        blob_services_name: Union[str, _models.Enum27],
        parameters: Union[_models.BlobServiceProperties, IO[bytes]],
        **kwargs: Any
    ) -> _models.BlobServiceProperties:
        """Sets the properties of a storage account’s Blob service, including properties for Storage
        Analytics and CORS (Cross-Origin Resource Sharing) rules.

        :param resource_group_name: The name of the resource group within the user's subscription. The
         name is case insensitive. Required.
        :type resource_group_name: str
        :param account_name: The name of the storage account within the specified resource group.
         Storage account names must be between 3 and 24 characters in length and use numbers and
         lower-case letters only. Required.
        :type account_name: str
        :param blob_services_name: The name of the blob Service within the specified storage account.
         Blob Service Name must be 'default'. "default" Required.
        :type blob_services_name: str or ~azure.mgmt.storage.v2019_06_01.models.Enum27
        :param parameters: The properties of a storage account’s Blob service, including properties for
         Storage Analytics and CORS (Cross-Origin Resource Sharing) rules. Is either a
         BlobServiceProperties type or a IO[bytes] type. Required.
        :type parameters: ~azure.mgmt.storage.v2019_06_01.models.BlobServiceProperties or IO[bytes]
        :return: BlobServiceProperties or the result of cls(response)
        :rtype: ~azure.mgmt.storage.v2019_06_01.models.BlobServiceProperties
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

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._api_version or "2019-06-01"))
        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.BlobServiceProperties] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(parameters, (IOBase, bytes)):
            _content = parameters
        else:
            _json = self._serialize.body(parameters, "BlobServiceProperties")

        _request = build_set_service_properties_request(
            resource_group_name=resource_group_name,
            account_name=account_name,
            blob_services_name=blob_services_name,
            subscription_id=self._config.subscription_id,
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

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize("BlobServiceProperties", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    @distributed_trace_async
    async def get_service_properties(
        self, resource_group_name: str, account_name: str, blob_services_name: Union[str, _models.Enum27], **kwargs: Any
    ) -> _models.BlobServiceProperties:
        """Gets the properties of a storage account’s Blob service, including properties for Storage
        Analytics and CORS (Cross-Origin Resource Sharing) rules.

        :param resource_group_name: The name of the resource group within the user's subscription. The
         name is case insensitive. Required.
        :type resource_group_name: str
        :param account_name: The name of the storage account within the specified resource group.
         Storage account names must be between 3 and 24 characters in length and use numbers and
         lower-case letters only. Required.
        :type account_name: str
        :param blob_services_name: The name of the blob Service within the specified storage account.
         Blob Service Name must be 'default'. "default" Required.
        :type blob_services_name: str or ~azure.mgmt.storage.v2019_06_01.models.Enum27
        :return: BlobServiceProperties or the result of cls(response)
        :rtype: ~azure.mgmt.storage.v2019_06_01.models.BlobServiceProperties
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

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._api_version or "2019-06-01"))
        cls: ClsType[_models.BlobServiceProperties] = kwargs.pop("cls", None)

        _request = build_get_service_properties_request(
            resource_group_name=resource_group_name,
            account_name=account_name,
            blob_services_name=blob_services_name,
            subscription_id=self._config.subscription_id,
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

        deserialized = self._deserialize("BlobServiceProperties", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore
