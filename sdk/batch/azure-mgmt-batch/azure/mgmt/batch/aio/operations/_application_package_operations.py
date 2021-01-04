# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, AsyncIterable, Callable, Dict, Generic, Optional, TypeVar
import warnings

from azure.core.async_paging import AsyncItemPaged, AsyncList
from azure.core.exceptions import ClientAuthenticationError, HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse, HttpRequest
from azure.mgmt.core.exceptions import ARMErrorFormat

from ... import models as _models

T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]

class ApplicationPackageOperations:
    """ApplicationPackageOperations async operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~azure.mgmt.batch.models
    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = _models

    def __init__(self, client, config, serializer, deserializer) -> None:
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    async def activate(
        self,
        resource_group_name: str,
        account_name: str,
        application_name: str,
        version_name: str,
        parameters: "_models.ActivateApplicationPackageParameters",
        **kwargs
    ) -> "_models.ApplicationPackage":
        """Activates the specified application package. This should be done after the
        ``ApplicationPackage`` was created and uploaded. This needs to be done before an
        ``ApplicationPackage`` can be used on Pools or Tasks.

        :param resource_group_name: The name of the resource group that contains the Batch account.
        :type resource_group_name: str
        :param account_name: The name of the Batch account.
        :type account_name: str
        :param application_name: The name of the application. This must be unique within the account.
        :type application_name: str
        :param version_name: The version of the application.
        :type version_name: str
        :param parameters: The parameters for the request.
        :type parameters: ~azure.mgmt.batch.models.ActivateApplicationPackageParameters
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ApplicationPackage, or the result of cls(response)
        :rtype: ~azure.mgmt.batch.models.ApplicationPackage
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.ApplicationPackage"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2020-09-01"
        content_type = kwargs.pop("content_type", "application/json")
        accept = "application/json"

        # Construct URL
        url = self.activate.metadata['url']  # type: ignore
        path_format_arguments = {
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'accountName': self._serialize.url("account_name", account_name, 'str', max_length=24, min_length=3, pattern=r'^[a-zA-Z0-9]+$'),
            'applicationName': self._serialize.url("application_name", application_name, 'str', max_length=64, min_length=1, pattern=r'^[a-zA-Z0-9_-]+$'),
            'versionName': self._serialize.url("version_name", version_name, 'str', max_length=64, min_length=1, pattern=r'^[a-zA-Z0-9_-][a-zA-Z0-9_.-]*$'),
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(parameters, 'ActivateApplicationPackageParameters')
        body_content_kwargs['content'] = body_content
        request = self._client.post(url, query_parameters, header_parameters, **body_content_kwargs)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize('ApplicationPackage', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    activate.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Batch/batchAccounts/{accountName}/applications/{applicationName}/versions/{versionName}/activate'}  # type: ignore

    async def create(
        self,
        resource_group_name: str,
        account_name: str,
        application_name: str,
        version_name: str,
        parameters: Optional["_models.ApplicationPackage"] = None,
        **kwargs
    ) -> "_models.ApplicationPackage":
        """Creates an application package record. The record contains the SAS where the package should be
        uploaded to.  Once it is uploaded the ``ApplicationPackage`` needs to be activated using
        ``ApplicationPackageActive`` before it can be used.

        :param resource_group_name: The name of the resource group that contains the Batch account.
        :type resource_group_name: str
        :param account_name: The name of the Batch account.
        :type account_name: str
        :param application_name: The name of the application. This must be unique within the account.
        :type application_name: str
        :param version_name: The version of the application.
        :type version_name: str
        :param parameters: The parameters for the request.
        :type parameters: ~azure.mgmt.batch.models.ApplicationPackage
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ApplicationPackage, or the result of cls(response)
        :rtype: ~azure.mgmt.batch.models.ApplicationPackage
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.ApplicationPackage"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2020-09-01"
        content_type = kwargs.pop("content_type", "application/json")
        accept = "application/json"

        # Construct URL
        url = self.create.metadata['url']  # type: ignore
        path_format_arguments = {
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'accountName': self._serialize.url("account_name", account_name, 'str', max_length=24, min_length=3, pattern=r'^[a-zA-Z0-9]+$'),
            'applicationName': self._serialize.url("application_name", application_name, 'str', max_length=64, min_length=1, pattern=r'^[a-zA-Z0-9_-]+$'),
            'versionName': self._serialize.url("version_name", version_name, 'str', max_length=64, min_length=1, pattern=r'^[a-zA-Z0-9_-][a-zA-Z0-9_.-]*$'),
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        if parameters is not None:
            body_content = self._serialize.body(parameters, 'ApplicationPackage')
        else:
            body_content = None
        body_content_kwargs['content'] = body_content
        request = self._client.put(url, query_parameters, header_parameters, **body_content_kwargs)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize('ApplicationPackage', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    create.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Batch/batchAccounts/{accountName}/applications/{applicationName}/versions/{versionName}'}  # type: ignore

    async def delete(
        self,
        resource_group_name: str,
        account_name: str,
        application_name: str,
        version_name: str,
        **kwargs
    ) -> None:
        """Deletes an application package record and its associated binary file.

        :param resource_group_name: The name of the resource group that contains the Batch account.
        :type resource_group_name: str
        :param account_name: The name of the Batch account.
        :type account_name: str
        :param application_name: The name of the application. This must be unique within the account.
        :type application_name: str
        :param version_name: The version of the application.
        :type version_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2020-09-01"
        accept = "application/json"

        # Construct URL
        url = self.delete.metadata['url']  # type: ignore
        path_format_arguments = {
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'accountName': self._serialize.url("account_name", account_name, 'str', max_length=24, min_length=3, pattern=r'^[a-zA-Z0-9]+$'),
            'applicationName': self._serialize.url("application_name", application_name, 'str', max_length=64, min_length=1, pattern=r'^[a-zA-Z0-9_-]+$'),
            'versionName': self._serialize.url("version_name", version_name, 'str', max_length=64, min_length=1, pattern=r'^[a-zA-Z0-9_-][a-zA-Z0-9_.-]*$'),
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        request = self._client.delete(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    delete.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Batch/batchAccounts/{accountName}/applications/{applicationName}/versions/{versionName}'}  # type: ignore

    async def get(
        self,
        resource_group_name: str,
        account_name: str,
        application_name: str,
        version_name: str,
        **kwargs
    ) -> "_models.ApplicationPackage":
        """Gets information about the specified application package.

        :param resource_group_name: The name of the resource group that contains the Batch account.
        :type resource_group_name: str
        :param account_name: The name of the Batch account.
        :type account_name: str
        :param application_name: The name of the application. This must be unique within the account.
        :type application_name: str
        :param version_name: The version of the application.
        :type version_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ApplicationPackage, or the result of cls(response)
        :rtype: ~azure.mgmt.batch.models.ApplicationPackage
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.ApplicationPackage"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2020-09-01"
        accept = "application/json"

        # Construct URL
        url = self.get.metadata['url']  # type: ignore
        path_format_arguments = {
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'accountName': self._serialize.url("account_name", account_name, 'str', max_length=24, min_length=3, pattern=r'^[a-zA-Z0-9]+$'),
            'applicationName': self._serialize.url("application_name", application_name, 'str', max_length=64, min_length=1, pattern=r'^[a-zA-Z0-9_-]+$'),
            'versionName': self._serialize.url("version_name", version_name, 'str', max_length=64, min_length=1, pattern=r'^[a-zA-Z0-9_-][a-zA-Z0-9_.-]*$'),
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize('ApplicationPackage', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    get.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Batch/batchAccounts/{accountName}/applications/{applicationName}/versions/{versionName}'}  # type: ignore

    def list(
        self,
        resource_group_name: str,
        account_name: str,
        application_name: str,
        maxresults: Optional[int] = None,
        **kwargs
    ) -> AsyncIterable["_models.ListApplicationPackagesResult"]:
        """Lists all of the application packages in the specified application.

        :param resource_group_name: The name of the resource group that contains the Batch account.
        :type resource_group_name: str
        :param account_name: The name of the Batch account.
        :type account_name: str
        :param application_name: The name of the application. This must be unique within the account.
        :type application_name: str
        :param maxresults: The maximum number of items to return in the response.
        :type maxresults: int
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either ListApplicationPackagesResult or the result of cls(response)
        :rtype: ~azure.core.async_paging.AsyncItemPaged[~azure.mgmt.batch.models.ListApplicationPackagesResult]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.ListApplicationPackagesResult"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2020-09-01"
        accept = "application/json"

        def prepare_request(next_link=None):
            # Construct headers
            header_parameters = {}  # type: Dict[str, Any]
            header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

            if not next_link:
                # Construct URL
                url = self.list.metadata['url']  # type: ignore
                path_format_arguments = {
                    'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
                    'accountName': self._serialize.url("account_name", account_name, 'str', max_length=24, min_length=3, pattern=r'^[a-zA-Z0-9]+$'),
                    'applicationName': self._serialize.url("application_name", application_name, 'str', max_length=64, min_length=1, pattern=r'^[a-zA-Z0-9_-]+$'),
                    'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
                }
                url = self._client.format_url(url, **path_format_arguments)
                # Construct parameters
                query_parameters = {}  # type: Dict[str, Any]
                if maxresults is not None:
                    query_parameters['maxresults'] = self._serialize.query("maxresults", maxresults, 'int')
                query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

                request = self._client.get(url, query_parameters, header_parameters)
            else:
                url = next_link
                query_parameters = {}  # type: Dict[str, Any]
                request = self._client.get(url, query_parameters, header_parameters)
            return request

        async def extract_data(pipeline_response):
            deserialized = self._deserialize('ListApplicationPackagesResult', pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link or None, AsyncList(list_of_elem)

        async def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response, error_format=ARMErrorFormat)

            return pipeline_response

        return AsyncItemPaged(
            get_next, extract_data
        )
    list.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Batch/batchAccounts/{accountName}/applications/{applicationName}/versions'}  # type: ignore
