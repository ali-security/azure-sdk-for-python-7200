# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import sys
from typing import Any, Callable, Dict, Iterable, Optional, TypeVar

from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    ResourceNotModifiedError,
    map_error,
)
from azure.core.paging import ItemPaged
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator import distributed_trace
from azure.core.utils import case_insensitive_dict
from azure.mgmt.core.exceptions import ARMErrorFormat

from .. import models as _models
from .._serialization import Serializer
from .._vendor import _convert_request, _format_url_section

if sys.version_info >= (3, 8):
    from typing import Literal  # pylint: disable=no-name-in-module, ungrouped-imports
else:
    from typing_extensions import Literal  # type: ignore  # pylint: disable=ungrouped-imports
T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False


def build_get_by_billing_account_request(
    billing_account_name: str, billing_role_definition_name: str, **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version = kwargs.pop("api_version", _params.pop("api-version", "2020-05-01"))  # type: Literal["2020-05-01"]
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop(
        "template_url",
        "/providers/Microsoft.Billing/billingAccounts/{billingAccountName}/billingRoleDefinitions/{billingRoleDefinitionName}",
    )  # pylint: disable=line-too-long
    path_format_arguments = {
        "billingAccountName": _SERIALIZER.url("billing_account_name", billing_account_name, "str"),
        "billingRoleDefinitionName": _SERIALIZER.url(
            "billing_role_definition_name", billing_role_definition_name, "str"
        ),
    }

    _url = _format_url_section(_url, **path_format_arguments)

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, params=_params, headers=_headers, **kwargs)


def build_get_by_invoice_section_request(
    billing_account_name: str,
    billing_profile_name: str,
    invoice_section_name: str,
    billing_role_definition_name: str,
    **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version = kwargs.pop("api_version", _params.pop("api-version", "2020-05-01"))  # type: Literal["2020-05-01"]
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop(
        "template_url",
        "/providers/Microsoft.Billing/billingAccounts/{billingAccountName}/billingProfiles/{billingProfileName}/invoiceSections/{invoiceSectionName}/billingRoleDefinitions/{billingRoleDefinitionName}",
    )  # pylint: disable=line-too-long
    path_format_arguments = {
        "billingAccountName": _SERIALIZER.url("billing_account_name", billing_account_name, "str"),
        "billingProfileName": _SERIALIZER.url("billing_profile_name", billing_profile_name, "str"),
        "invoiceSectionName": _SERIALIZER.url("invoice_section_name", invoice_section_name, "str"),
        "billingRoleDefinitionName": _SERIALIZER.url(
            "billing_role_definition_name", billing_role_definition_name, "str"
        ),
    }

    _url = _format_url_section(_url, **path_format_arguments)

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, params=_params, headers=_headers, **kwargs)


def build_get_by_billing_profile_request(
    billing_account_name: str, billing_profile_name: str, billing_role_definition_name: str, **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version = kwargs.pop("api_version", _params.pop("api-version", "2020-05-01"))  # type: Literal["2020-05-01"]
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop(
        "template_url",
        "/providers/Microsoft.Billing/billingAccounts/{billingAccountName}/billingProfiles/{billingProfileName}/billingRoleDefinitions/{billingRoleDefinitionName}",
    )  # pylint: disable=line-too-long
    path_format_arguments = {
        "billingAccountName": _SERIALIZER.url("billing_account_name", billing_account_name, "str"),
        "billingProfileName": _SERIALIZER.url("billing_profile_name", billing_profile_name, "str"),
        "billingRoleDefinitionName": _SERIALIZER.url(
            "billing_role_definition_name", billing_role_definition_name, "str"
        ),
    }

    _url = _format_url_section(_url, **path_format_arguments)

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, params=_params, headers=_headers, **kwargs)


def build_list_by_billing_account_request(billing_account_name: str, **kwargs: Any) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version = kwargs.pop("api_version", _params.pop("api-version", "2020-05-01"))  # type: Literal["2020-05-01"]
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop(
        "template_url", "/providers/Microsoft.Billing/billingAccounts/{billingAccountName}/billingRoleDefinitions"
    )  # pylint: disable=line-too-long
    path_format_arguments = {
        "billingAccountName": _SERIALIZER.url("billing_account_name", billing_account_name, "str"),
    }

    _url = _format_url_section(_url, **path_format_arguments)

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, params=_params, headers=_headers, **kwargs)


def build_list_by_invoice_section_request(
    billing_account_name: str, billing_profile_name: str, invoice_section_name: str, **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version = kwargs.pop("api_version", _params.pop("api-version", "2020-05-01"))  # type: Literal["2020-05-01"]
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop(
        "template_url",
        "/providers/Microsoft.Billing/billingAccounts/{billingAccountName}/billingProfiles/{billingProfileName}/invoiceSections/{invoiceSectionName}/billingRoleDefinitions",
    )  # pylint: disable=line-too-long
    path_format_arguments = {
        "billingAccountName": _SERIALIZER.url("billing_account_name", billing_account_name, "str"),
        "billingProfileName": _SERIALIZER.url("billing_profile_name", billing_profile_name, "str"),
        "invoiceSectionName": _SERIALIZER.url("invoice_section_name", invoice_section_name, "str"),
    }

    _url = _format_url_section(_url, **path_format_arguments)

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, params=_params, headers=_headers, **kwargs)


def build_list_by_billing_profile_request(
    billing_account_name: str, billing_profile_name: str, **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version = kwargs.pop("api_version", _params.pop("api-version", "2020-05-01"))  # type: Literal["2020-05-01"]
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop(
        "template_url",
        "/providers/Microsoft.Billing/billingAccounts/{billingAccountName}/billingProfiles/{billingProfileName}/billingRoleDefinitions",
    )  # pylint: disable=line-too-long
    path_format_arguments = {
        "billingAccountName": _SERIALIZER.url("billing_account_name", billing_account_name, "str"),
        "billingProfileName": _SERIALIZER.url("billing_profile_name", billing_profile_name, "str"),
    }

    _url = _format_url_section(_url, **path_format_arguments)

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, params=_params, headers=_headers, **kwargs)


class BillingRoleDefinitionsOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.mgmt.billing.BillingManagementClient`'s
        :attr:`billing_role_definitions` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs):
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @distributed_trace
    def get_by_billing_account(
        self, billing_account_name: str, billing_role_definition_name: str, **kwargs: Any
    ) -> _models.BillingRoleDefinition:
        """Gets the definition for a role on a billing account. The operation is supported for billing
        accounts with agreement type Microsoft Partner Agreement or Microsoft Customer Agreement.

        :param billing_account_name: The ID that uniquely identifies a billing account. Required.
        :type billing_account_name: str
        :param billing_role_definition_name: The ID that uniquely identifies a role definition.
         Required.
        :type billing_role_definition_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: BillingRoleDefinition or the result of cls(response)
        :rtype: ~azure.mgmt.billing.models.BillingRoleDefinition
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

        api_version = kwargs.pop("api_version", _params.pop("api-version", "2020-05-01"))  # type: Literal["2020-05-01"]
        cls = kwargs.pop("cls", None)  # type: ClsType[_models.BillingRoleDefinition]

        request = build_get_by_billing_account_request(
            billing_account_name=billing_account_name,
            billing_role_definition_name=billing_role_definition_name,
            api_version=api_version,
            template_url=self.get_by_billing_account.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize("BillingRoleDefinition", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_by_billing_account.metadata = {"url": "/providers/Microsoft.Billing/billingAccounts/{billingAccountName}/billingRoleDefinitions/{billingRoleDefinitionName}"}  # type: ignore

    @distributed_trace
    def get_by_invoice_section(
        self,
        billing_account_name: str,
        billing_profile_name: str,
        invoice_section_name: str,
        billing_role_definition_name: str,
        **kwargs: Any
    ) -> _models.BillingRoleDefinition:
        """Gets the definition for a role on an invoice section. The operation is supported only for
        billing accounts with agreement type Microsoft Customer Agreement.

        :param billing_account_name: The ID that uniquely identifies a billing account. Required.
        :type billing_account_name: str
        :param billing_profile_name: The ID that uniquely identifies a billing profile. Required.
        :type billing_profile_name: str
        :param invoice_section_name: The ID that uniquely identifies an invoice section. Required.
        :type invoice_section_name: str
        :param billing_role_definition_name: The ID that uniquely identifies a role definition.
         Required.
        :type billing_role_definition_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: BillingRoleDefinition or the result of cls(response)
        :rtype: ~azure.mgmt.billing.models.BillingRoleDefinition
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

        api_version = kwargs.pop("api_version", _params.pop("api-version", "2020-05-01"))  # type: Literal["2020-05-01"]
        cls = kwargs.pop("cls", None)  # type: ClsType[_models.BillingRoleDefinition]

        request = build_get_by_invoice_section_request(
            billing_account_name=billing_account_name,
            billing_profile_name=billing_profile_name,
            invoice_section_name=invoice_section_name,
            billing_role_definition_name=billing_role_definition_name,
            api_version=api_version,
            template_url=self.get_by_invoice_section.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize("BillingRoleDefinition", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_by_invoice_section.metadata = {"url": "/providers/Microsoft.Billing/billingAccounts/{billingAccountName}/billingProfiles/{billingProfileName}/invoiceSections/{invoiceSectionName}/billingRoleDefinitions/{billingRoleDefinitionName}"}  # type: ignore

    @distributed_trace
    def get_by_billing_profile(
        self, billing_account_name: str, billing_profile_name: str, billing_role_definition_name: str, **kwargs: Any
    ) -> _models.BillingRoleDefinition:
        """Gets the definition for a role on a billing profile. The operation is supported for billing
        accounts with agreement type Microsoft Partner Agreement or Microsoft Customer Agreement.

        :param billing_account_name: The ID that uniquely identifies a billing account. Required.
        :type billing_account_name: str
        :param billing_profile_name: The ID that uniquely identifies a billing profile. Required.
        :type billing_profile_name: str
        :param billing_role_definition_name: The ID that uniquely identifies a role definition.
         Required.
        :type billing_role_definition_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: BillingRoleDefinition or the result of cls(response)
        :rtype: ~azure.mgmt.billing.models.BillingRoleDefinition
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

        api_version = kwargs.pop("api_version", _params.pop("api-version", "2020-05-01"))  # type: Literal["2020-05-01"]
        cls = kwargs.pop("cls", None)  # type: ClsType[_models.BillingRoleDefinition]

        request = build_get_by_billing_profile_request(
            billing_account_name=billing_account_name,
            billing_profile_name=billing_profile_name,
            billing_role_definition_name=billing_role_definition_name,
            api_version=api_version,
            template_url=self.get_by_billing_profile.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize("BillingRoleDefinition", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_by_billing_profile.metadata = {"url": "/providers/Microsoft.Billing/billingAccounts/{billingAccountName}/billingProfiles/{billingProfileName}/billingRoleDefinitions/{billingRoleDefinitionName}"}  # type: ignore

    @distributed_trace
    def list_by_billing_account(
        self, billing_account_name: str, **kwargs: Any
    ) -> Iterable["_models.BillingRoleDefinition"]:
        """Lists the role definitions for a billing account. The operation is supported for billing
        accounts with agreement type Microsoft Partner Agreement or Microsoft Customer Agreement.

        :param billing_account_name: The ID that uniquely identifies a billing account. Required.
        :type billing_account_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either BillingRoleDefinition or the result of
         cls(response)
        :rtype: ~azure.core.paging.ItemPaged[~azure.mgmt.billing.models.BillingRoleDefinition]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop("api_version", _params.pop("api-version", "2020-05-01"))  # type: Literal["2020-05-01"]
        cls = kwargs.pop("cls", None)  # type: ClsType[_models.BillingRoleDefinitionListResult]

        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        def prepare_request(next_link=None):
            if not next_link:

                request = build_list_by_billing_account_request(
                    billing_account_name=billing_account_name,
                    api_version=api_version,
                    template_url=self.list_by_billing_account.metadata["url"],
                    headers=_headers,
                    params=_params,
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)  # type: ignore

            else:
                request = HttpRequest("GET", next_link)
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)  # type: ignore
                request.method = "GET"
            return request

        def extract_data(pipeline_response):
            deserialized = self._deserialize("BillingRoleDefinitionListResult", pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link or None, iter(list_of_elem)

        def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
                request, stream=False, **kwargs
            )
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
                raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

            return pipeline_response

        return ItemPaged(get_next, extract_data)

    list_by_billing_account.metadata = {"url": "/providers/Microsoft.Billing/billingAccounts/{billingAccountName}/billingRoleDefinitions"}  # type: ignore

    @distributed_trace
    def list_by_invoice_section(
        self, billing_account_name: str, billing_profile_name: str, invoice_section_name: str, **kwargs: Any
    ) -> Iterable["_models.BillingRoleDefinition"]:
        """Lists the role definitions for an invoice section. The operation is supported for billing
        accounts with agreement type Microsoft Partner Agreement or Microsoft Customer Agreement.

        :param billing_account_name: The ID that uniquely identifies a billing account. Required.
        :type billing_account_name: str
        :param billing_profile_name: The ID that uniquely identifies a billing profile. Required.
        :type billing_profile_name: str
        :param invoice_section_name: The ID that uniquely identifies an invoice section. Required.
        :type invoice_section_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either BillingRoleDefinition or the result of
         cls(response)
        :rtype: ~azure.core.paging.ItemPaged[~azure.mgmt.billing.models.BillingRoleDefinition]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop("api_version", _params.pop("api-version", "2020-05-01"))  # type: Literal["2020-05-01"]
        cls = kwargs.pop("cls", None)  # type: ClsType[_models.BillingRoleDefinitionListResult]

        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        def prepare_request(next_link=None):
            if not next_link:

                request = build_list_by_invoice_section_request(
                    billing_account_name=billing_account_name,
                    billing_profile_name=billing_profile_name,
                    invoice_section_name=invoice_section_name,
                    api_version=api_version,
                    template_url=self.list_by_invoice_section.metadata["url"],
                    headers=_headers,
                    params=_params,
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)  # type: ignore

            else:
                request = HttpRequest("GET", next_link)
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)  # type: ignore
                request.method = "GET"
            return request

        def extract_data(pipeline_response):
            deserialized = self._deserialize("BillingRoleDefinitionListResult", pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link or None, iter(list_of_elem)

        def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
                request, stream=False, **kwargs
            )
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
                raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

            return pipeline_response

        return ItemPaged(get_next, extract_data)

    list_by_invoice_section.metadata = {"url": "/providers/Microsoft.Billing/billingAccounts/{billingAccountName}/billingProfiles/{billingProfileName}/invoiceSections/{invoiceSectionName}/billingRoleDefinitions"}  # type: ignore

    @distributed_trace
    def list_by_billing_profile(
        self, billing_account_name: str, billing_profile_name: str, **kwargs: Any
    ) -> Iterable["_models.BillingRoleDefinition"]:
        """Lists the role definitions for a billing profile. The operation is supported for billing
        accounts with agreement type Microsoft Partner Agreement or Microsoft Customer Agreement.

        :param billing_account_name: The ID that uniquely identifies a billing account. Required.
        :type billing_account_name: str
        :param billing_profile_name: The ID that uniquely identifies a billing profile. Required.
        :type billing_profile_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either BillingRoleDefinition or the result of
         cls(response)
        :rtype: ~azure.core.paging.ItemPaged[~azure.mgmt.billing.models.BillingRoleDefinition]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop("api_version", _params.pop("api-version", "2020-05-01"))  # type: Literal["2020-05-01"]
        cls = kwargs.pop("cls", None)  # type: ClsType[_models.BillingRoleDefinitionListResult]

        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        def prepare_request(next_link=None):
            if not next_link:

                request = build_list_by_billing_profile_request(
                    billing_account_name=billing_account_name,
                    billing_profile_name=billing_profile_name,
                    api_version=api_version,
                    template_url=self.list_by_billing_profile.metadata["url"],
                    headers=_headers,
                    params=_params,
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)  # type: ignore

            else:
                request = HttpRequest("GET", next_link)
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)  # type: ignore
                request.method = "GET"
            return request

        def extract_data(pipeline_response):
            deserialized = self._deserialize("BillingRoleDefinitionListResult", pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link or None, iter(list_of_elem)

        def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
                request, stream=False, **kwargs
            )
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
                raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

            return pipeline_response

        return ItemPaged(get_next, extract_data)

    list_by_billing_profile.metadata = {"url": "/providers/Microsoft.Billing/billingAccounts/{billingAccountName}/billingProfiles/{billingProfileName}/billingRoleDefinitions"}  # type: ignore
