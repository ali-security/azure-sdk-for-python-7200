# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator (autorest: 3.9.7, generator: @autorest/python@6.9.6)
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from io import IOBase
from typing import Any, AsyncIterable, Callable, Dict, IO, Optional, TypeVar, Union, overload
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

from ... import models as _models
from ..._vendor import _convert_request
from ...operations._indexes_operations import (
    build_analyze_request,
    build_create_or_update_request,
    build_create_request,
    build_delete_request,
    build_get_request,
    build_get_statistics_request,
    build_list_request,
)
from .._vendor import SearchServiceClientMixinABC

T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class IndexesOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~search_service_client.aio.SearchServiceClient`'s
        :attr:`indexes` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs) -> None:
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @overload
    async def create(
        self,
        index: _models.SearchIndex,
        request_options: Optional[_models.RequestOptions] = None,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.SearchIndex:
        """Creates a new search index.

        .. seealso::
           - https://docs.microsoft.com/rest/api/searchservice/Create-Index

        :param index: The definition of the index to create. Required.
        :type index: ~search_service_client.models.SearchIndex
        :param request_options: Parameter group. Default value is None.
        :type request_options: ~search_service_client.models.RequestOptions
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: SearchIndex or the result of cls(response)
        :rtype: ~search_service_client.models.SearchIndex
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def create(
        self,
        index: IO,
        request_options: Optional[_models.RequestOptions] = None,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.SearchIndex:
        """Creates a new search index.

        .. seealso::
           - https://docs.microsoft.com/rest/api/searchservice/Create-Index

        :param index: The definition of the index to create. Required.
        :type index: IO
        :param request_options: Parameter group. Default value is None.
        :type request_options: ~search_service_client.models.RequestOptions
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: SearchIndex or the result of cls(response)
        :rtype: ~search_service_client.models.SearchIndex
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def create(
        self,
        index: Union[_models.SearchIndex, IO],
        request_options: Optional[_models.RequestOptions] = None,
        **kwargs: Any
    ) -> _models.SearchIndex:
        """Creates a new search index.

        .. seealso::
           - https://docs.microsoft.com/rest/api/searchservice/Create-Index

        :param index: The definition of the index to create. Is either a SearchIndex type or a IO type.
         Required.
        :type index: ~search_service_client.models.SearchIndex or IO
        :param request_options: Parameter group. Default value is None.
        :type request_options: ~search_service_client.models.RequestOptions
        :keyword content_type: Body Parameter content-type. Known values are: 'application/json'.
         Default value is None.
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: SearchIndex or the result of cls(response)
        :rtype: ~search_service_client.models.SearchIndex
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

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._config.api_version))
        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.SearchIndex] = kwargs.pop("cls", None)

        _x_ms_client_request_id = None
        if request_options is not None:
            _x_ms_client_request_id = request_options.x_ms_client_request_id
        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(index, (IOBase, bytes)):
            _content = index
        else:
            _json = self._serialize.body(index, "SearchIndex")

        _request = build_create_request(
            x_ms_client_request_id=_x_ms_client_request_id,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            content=_content,
            headers=_headers,
            params=_params,
        )
        _request = _convert_request(_request)
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        _request.url = self._client.format_url(_request.url, **path_format_arguments)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.SearchError, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize("SearchIndex", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    @distributed_trace
    def list(
        self, select: Optional[str] = None, request_options: Optional[_models.RequestOptions] = None, **kwargs: Any
    ) -> AsyncIterable["_models.SearchIndex"]:
        """Lists all indexes available for a search service.

        .. seealso::
           - https://docs.microsoft.com/rest/api/searchservice/List-Indexes

        :param select: Selects which top-level properties of the index definitions to retrieve.
         Specified as a comma-separated list of JSON property names, or '*' for all properties. The
         default is all properties. Default value is None.
        :type select: str
        :param request_options: Parameter group. Default value is None.
        :type request_options: ~search_service_client.models.RequestOptions
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either SearchIndex or the result of cls(response)
        :rtype: ~azure.core.async_paging.AsyncItemPaged[~search_service_client.models.SearchIndex]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._config.api_version))
        cls: ClsType[_models.ListIndexesResult] = kwargs.pop("cls", None)

        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        def prepare_request(next_link=None):
            if not next_link:
                _x_ms_client_request_id = None
                if request_options is not None:
                    _x_ms_client_request_id = request_options.x_ms_client_request_id

                _request = build_list_request(
                    select=select,
                    x_ms_client_request_id=_x_ms_client_request_id,
                    api_version=api_version,
                    headers=_headers,
                    params=_params,
                )
                _request = _convert_request(_request)
                path_format_arguments = {
                    "endpoint": self._serialize.url(
                        "self._config.endpoint", self._config.endpoint, "str", skip_quote=True
                    ),
                }
                _request.url = self._client.format_url(_request.url, **path_format_arguments)

            else:
                # make call to next link with the client's api-version
                _parsed_next_link = urllib.parse.urlparse(next_link)
                _next_request_params = case_insensitive_dict(
                    {
                        key: [urllib.parse.quote(v) for v in value]
                        for key, value in urllib.parse.parse_qs(_parsed_next_link.query).items()
                    }
                )
                _next_request_params["api-version"] = self._config.api_version
                _request = HttpRequest(
                    "GET", urllib.parse.urljoin(next_link, _parsed_next_link.path), params=_next_request_params
                )
                _request = _convert_request(_request)
                path_format_arguments = {
                    "endpoint": self._serialize.url(
                        "self._config.endpoint", self._config.endpoint, "str", skip_quote=True
                    ),
                }
                _request.url = self._client.format_url(_request.url, **path_format_arguments)
                _request.method = "GET"
            return _request

        async def extract_data(pipeline_response):
            deserialized = self._deserialize("ListIndexesResult", pipeline_response)
            list_of_elem = deserialized.indexes
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
                error = self._deserialize.failsafe_deserialize(_models.SearchError, pipeline_response)
                raise HttpResponseError(response=response, model=error)

            return pipeline_response

        return AsyncItemPaged(get_next, extract_data)

    @overload
    async def create_or_update(
        self,
        index_name: str,
        prefer: Union[str, _models.Enum0],
        index: _models.SearchIndex,
        allow_index_downtime: Optional[bool] = None,
        if_match: Optional[str] = None,
        if_none_match: Optional[str] = None,
        request_options: Optional[_models.RequestOptions] = None,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.SearchIndex:
        """Creates a new search index or updates an index if it already exists.

        .. seealso::
           - https://docs.microsoft.com/rest/api/searchservice/Update-Index

        :param index_name: The definition of the index to create or update. Required.
        :type index_name: str
        :param prefer: For HTTP PUT requests, instructs the service to return the created/updated
         resource on success. "return=representation" Required.
        :type prefer: str or ~search_service_client.models.Enum0
        :param index: The definition of the index to create or update. Required.
        :type index: ~search_service_client.models.SearchIndex
        :param allow_index_downtime: Allows new analyzers, tokenizers, token filters, or char filters
         to be added to an index by taking the index offline for at least a few seconds. This
         temporarily causes indexing and query requests to fail. Performance and write availability of
         the index can be impaired for several minutes after the index is updated, or longer for very
         large indexes. Default value is None.
        :type allow_index_downtime: bool
        :param if_match: Defines the If-Match condition. The operation will be performed only if the
         ETag on the server matches this value. Default value is None.
        :type if_match: str
        :param if_none_match: Defines the If-None-Match condition. The operation will be performed only
         if the ETag on the server does not match this value. Default value is None.
        :type if_none_match: str
        :param request_options: Parameter group. Default value is None.
        :type request_options: ~search_service_client.models.RequestOptions
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: SearchIndex or the result of cls(response)
        :rtype: ~search_service_client.models.SearchIndex
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def create_or_update(
        self,
        index_name: str,
        prefer: Union[str, _models.Enum0],
        index: IO,
        allow_index_downtime: Optional[bool] = None,
        if_match: Optional[str] = None,
        if_none_match: Optional[str] = None,
        request_options: Optional[_models.RequestOptions] = None,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.SearchIndex:
        """Creates a new search index or updates an index if it already exists.

        .. seealso::
           - https://docs.microsoft.com/rest/api/searchservice/Update-Index

        :param index_name: The definition of the index to create or update. Required.
        :type index_name: str
        :param prefer: For HTTP PUT requests, instructs the service to return the created/updated
         resource on success. "return=representation" Required.
        :type prefer: str or ~search_service_client.models.Enum0
        :param index: The definition of the index to create or update. Required.
        :type index: IO
        :param allow_index_downtime: Allows new analyzers, tokenizers, token filters, or char filters
         to be added to an index by taking the index offline for at least a few seconds. This
         temporarily causes indexing and query requests to fail. Performance and write availability of
         the index can be impaired for several minutes after the index is updated, or longer for very
         large indexes. Default value is None.
        :type allow_index_downtime: bool
        :param if_match: Defines the If-Match condition. The operation will be performed only if the
         ETag on the server matches this value. Default value is None.
        :type if_match: str
        :param if_none_match: Defines the If-None-Match condition. The operation will be performed only
         if the ETag on the server does not match this value. Default value is None.
        :type if_none_match: str
        :param request_options: Parameter group. Default value is None.
        :type request_options: ~search_service_client.models.RequestOptions
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: SearchIndex or the result of cls(response)
        :rtype: ~search_service_client.models.SearchIndex
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def create_or_update(
        self,
        index_name: str,
        prefer: Union[str, _models.Enum0],
        index: Union[_models.SearchIndex, IO],
        allow_index_downtime: Optional[bool] = None,
        if_match: Optional[str] = None,
        if_none_match: Optional[str] = None,
        request_options: Optional[_models.RequestOptions] = None,
        **kwargs: Any
    ) -> _models.SearchIndex:
        """Creates a new search index or updates an index if it already exists.

        .. seealso::
           - https://docs.microsoft.com/rest/api/searchservice/Update-Index

        :param index_name: The definition of the index to create or update. Required.
        :type index_name: str
        :param prefer: For HTTP PUT requests, instructs the service to return the created/updated
         resource on success. "return=representation" Required.
        :type prefer: str or ~search_service_client.models.Enum0
        :param index: The definition of the index to create or update. Is either a SearchIndex type or
         a IO type. Required.
        :type index: ~search_service_client.models.SearchIndex or IO
        :param allow_index_downtime: Allows new analyzers, tokenizers, token filters, or char filters
         to be added to an index by taking the index offline for at least a few seconds. This
         temporarily causes indexing and query requests to fail. Performance and write availability of
         the index can be impaired for several minutes after the index is updated, or longer for very
         large indexes. Default value is None.
        :type allow_index_downtime: bool
        :param if_match: Defines the If-Match condition. The operation will be performed only if the
         ETag on the server matches this value. Default value is None.
        :type if_match: str
        :param if_none_match: Defines the If-None-Match condition. The operation will be performed only
         if the ETag on the server does not match this value. Default value is None.
        :type if_none_match: str
        :param request_options: Parameter group. Default value is None.
        :type request_options: ~search_service_client.models.RequestOptions
        :keyword content_type: Body Parameter content-type. Known values are: 'application/json'.
         Default value is None.
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: SearchIndex or the result of cls(response)
        :rtype: ~search_service_client.models.SearchIndex
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

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._config.api_version))
        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.SearchIndex] = kwargs.pop("cls", None)

        _x_ms_client_request_id = None
        if request_options is not None:
            _x_ms_client_request_id = request_options.x_ms_client_request_id
        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(index, (IOBase, bytes)):
            _content = index
        else:
            _json = self._serialize.body(index, "SearchIndex")

        _request = build_create_or_update_request(
            index_name=index_name,
            prefer=prefer,
            allow_index_downtime=allow_index_downtime,
            x_ms_client_request_id=_x_ms_client_request_id,
            if_match=if_match,
            if_none_match=if_none_match,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            content=_content,
            headers=_headers,
            params=_params,
        )
        _request = _convert_request(_request)
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        _request.url = self._client.format_url(_request.url, **path_format_arguments)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200, 201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.SearchError, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        if response.status_code == 200:
            deserialized = self._deserialize("SearchIndex", pipeline_response)

        if response.status_code == 201:
            deserialized = self._deserialize("SearchIndex", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    @distributed_trace_async
    async def delete(  # pylint: disable=inconsistent-return-statements
        self,
        index_name: str,
        if_match: Optional[str] = None,
        if_none_match: Optional[str] = None,
        request_options: Optional[_models.RequestOptions] = None,
        **kwargs: Any
    ) -> None:
        """Deletes a search index and all the documents it contains. This operation is permanent, with no
        recovery option. Make sure you have a master copy of your index definition, data ingestion
        code, and a backup of the primary data source in case you need to re-build the index.

        .. seealso::
           - https://docs.microsoft.com/rest/api/searchservice/Delete-Index

        :param index_name: The name of the index to delete. Required.
        :type index_name: str
        :param if_match: Defines the If-Match condition. The operation will be performed only if the
         ETag on the server matches this value. Default value is None.
        :type if_match: str
        :param if_none_match: Defines the If-None-Match condition. The operation will be performed only
         if the ETag on the server does not match this value. Default value is None.
        :type if_none_match: str
        :param request_options: Parameter group. Default value is None.
        :type request_options: ~search_service_client.models.RequestOptions
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
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

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._config.api_version))
        cls: ClsType[None] = kwargs.pop("cls", None)

        _x_ms_client_request_id = None
        if request_options is not None:
            _x_ms_client_request_id = request_options.x_ms_client_request_id

        _request = build_delete_request(
            index_name=index_name,
            x_ms_client_request_id=_x_ms_client_request_id,
            if_match=if_match,
            if_none_match=if_none_match,
            api_version=api_version,
            headers=_headers,
            params=_params,
        )
        _request = _convert_request(_request)
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        _request.url = self._client.format_url(_request.url, **path_format_arguments)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [204, 404]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.SearchError, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        if cls:
            return cls(pipeline_response, None, {})  # type: ignore

    @distributed_trace_async
    async def get(
        self, index_name: str, request_options: Optional[_models.RequestOptions] = None, **kwargs: Any
    ) -> _models.SearchIndex:
        """Retrieves an index definition.

        .. seealso::
           - https://docs.microsoft.com/rest/api/searchservice/Get-Index

        :param index_name: The name of the index to retrieve. Required.
        :type index_name: str
        :param request_options: Parameter group. Default value is None.
        :type request_options: ~search_service_client.models.RequestOptions
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: SearchIndex or the result of cls(response)
        :rtype: ~search_service_client.models.SearchIndex
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

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._config.api_version))
        cls: ClsType[_models.SearchIndex] = kwargs.pop("cls", None)

        _x_ms_client_request_id = None
        if request_options is not None:
            _x_ms_client_request_id = request_options.x_ms_client_request_id

        _request = build_get_request(
            index_name=index_name,
            x_ms_client_request_id=_x_ms_client_request_id,
            api_version=api_version,
            headers=_headers,
            params=_params,
        )
        _request = _convert_request(_request)
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        _request.url = self._client.format_url(_request.url, **path_format_arguments)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.SearchError, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize("SearchIndex", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    @distributed_trace_async
    async def get_statistics(
        self, index_name: str, request_options: Optional[_models.RequestOptions] = None, **kwargs: Any
    ) -> _models.GetIndexStatisticsResult:
        """Returns statistics for the given index, including a document count and storage usage.

        .. seealso::
           - https://docs.microsoft.com/rest/api/searchservice/Get-Index-Statistics

        :param index_name: The name of the index for which to retrieve statistics. Required.
        :type index_name: str
        :param request_options: Parameter group. Default value is None.
        :type request_options: ~search_service_client.models.RequestOptions
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: GetIndexStatisticsResult or the result of cls(response)
        :rtype: ~search_service_client.models.GetIndexStatisticsResult
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

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._config.api_version))
        cls: ClsType[_models.GetIndexStatisticsResult] = kwargs.pop("cls", None)

        _x_ms_client_request_id = None
        if request_options is not None:
            _x_ms_client_request_id = request_options.x_ms_client_request_id

        _request = build_get_statistics_request(
            index_name=index_name,
            x_ms_client_request_id=_x_ms_client_request_id,
            api_version=api_version,
            headers=_headers,
            params=_params,
        )
        _request = _convert_request(_request)
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        _request.url = self._client.format_url(_request.url, **path_format_arguments)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.SearchError, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize("GetIndexStatisticsResult", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    @overload
    async def analyze(
        self,
        index_name: str,
        request: _models.AnalyzeRequest,
        request_options: Optional[_models.RequestOptions] = None,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.AnalyzeResult:
        """Shows how an analyzer breaks text into tokens.

        .. seealso::
           - https://docs.microsoft.com/rest/api/searchservice/test-analyzer

        :param index_name: The name of the index for which to test an analyzer. Required.
        :type index_name: str
        :param request: The text and analyzer or analysis components to test. Required.
        :type request: ~search_service_client.models.AnalyzeRequest
        :param request_options: Parameter group. Default value is None.
        :type request_options: ~search_service_client.models.RequestOptions
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: AnalyzeResult or the result of cls(response)
        :rtype: ~search_service_client.models.AnalyzeResult
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def analyze(
        self,
        index_name: str,
        request: IO,
        request_options: Optional[_models.RequestOptions] = None,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.AnalyzeResult:
        """Shows how an analyzer breaks text into tokens.

        .. seealso::
           - https://docs.microsoft.com/rest/api/searchservice/test-analyzer

        :param index_name: The name of the index for which to test an analyzer. Required.
        :type index_name: str
        :param request: The text and analyzer or analysis components to test. Required.
        :type request: IO
        :param request_options: Parameter group. Default value is None.
        :type request_options: ~search_service_client.models.RequestOptions
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: AnalyzeResult or the result of cls(response)
        :rtype: ~search_service_client.models.AnalyzeResult
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def analyze(
        self,
        index_name: str,
        request: Union[_models.AnalyzeRequest, IO],
        request_options: Optional[_models.RequestOptions] = None,
        **kwargs: Any
    ) -> _models.AnalyzeResult:
        """Shows how an analyzer breaks text into tokens.

        .. seealso::
           - https://docs.microsoft.com/rest/api/searchservice/test-analyzer

        :param index_name: The name of the index for which to test an analyzer. Required.
        :type index_name: str
        :param request: The text and analyzer or analysis components to test. Is either a
         AnalyzeRequest type or a IO type. Required.
        :type request: ~search_service_client.models.AnalyzeRequest or IO
        :param request_options: Parameter group. Default value is None.
        :type request_options: ~search_service_client.models.RequestOptions
        :keyword content_type: Body Parameter content-type. Known values are: 'application/json'.
         Default value is None.
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: AnalyzeResult or the result of cls(response)
        :rtype: ~search_service_client.models.AnalyzeResult
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

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._config.api_version))
        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.AnalyzeResult] = kwargs.pop("cls", None)

        _x_ms_client_request_id = None
        if request_options is not None:
            _x_ms_client_request_id = request_options.x_ms_client_request_id
        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(request, (IOBase, bytes)):
            _content = request
        else:
            _json = self._serialize.body(request, "AnalyzeRequest")

        _request = build_analyze_request(
            index_name=index_name,
            x_ms_client_request_id=_x_ms_client_request_id,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            content=_content,
            headers=_headers,
            params=_params,
        )
        _request = _convert_request(_request)
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        _request.url = self._client.format_url(_request.url, **path_format_arguments)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.SearchError, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize("AnalyzeResult", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore
