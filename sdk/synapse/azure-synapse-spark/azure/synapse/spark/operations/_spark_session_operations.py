# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import TYPE_CHECKING
import warnings

from azure.core.exceptions import ClientAuthenticationError, HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpRequest, HttpResponse

from .. import models as _models

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Callable, Dict, Generic, Optional, TypeVar

    T = TypeVar('T')
    ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

class SparkSessionOperations(object):
    """SparkSessionOperations operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~azure.synapse.spark.models
    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = _models

    def __init__(self, client, config, serializer, deserializer):
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    def get_spark_sessions(
        self,
        from_parameter=None,  # type: Optional[int]
        size=None,  # type: Optional[int]
        detailed=None,  # type: Optional[bool]
        **kwargs  # type: Any
    ):
        # type: (...) -> "_models.SparkSessionCollection"
        """List all spark sessions which are running under a particular spark pool.

        :param from_parameter: Optional param specifying which index the list should begin from.
        :type from_parameter: int
        :param size: Optional param specifying the size of the returned list.
                     By default it is 20 and that is the maximum.
        :type size: int
        :param detailed: Optional query param specifying whether detailed response is returned beyond
         plain livy.
        :type detailed: bool
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: SparkSessionCollection, or the result of cls(response)
        :rtype: ~azure.synapse.spark.models.SparkSessionCollection
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.SparkSessionCollection"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        accept = "application/json"

        # Construct URL
        url = self.get_spark_sessions.metadata['url']  # type: ignore
        path_format_arguments = {
            'endpoint': self._serialize.url("self._config.endpoint", self._config.endpoint, 'str', skip_quote=True),
            'livyApiVersion': self._serialize.url("self._config.livy_api_version", self._config.livy_api_version, 'str', skip_quote=True),
            'sparkPoolName': self._serialize.url("self._config.spark_pool_name", self._config.spark_pool_name, 'str', skip_quote=True),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        if from_parameter is not None:
            query_parameters['from'] = self._serialize.query("from_parameter", from_parameter, 'int')
        if size is not None:
            query_parameters['size'] = self._serialize.query("size", size, 'int')
        if detailed is not None:
            query_parameters['detailed'] = self._serialize.query("detailed", detailed, 'bool')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        deserialized = self._deserialize('SparkSessionCollection', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    get_spark_sessions.metadata = {'url': '/sessions'}  # type: ignore

    def create_spark_session(
        self,
        spark_session_options,  # type: "_models.SparkSessionOptions"
        detailed=None,  # type: Optional[bool]
        **kwargs  # type: Any
    ):
        # type: (...) -> "_models.SparkSession"
        """Create new spark session.

        :param spark_session_options: Livy compatible batch job request payload.
        :type spark_session_options: ~azure.synapse.spark.models.SparkSessionOptions
        :param detailed: Optional query param specifying whether detailed response is returned beyond
         plain livy.
        :type detailed: bool
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: SparkSession, or the result of cls(response)
        :rtype: ~azure.synapse.spark.models.SparkSession
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.SparkSession"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        content_type = kwargs.pop("content_type", "application/json")
        accept = "application/json"

        # Construct URL
        url = self.create_spark_session.metadata['url']  # type: ignore
        path_format_arguments = {
            'endpoint': self._serialize.url("self._config.endpoint", self._config.endpoint, 'str', skip_quote=True),
            'livyApiVersion': self._serialize.url("self._config.livy_api_version", self._config.livy_api_version, 'str', skip_quote=True),
            'sparkPoolName': self._serialize.url("self._config.spark_pool_name", self._config.spark_pool_name, 'str', skip_quote=True),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        if detailed is not None:
            query_parameters['detailed'] = self._serialize.query("detailed", detailed, 'bool')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(spark_session_options, 'SparkSessionOptions')
        body_content_kwargs['content'] = body_content
        request = self._client.post(url, query_parameters, header_parameters, **body_content_kwargs)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        deserialized = self._deserialize('SparkSession', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    create_spark_session.metadata = {'url': '/sessions'}  # type: ignore

    def get_spark_session(
        self,
        session_id,  # type: int
        detailed=None,  # type: Optional[bool]
        **kwargs  # type: Any
    ):
        # type: (...) -> "_models.SparkSession"
        """Gets a single spark session.

        :param session_id: Identifier for the session.
        :type session_id: int
        :param detailed: Optional query param specifying whether detailed response is returned beyond
         plain livy.
        :type detailed: bool
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: SparkSession, or the result of cls(response)
        :rtype: ~azure.synapse.spark.models.SparkSession
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.SparkSession"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        accept = "application/json"

        # Construct URL
        url = self.get_spark_session.metadata['url']  # type: ignore
        path_format_arguments = {
            'endpoint': self._serialize.url("self._config.endpoint", self._config.endpoint, 'str', skip_quote=True),
            'livyApiVersion': self._serialize.url("self._config.livy_api_version", self._config.livy_api_version, 'str', skip_quote=True),
            'sparkPoolName': self._serialize.url("self._config.spark_pool_name", self._config.spark_pool_name, 'str', skip_quote=True),
            'sessionId': self._serialize.url("session_id", session_id, 'int'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        if detailed is not None:
            query_parameters['detailed'] = self._serialize.query("detailed", detailed, 'bool')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        deserialized = self._deserialize('SparkSession', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    get_spark_session.metadata = {'url': '/sessions/{sessionId}'}  # type: ignore

    def cancel_spark_session(
        self,
        session_id,  # type: int
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Cancels a running spark session.

        :param session_id: Identifier for the session.
        :type session_id: int
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

        # Construct URL
        url = self.cancel_spark_session.metadata['url']  # type: ignore
        path_format_arguments = {
            'endpoint': self._serialize.url("self._config.endpoint", self._config.endpoint, 'str', skip_quote=True),
            'livyApiVersion': self._serialize.url("self._config.livy_api_version", self._config.livy_api_version, 'str', skip_quote=True),
            'sparkPoolName': self._serialize.url("self._config.spark_pool_name", self._config.spark_pool_name, 'str', skip_quote=True),
            'sessionId': self._serialize.url("session_id", session_id, 'int'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]

        request = self._client.delete(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})

    cancel_spark_session.metadata = {'url': '/sessions/{sessionId}'}  # type: ignore

    def reset_spark_session_timeout(
        self,
        session_id,  # type: int
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Sends a keep alive call to the current session to reset the session timeout.

        :param session_id: Identifier for the session.
        :type session_id: int
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

        # Construct URL
        url = self.reset_spark_session_timeout.metadata['url']  # type: ignore
        path_format_arguments = {
            'endpoint': self._serialize.url("self._config.endpoint", self._config.endpoint, 'str', skip_quote=True),
            'livyApiVersion': self._serialize.url("self._config.livy_api_version", self._config.livy_api_version, 'str', skip_quote=True),
            'sparkPoolName': self._serialize.url("self._config.spark_pool_name", self._config.spark_pool_name, 'str', skip_quote=True),
            'sessionId': self._serialize.url("session_id", session_id, 'int'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]

        request = self._client.put(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})

    reset_spark_session_timeout.metadata = {'url': '/sessions/{sessionId}/reset-timeout'}  # type: ignore

    def get_spark_statements(
        self,
        session_id,  # type: int
        **kwargs  # type: Any
    ):
        # type: (...) -> "_models.SparkStatementCollection"
        """Gets a list of statements within a spark session.

        :param session_id: Identifier for the session.
        :type session_id: int
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: SparkStatementCollection, or the result of cls(response)
        :rtype: ~azure.synapse.spark.models.SparkStatementCollection
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.SparkStatementCollection"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        accept = "application/json"

        # Construct URL
        url = self.get_spark_statements.metadata['url']  # type: ignore
        path_format_arguments = {
            'endpoint': self._serialize.url("self._config.endpoint", self._config.endpoint, 'str', skip_quote=True),
            'livyApiVersion': self._serialize.url("self._config.livy_api_version", self._config.livy_api_version, 'str', skip_quote=True),
            'sparkPoolName': self._serialize.url("self._config.spark_pool_name", self._config.spark_pool_name, 'str', skip_quote=True),
            'sessionId': self._serialize.url("session_id", session_id, 'int'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        deserialized = self._deserialize('SparkStatementCollection', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    get_spark_statements.metadata = {'url': '/sessions/{sessionId}/statements'}  # type: ignore

    def create_spark_statement(
        self,
        session_id,  # type: int
        spark_statement_options,  # type: "_models.SparkStatementOptions"
        **kwargs  # type: Any
    ):
        # type: (...) -> "_models.SparkStatement"
        """Create statement within a spark session.

        :param session_id: Identifier for the session.
        :type session_id: int
        :param spark_statement_options: Livy compatible batch job request payload.
        :type spark_statement_options: ~azure.synapse.spark.models.SparkStatementOptions
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: SparkStatement, or the result of cls(response)
        :rtype: ~azure.synapse.spark.models.SparkStatement
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.SparkStatement"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        content_type = kwargs.pop("content_type", "application/json")
        accept = "application/json"

        # Construct URL
        url = self.create_spark_statement.metadata['url']  # type: ignore
        path_format_arguments = {
            'endpoint': self._serialize.url("self._config.endpoint", self._config.endpoint, 'str', skip_quote=True),
            'livyApiVersion': self._serialize.url("self._config.livy_api_version", self._config.livy_api_version, 'str', skip_quote=True),
            'sparkPoolName': self._serialize.url("self._config.spark_pool_name", self._config.spark_pool_name, 'str', skip_quote=True),
            'sessionId': self._serialize.url("session_id", session_id, 'int'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(spark_statement_options, 'SparkStatementOptions')
        body_content_kwargs['content'] = body_content
        request = self._client.post(url, query_parameters, header_parameters, **body_content_kwargs)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        deserialized = self._deserialize('SparkStatement', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    create_spark_statement.metadata = {'url': '/sessions/{sessionId}/statements'}  # type: ignore

    def get_spark_statement(
        self,
        session_id,  # type: int
        statement_id,  # type: int
        **kwargs  # type: Any
    ):
        # type: (...) -> "_models.SparkStatement"
        """Gets a single statement within a spark session.

        :param session_id: Identifier for the session.
        :type session_id: int
        :param statement_id: Identifier for the statement.
        :type statement_id: int
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: SparkStatement, or the result of cls(response)
        :rtype: ~azure.synapse.spark.models.SparkStatement
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.SparkStatement"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        accept = "application/json"

        # Construct URL
        url = self.get_spark_statement.metadata['url']  # type: ignore
        path_format_arguments = {
            'endpoint': self._serialize.url("self._config.endpoint", self._config.endpoint, 'str', skip_quote=True),
            'livyApiVersion': self._serialize.url("self._config.livy_api_version", self._config.livy_api_version, 'str', skip_quote=True),
            'sparkPoolName': self._serialize.url("self._config.spark_pool_name", self._config.spark_pool_name, 'str', skip_quote=True),
            'sessionId': self._serialize.url("session_id", session_id, 'int'),
            'statementId': self._serialize.url("statement_id", statement_id, 'int'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        deserialized = self._deserialize('SparkStatement', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    get_spark_statement.metadata = {'url': '/sessions/{sessionId}/statements/{statementId}'}  # type: ignore

    def cancel_spark_statement(
        self,
        session_id,  # type: int
        statement_id,  # type: int
        **kwargs  # type: Any
    ):
        # type: (...) -> "_models.SparkStatementCancellationResult"
        """Kill a statement within a session.

        :param session_id: Identifier for the session.
        :type session_id: int
        :param statement_id: Identifier for the statement.
        :type statement_id: int
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: SparkStatementCancellationResult, or the result of cls(response)
        :rtype: ~azure.synapse.spark.models.SparkStatementCancellationResult
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.SparkStatementCancellationResult"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        accept = "application/json"

        # Construct URL
        url = self.cancel_spark_statement.metadata['url']  # type: ignore
        path_format_arguments = {
            'endpoint': self._serialize.url("self._config.endpoint", self._config.endpoint, 'str', skip_quote=True),
            'livyApiVersion': self._serialize.url("self._config.livy_api_version", self._config.livy_api_version, 'str', skip_quote=True),
            'sparkPoolName': self._serialize.url("self._config.spark_pool_name", self._config.spark_pool_name, 'str', skip_quote=True),
            'sessionId': self._serialize.url("session_id", session_id, 'int'),
            'statementId': self._serialize.url("statement_id", statement_id, 'int'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        request = self._client.post(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        deserialized = self._deserialize('SparkStatementCancellationResult', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    cancel_spark_statement.metadata = {'url': '/sessions/{sessionId}/statements/{statementId}/cancel'}  # type: ignore
