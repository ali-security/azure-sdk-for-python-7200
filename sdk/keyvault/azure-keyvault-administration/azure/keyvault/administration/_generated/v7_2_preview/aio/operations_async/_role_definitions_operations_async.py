# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator (autorest: 3.0.6306, generator: {generator})
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, AsyncIterable, Callable, Dict, Generic, Optional, TypeVar
import warnings

from azure.core.async_paging import AsyncItemPaged, AsyncList
from azure.core.exceptions import ClientAuthenticationError, HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse, HttpRequest

from ... import models as _models

T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]

class RoleDefinitionsOperations:
    """RoleDefinitionsOperations async operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~key_vault_client.models
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

    async def delete(
        self,
        vault_base_url: str,
        scope: str,
        role_definition_name: str,
        **kwargs
    ) -> "_models.RoleDefinition":
        """Deletes a custom role definition.

        :param vault_base_url: The vault name, for example https://myvault.vault.azure.net.
        :type vault_base_url: str
        :param scope: The scope of the role definition to delete. Managed HSM only supports '/'.
        :type scope: str
        :param role_definition_name: The name (GUID) of the role definition to delete.
        :type role_definition_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: RoleDefinition, or the result of cls(response)
        :rtype: ~key_vault_client.models.RoleDefinition
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.RoleDefinition"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "7.2-preview"
        accept = "application/json"

        # Construct URL
        url = self.delete.metadata['url']  # type: ignore
        path_format_arguments = {
            'vaultBaseUrl': self._serialize.url("vault_base_url", vault_base_url, 'str', skip_quote=True),
            'scope': self._serialize.url("scope", scope, 'str', skip_quote=True),
            'roleDefinitionName': self._serialize.url("role_definition_name", role_definition_name, 'str'),
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

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(_models.KeyVaultError, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize('RoleDefinition', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    delete.metadata = {'url': '/{scope}/providers/Microsoft.Authorization/roleDefinitions/{roleDefinitionName}'}  # type: ignore

    async def create_or_update(
        self,
        vault_base_url: str,
        scope: str,
        role_definition_name: str,
        parameters: "_models.RoleDefinitionCreateParameters",
        **kwargs
    ) -> "_models.RoleDefinition":
        """Creates or updates a custom role definition.

        :param vault_base_url: The vault name, for example https://myvault.vault.azure.net.
        :type vault_base_url: str
        :param scope: The scope of the role definition to create or update. Managed HSM only supports
         '/'.
        :type scope: str
        :param role_definition_name: The name of the role definition to create or update. It can be any
         valid GUID.
        :type role_definition_name: str
        :param parameters: Parameters for the role definition.
        :type parameters: ~key_vault_client.models.RoleDefinitionCreateParameters
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: RoleDefinition, or the result of cls(response)
        :rtype: ~key_vault_client.models.RoleDefinition
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.RoleDefinition"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "7.2-preview"
        content_type = kwargs.pop("content_type", "application/json")
        accept = "application/json"

        # Construct URL
        url = self.create_or_update.metadata['url']  # type: ignore
        path_format_arguments = {
            'vaultBaseUrl': self._serialize.url("vault_base_url", vault_base_url, 'str', skip_quote=True),
            'scope': self._serialize.url("scope", scope, 'str', skip_quote=True),
            'roleDefinitionName': self._serialize.url("role_definition_name", role_definition_name, 'str'),
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
        body_content = self._serialize.body(parameters, 'RoleDefinitionCreateParameters')
        body_content_kwargs['content'] = body_content
        request = self._client.put(url, query_parameters, header_parameters, **body_content_kwargs)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(_models.KeyVaultError, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize('RoleDefinition', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    create_or_update.metadata = {'url': '/{scope}/providers/Microsoft.Authorization/roleDefinitions/{roleDefinitionName}'}  # type: ignore

    async def get(
        self,
        vault_base_url: str,
        scope: str,
        role_definition_name: str,
        **kwargs
    ) -> "_models.RoleDefinition":
        """Get the specified role definition.

        :param vault_base_url: The vault name, for example https://myvault.vault.azure.net.
        :type vault_base_url: str
        :param scope: The scope of the role definition to get. Managed HSM only supports '/'.
        :type scope: str
        :param role_definition_name: The name of the role definition to get.
        :type role_definition_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: RoleDefinition, or the result of cls(response)
        :rtype: ~key_vault_client.models.RoleDefinition
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.RoleDefinition"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "7.2-preview"
        accept = "application/json"

        # Construct URL
        url = self.get.metadata['url']  # type: ignore
        path_format_arguments = {
            'vaultBaseUrl': self._serialize.url("vault_base_url", vault_base_url, 'str', skip_quote=True),
            'scope': self._serialize.url("scope", scope, 'str', skip_quote=True),
            'roleDefinitionName': self._serialize.url("role_definition_name", role_definition_name, 'str'),
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
            error = self._deserialize(_models.KeyVaultError, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize('RoleDefinition', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    get.metadata = {'url': '/{scope}/providers/Microsoft.Authorization/roleDefinitions/{roleDefinitionName}'}  # type: ignore

    def list(
        self,
        vault_base_url: str,
        scope: str,
        filter: Optional[str] = None,
        **kwargs
    ) -> AsyncIterable["_models.RoleDefinitionListResult"]:
        """Get all role definitions that are applicable at scope and above.

        :param vault_base_url: The vault name, for example https://myvault.vault.azure.net.
        :type vault_base_url: str
        :param scope: The scope of the role definition.
        :type scope: str
        :param filter: The filter to apply on the operation. Use atScopeAndBelow filter to search below
         the given scope as well.
        :type filter: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either RoleDefinitionListResult or the result of cls(response)
        :rtype: ~azure.core.async_paging.AsyncItemPaged[~key_vault_client.models.RoleDefinitionListResult]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.RoleDefinitionListResult"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "7.2-preview"
        accept = "application/json"

        def prepare_request(next_link=None):
            # Construct headers
            header_parameters = {}  # type: Dict[str, Any]
            header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

            if not next_link:
                # Construct URL
                url = self.list.metadata['url']  # type: ignore
                path_format_arguments = {
                    'vaultBaseUrl': self._serialize.url("vault_base_url", vault_base_url, 'str', skip_quote=True),
                    'scope': self._serialize.url("scope", scope, 'str', skip_quote=True),
                }
                url = self._client.format_url(url, **path_format_arguments)
                # Construct parameters
                query_parameters = {}  # type: Dict[str, Any]
                if filter is not None:
                    query_parameters['$filter'] = self._serialize.query("filter", filter, 'str')
                query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

                request = self._client.get(url, query_parameters, header_parameters)
            else:
                url = next_link
                query_parameters = {}  # type: Dict[str, Any]
                path_format_arguments = {
                    'vaultBaseUrl': self._serialize.url("vault_base_url", vault_base_url, 'str', skip_quote=True),
                    'scope': self._serialize.url("scope", scope, 'str', skip_quote=True),
                }
                url = self._client.format_url(url, **path_format_arguments)
                request = self._client.get(url, query_parameters, header_parameters)
            return request

        async def extract_data(pipeline_response):
            deserialized = self._deserialize('RoleDefinitionListResult', pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link or None, AsyncList(list_of_elem)

        async def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                error = self._deserialize(_models.KeyVaultError, response)
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response, model=error)

            return pipeline_response

        return AsyncItemPaged(
            get_next, extract_data
        )
    list.metadata = {'url': '/{scope}/providers/Microsoft.Authorization/roleDefinitions'}  # type: ignore
