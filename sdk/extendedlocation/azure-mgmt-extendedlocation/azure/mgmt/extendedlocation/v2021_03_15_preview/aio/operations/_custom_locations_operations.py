# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, AsyncIterable, Callable, Dict, List, Optional, TypeVar, Union, cast

from azure.core.async_paging import AsyncItemPaged, AsyncList
from azure.core.exceptions import ClientAuthenticationError, HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse
from azure.core.polling import AsyncLROPoller, AsyncNoPolling, AsyncPollingMethod
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator import distributed_trace
from azure.core.tracing.decorator_async import distributed_trace_async
from azure.core.utils import case_insensitive_dict
from azure.mgmt.core.exceptions import ARMErrorFormat
from azure.mgmt.core.polling.async_arm_polling import AsyncARMPolling

from ... import models as _models
from ..._vendor import _convert_request
from ...operations._custom_locations_operations import build_create_or_update_request_initial, build_delete_request_initial, build_get_request, build_list_by_resource_group_request, build_list_by_subscription_request, build_list_enabled_resource_types_request, build_list_operations_request, build_update_request
T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]

class CustomLocationsOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.mgmt.extendedlocation.v2021_03_15_preview.aio.CustomLocations`'s
        :attr:`custom_locations` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs) -> None:
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")


    @distributed_trace
    def list_operations(
        self,
        **kwargs: Any
    ) -> AsyncIterable[_models.CustomLocationOperationsList]:
        """Lists all available Custom Locations operations.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either CustomLocationOperationsList or the result of
         cls(response)
        :rtype:
         ~azure.core.async_paging.AsyncItemPaged[~azure.mgmt.extendedlocation.v2021_03_15_preview.models.CustomLocationOperationsList]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop('api_version', _params.pop('api-version', "2021-03-15-preview"))  # type: str
        cls = kwargs.pop('cls', None)  # type: ClsType[_models.CustomLocationOperationsList]

        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}) or {})
        def prepare_request(next_link=None):
            if not next_link:
                
                request = build_list_operations_request(
                    api_version=api_version,
                    template_url=self.list_operations.metadata['url'],
                    headers=_headers,
                    params=_params,
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)  # type: ignore

            else:
                
                request = build_list_operations_request(
                    api_version=api_version,
                    template_url=next_link,
                    headers=_headers,
                    params=_params,
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)  # type: ignore
                request.method = "GET"
            return request

        async def extract_data(pipeline_response):
            deserialized = self._deserialize("CustomLocationOperationsList", pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link or None, AsyncList(list_of_elem)

        async def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = await self._client._pipeline.run(  # pylint: disable=protected-access
                request,
                stream=False,
                **kwargs
            )
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
                raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

            return pipeline_response


        return AsyncItemPaged(
            get_next, extract_data
        )
    list_operations.metadata = {'url': "/providers/Microsoft.ExtendedLocation/operations"}  # type: ignore

    @distributed_trace
    def list_by_subscription(
        self,
        **kwargs: Any
    ) -> AsyncIterable[_models.CustomLocationListResult]:
        """Gets a list of Custom Locations in a subscription.

        Gets a list of Custom Locations in the specified subscription. The operation returns properties
        of each Custom Location.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either CustomLocationListResult or the result of
         cls(response)
        :rtype:
         ~azure.core.async_paging.AsyncItemPaged[~azure.mgmt.extendedlocation.v2021_03_15_preview.models.CustomLocationListResult]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop('api_version', _params.pop('api-version', "2021-03-15-preview"))  # type: str
        cls = kwargs.pop('cls', None)  # type: ClsType[_models.CustomLocationListResult]

        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}) or {})
        def prepare_request(next_link=None):
            if not next_link:
                
                request = build_list_by_subscription_request(
                    subscription_id=self._config.subscription_id,
                    api_version=api_version,
                    template_url=self.list_by_subscription.metadata['url'],
                    headers=_headers,
                    params=_params,
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)  # type: ignore

            else:
                
                request = build_list_by_subscription_request(
                    subscription_id=self._config.subscription_id,
                    api_version=api_version,
                    template_url=next_link,
                    headers=_headers,
                    params=_params,
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)  # type: ignore
                request.method = "GET"
            return request

        async def extract_data(pipeline_response):
            deserialized = self._deserialize("CustomLocationListResult", pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link or None, AsyncList(list_of_elem)

        async def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = await self._client._pipeline.run(  # pylint: disable=protected-access
                request,
                stream=False,
                **kwargs
            )
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
                raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

            return pipeline_response


        return AsyncItemPaged(
            get_next, extract_data
        )
    list_by_subscription.metadata = {'url': "/subscriptions/{subscriptionId}/providers/Microsoft.ExtendedLocation/customLocations"}  # type: ignore

    @distributed_trace
    def list_by_resource_group(
        self,
        resource_group_name: str,
        **kwargs: Any
    ) -> AsyncIterable[_models.CustomLocationListResult]:
        """Gets a list of Custom Locations in the specified subscription and resource group.

        Gets a list of Custom Locations in the specified subscription and resource group. The operation
        returns properties of each Custom Location.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
        :type resource_group_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either CustomLocationListResult or the result of
         cls(response)
        :rtype:
         ~azure.core.async_paging.AsyncItemPaged[~azure.mgmt.extendedlocation.v2021_03_15_preview.models.CustomLocationListResult]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop('api_version', _params.pop('api-version', "2021-03-15-preview"))  # type: str
        cls = kwargs.pop('cls', None)  # type: ClsType[_models.CustomLocationListResult]

        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}) or {})
        def prepare_request(next_link=None):
            if not next_link:
                
                request = build_list_by_resource_group_request(
                    subscription_id=self._config.subscription_id,
                    resource_group_name=resource_group_name,
                    api_version=api_version,
                    template_url=self.list_by_resource_group.metadata['url'],
                    headers=_headers,
                    params=_params,
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)  # type: ignore

            else:
                
                request = build_list_by_resource_group_request(
                    subscription_id=self._config.subscription_id,
                    resource_group_name=resource_group_name,
                    api_version=api_version,
                    template_url=next_link,
                    headers=_headers,
                    params=_params,
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)  # type: ignore
                request.method = "GET"
            return request

        async def extract_data(pipeline_response):
            deserialized = self._deserialize("CustomLocationListResult", pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link or None, AsyncList(list_of_elem)

        async def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = await self._client._pipeline.run(  # pylint: disable=protected-access
                request,
                stream=False,
                **kwargs
            )
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
                raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

            return pipeline_response


        return AsyncItemPaged(
            get_next, extract_data
        )
    list_by_resource_group.metadata = {'url': "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ExtendedLocation/customLocations"}  # type: ignore

    @distributed_trace_async
    async def get(
        self,
        resource_group_name: str,
        resource_name: str,
        **kwargs: Any
    ) -> _models.CustomLocation:
        """Gets a Custom Location.

        Gets the details of the customLocation with a specified resource group and name.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
        :type resource_group_name: str
        :param resource_name: Custom Locations name.
        :type resource_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: CustomLocation, or the result of cls(response)
        :rtype: ~azure.mgmt.extendedlocation.v2021_03_15_preview.models.CustomLocation
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop('api_version', _params.pop('api-version', "2021-03-15-preview"))  # type: str
        cls = kwargs.pop('cls', None)  # type: ClsType[_models.CustomLocation]

        
        request = build_get_request(
            subscription_id=self._config.subscription_id,
            resource_group_name=resource_group_name,
            resource_name=resource_name,
            api_version=api_version,
            template_url=self.get.metadata['url'],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request,
            stream=False,
            **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('CustomLocation', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get.metadata = {'url': "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ExtendedLocation/customLocations/{resourceName}"}  # type: ignore


    async def _create_or_update_initial(
        self,
        resource_group_name: str,
        resource_name: str,
        parameters: _models.CustomLocation,
        **kwargs: Any
    ) -> _models.CustomLocation:
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop('api_version', _params.pop('api-version', "2021-03-15-preview"))  # type: str
        content_type = kwargs.pop('content_type', _headers.pop('Content-Type', "application/json"))  # type: Optional[str]
        cls = kwargs.pop('cls', None)  # type: ClsType[_models.CustomLocation]

        _json = self._serialize.body(parameters, 'CustomLocation')

        request = build_create_or_update_request_initial(
            subscription_id=self._config.subscription_id,
            resource_group_name=resource_group_name,
            resource_name=resource_name,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            template_url=self._create_or_update_initial.metadata['url'],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request,
            stream=False,
            **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200, 201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        if response.status_code == 200:
            deserialized = self._deserialize('CustomLocation', pipeline_response)

        if response.status_code == 201:
            deserialized = self._deserialize('CustomLocation', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    _create_or_update_initial.metadata = {'url': "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ExtendedLocation/customLocations/{resourceName}"}  # type: ignore


    @distributed_trace_async
    async def begin_create_or_update(
        self,
        resource_group_name: str,
        resource_name: str,
        parameters: _models.CustomLocation,
        **kwargs: Any
    ) -> AsyncLROPoller[_models.CustomLocation]:
        """Creates or updates a Custom Location.

        Creates or updates a Custom Location in the specified Subscription and Resource Group.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
        :type resource_group_name: str
        :param resource_name: Custom Locations name.
        :type resource_name: str
        :param parameters: Parameters supplied to create or update a Custom Location.
        :type parameters: ~azure.mgmt.extendedlocation.v2021_03_15_preview.models.CustomLocation
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword str continuation_token: A continuation token to restart a poller from a saved state.
        :keyword polling: By default, your polling method will be AsyncARMPolling. Pass in False for
         this operation to not poll, or pass in your own initialized polling object for a personal
         polling strategy.
        :paramtype polling: bool or ~azure.core.polling.AsyncPollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no
         Retry-After header is present.
        :return: An instance of AsyncLROPoller that returns either CustomLocation or the result of
         cls(response)
        :rtype:
         ~azure.core.polling.AsyncLROPoller[~azure.mgmt.extendedlocation.v2021_03_15_preview.models.CustomLocation]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop('api_version', _params.pop('api-version', "2021-03-15-preview"))  # type: str
        content_type = kwargs.pop('content_type', _headers.pop('Content-Type', "application/json"))  # type: Optional[str]
        cls = kwargs.pop('cls', None)  # type: ClsType[_models.CustomLocation]
        polling = kwargs.pop('polling', True)  # type: Union[bool, AsyncPollingMethod]
        lro_delay = kwargs.pop(
            'polling_interval',
            self._config.polling_interval
        )
        cont_token = kwargs.pop('continuation_token', None)  # type: Optional[str]
        if cont_token is None:
            raw_result = await self._create_or_update_initial(  # type: ignore
                resource_group_name=resource_group_name,
                resource_name=resource_name,
                parameters=parameters,
                api_version=api_version,
                content_type=content_type,
                cls=lambda x,y,z: x,
                headers=_headers,
                params=_params,
                **kwargs
            )
        kwargs.pop('error_map', None)

        def get_long_running_output(pipeline_response):
            deserialized = self._deserialize('CustomLocation', pipeline_response)
            if cls:
                return cls(pipeline_response, deserialized, {})
            return deserialized


        if polling is True:
            polling_method = cast(AsyncPollingMethod, AsyncARMPolling(
                lro_delay,
                lro_options={'final-state-via': 'azure-async-operation'},
                
                **kwargs
        ))  # type: AsyncPollingMethod
        elif polling is False: polling_method = cast(AsyncPollingMethod, AsyncNoPolling())
        else: polling_method = polling
        if cont_token:
            return AsyncLROPoller.from_continuation_token(
                polling_method=polling_method,
                continuation_token=cont_token,
                client=self._client,
                deserialization_callback=get_long_running_output
            )
        return AsyncLROPoller(self._client, raw_result, get_long_running_output, polling_method)

    begin_create_or_update.metadata = {'url': "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ExtendedLocation/customLocations/{resourceName}"}  # type: ignore

    async def _delete_initial(  # pylint: disable=inconsistent-return-statements
        self,
        resource_group_name: str,
        resource_name: str,
        **kwargs: Any
    ) -> None:
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop('api_version', _params.pop('api-version', "2021-03-15-preview"))  # type: str
        cls = kwargs.pop('cls', None)  # type: ClsType[None]

        
        request = build_delete_request_initial(
            subscription_id=self._config.subscription_id,
            resource_group_name=resource_group_name,
            resource_name=resource_name,
            api_version=api_version,
            template_url=self._delete_initial.metadata['url'],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request,
            stream=False,
            **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [202, 204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    _delete_initial.metadata = {'url': "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ExtendedLocation/customLocations/{resourceName}"}  # type: ignore


    @distributed_trace_async
    async def begin_delete(  # pylint: disable=inconsistent-return-statements
        self,
        resource_group_name: str,
        resource_name: str,
        **kwargs: Any
    ) -> AsyncLROPoller[None]:
        """Deletes a Custom Location.

        Deletes the Custom Location with the specified Resource Name, Resource Group, and Subscription
        Id.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
        :type resource_group_name: str
        :param resource_name: Custom Locations name.
        :type resource_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword str continuation_token: A continuation token to restart a poller from a saved state.
        :keyword polling: By default, your polling method will be AsyncARMPolling. Pass in False for
         this operation to not poll, or pass in your own initialized polling object for a personal
         polling strategy.
        :paramtype polling: bool or ~azure.core.polling.AsyncPollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no
         Retry-After header is present.
        :return: An instance of AsyncLROPoller that returns either None or the result of cls(response)
        :rtype: ~azure.core.polling.AsyncLROPoller[None]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop('api_version', _params.pop('api-version', "2021-03-15-preview"))  # type: str
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        polling = kwargs.pop('polling', True)  # type: Union[bool, AsyncPollingMethod]
        lro_delay = kwargs.pop(
            'polling_interval',
            self._config.polling_interval
        )
        cont_token = kwargs.pop('continuation_token', None)  # type: Optional[str]
        if cont_token is None:
            raw_result = await self._delete_initial(  # type: ignore
                resource_group_name=resource_group_name,
                resource_name=resource_name,
                api_version=api_version,
                cls=lambda x,y,z: x,
                headers=_headers,
                params=_params,
                **kwargs
            )
        kwargs.pop('error_map', None)

        def get_long_running_output(pipeline_response):
            if cls:
                return cls(pipeline_response, None, {})


        if polling is True:
            polling_method = cast(AsyncPollingMethod, AsyncARMPolling(
                lro_delay,
                lro_options={'final-state-via': 'azure-async-operation'},
                
                **kwargs
        ))  # type: AsyncPollingMethod
        elif polling is False: polling_method = cast(AsyncPollingMethod, AsyncNoPolling())
        else: polling_method = polling
        if cont_token:
            return AsyncLROPoller.from_continuation_token(
                polling_method=polling_method,
                continuation_token=cont_token,
                client=self._client,
                deserialization_callback=get_long_running_output
            )
        return AsyncLROPoller(self._client, raw_result, get_long_running_output, polling_method)

    begin_delete.metadata = {'url': "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ExtendedLocation/customLocations/{resourceName}"}  # type: ignore

    @distributed_trace_async
    async def update(
        self,
        resource_group_name: str,
        resource_name: str,
        tags: Optional[Dict[str, str]] = None,
        authentication: Optional[_models.CustomLocationPropertiesAuthentication] = None,
        cluster_extension_ids: Optional[List[str]] = None,
        display_name: Optional[str] = None,
        host_resource_id: Optional[str] = None,
        host_type: Optional[Union[str, "_models.HostType"]] = None,
        namespace: Optional[str] = None,
        provisioning_state: Optional[str] = None,
        **kwargs: Any
    ) -> _models.CustomLocation:
        """Updates a Custom Location.

        Updates a Custom Location with the specified Resource Name in the specified Resource Group and
        Subscription.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
        :type resource_group_name: str
        :param resource_name: Custom Locations name.
        :type resource_name: str
        :param tags: Resource tags. Default value is None.
        :type tags: dict[str, str]
        :param authentication: This is optional input that contains the authentication that should be
         used to generate the namespace. Default value is None.
        :type authentication:
         ~azure.mgmt.extendedlocation.v2021_03_15_preview.models.CustomLocationPropertiesAuthentication
        :param cluster_extension_ids: Contains the reference to the add-on that contains charts to
         deploy CRDs and operators. Default value is None.
        :type cluster_extension_ids: list[str]
        :param display_name: Display name for the Custom Locations location. Default value is None.
        :type display_name: str
        :param host_resource_id: Connected Cluster or AKS Cluster. The Custom Locations RP will perform
         a checkAccess API for listAdminCredentials permissions. Default value is None.
        :type host_resource_id: str
        :param host_type: Type of host the Custom Locations is referencing (Kubernetes, etc...).
         Default value is None.
        :type host_type: str or ~azure.mgmt.extendedlocation.v2021_03_15_preview.models.HostType
        :param namespace: Kubernetes namespace that will be created on the specified cluster. Default
         value is None.
        :type namespace: str
        :param provisioning_state: Provisioning State for the Custom Location. Default value is None.
        :type provisioning_state: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: CustomLocation, or the result of cls(response)
        :rtype: ~azure.mgmt.extendedlocation.v2021_03_15_preview.models.CustomLocation
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop('api_version', _params.pop('api-version', "2021-03-15-preview"))  # type: str
        content_type = kwargs.pop('content_type', _headers.pop('Content-Type', "application/json"))  # type: Optional[str]
        cls = kwargs.pop('cls', None)  # type: ClsType[_models.CustomLocation]

        _parameters = _models.PatchableCustomLocations(tags=tags, authentication=authentication, cluster_extension_ids=cluster_extension_ids, display_name=display_name, host_resource_id=host_resource_id, host_type=host_type, namespace=namespace, provisioning_state=provisioning_state)
        _json = self._serialize.body(_parameters, 'PatchableCustomLocations')

        request = build_update_request(
            subscription_id=self._config.subscription_id,
            resource_group_name=resource_group_name,
            resource_name=resource_name,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            template_url=self.update.metadata['url'],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request,
            stream=False,
            **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('CustomLocation', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    update.metadata = {'url': "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ExtendedLocation/customLocations/{resourceName}"}  # type: ignore


    @distributed_trace
    def list_enabled_resource_types(
        self,
        resource_group_name: str,
        resource_name: str,
        **kwargs: Any
    ) -> AsyncIterable[_models.EnabledResourceTypesListResult]:
        """Gets the list of Enabled Resource Types.

        Gets the list of the Enabled Resource Types.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
        :type resource_group_name: str
        :param resource_name: Custom Locations name.
        :type resource_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either EnabledResourceTypesListResult or the result of
         cls(response)
        :rtype:
         ~azure.core.async_paging.AsyncItemPaged[~azure.mgmt.extendedlocation.v2021_03_15_preview.models.EnabledResourceTypesListResult]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop('api_version', _params.pop('api-version', "2021-03-15-preview"))  # type: str
        cls = kwargs.pop('cls', None)  # type: ClsType[_models.EnabledResourceTypesListResult]

        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}) or {})
        def prepare_request(next_link=None):
            if not next_link:
                
                request = build_list_enabled_resource_types_request(
                    subscription_id=self._config.subscription_id,
                    resource_group_name=resource_group_name,
                    resource_name=resource_name,
                    api_version=api_version,
                    template_url=self.list_enabled_resource_types.metadata['url'],
                    headers=_headers,
                    params=_params,
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)  # type: ignore

            else:
                
                request = build_list_enabled_resource_types_request(
                    subscription_id=self._config.subscription_id,
                    resource_group_name=resource_group_name,
                    resource_name=resource_name,
                    api_version=api_version,
                    template_url=next_link,
                    headers=_headers,
                    params=_params,
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)  # type: ignore
                request.method = "GET"
            return request

        async def extract_data(pipeline_response):
            deserialized = self._deserialize("EnabledResourceTypesListResult", pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link or None, AsyncList(list_of_elem)

        async def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = await self._client._pipeline.run(  # pylint: disable=protected-access
                request,
                stream=False,
                **kwargs
            )
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
                raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

            return pipeline_response


        return AsyncItemPaged(
            get_next, extract_data
        )
    list_enabled_resource_types.metadata = {'url': "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ExtendedLocation/customLocations/{resourceName}/enabledResourceTypes"}  # type: ignore
