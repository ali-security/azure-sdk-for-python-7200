# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, Callable, Dict, Optional, TypeVar, Union, cast

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
from azure.core.polling import AsyncLROPoller, AsyncNoPolling, AsyncPollingMethod
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator_async import distributed_trace_async
from azure.core.utils import case_insensitive_dict
from azure.mgmt.core.exceptions import ARMErrorFormat
from azure.mgmt.core.polling.async_arm_polling import AsyncARMPolling

from ... import models as _models
from ..._vendor import _convert_request
from ...operations._virtual_machine_scale_set_rolling_upgrades_operations import (
    build_cancel_request,
    build_get_latest_request,
    build_start_extension_upgrade_request,
    build_start_os_upgrade_request,
)

T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class VirtualMachineScaleSetRollingUpgradesOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.mgmt.compute.v2021_07_01.aio.ComputeManagementClient`'s
        :attr:`virtual_machine_scale_set_rolling_upgrades` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs) -> None:
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    async def _cancel_initial(  # pylint: disable=inconsistent-return-statements
        self, resource_group_name: str, vm_scale_set_name: str, **kwargs: Any
    ) -> None:
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop("api_version", _params.pop("api-version", "2021-07-01"))  # type: str
        cls = kwargs.pop("cls", None)  # type: ClsType[None]

        request = build_cancel_request(
            resource_group_name=resource_group_name,
            vm_scale_set_name=vm_scale_set_name,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            template_url=self._cancel_initial.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200, 202]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    _cancel_initial.metadata = {"url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachineScaleSets/{vmScaleSetName}/rollingUpgrades/cancel"}  # type: ignore

    @distributed_trace_async
    async def begin_cancel(
        self, resource_group_name: str, vm_scale_set_name: str, **kwargs: Any
    ) -> AsyncLROPoller[None]:
        """Cancels the current virtual machine scale set rolling upgrade.

        :param resource_group_name: The name of the resource group. Required.
        :type resource_group_name: str
        :param vm_scale_set_name: The name of the VM scale set. Required.
        :type vm_scale_set_name: str
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
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop("api_version", _params.pop("api-version", "2021-07-01"))  # type: str
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        polling = kwargs.pop("polling", True)  # type: Union[bool, AsyncPollingMethod]
        lro_delay = kwargs.pop("polling_interval", self._config.polling_interval)
        cont_token = kwargs.pop("continuation_token", None)  # type: Optional[str]
        if cont_token is None:
            raw_result = await self._cancel_initial(  # type: ignore
                resource_group_name=resource_group_name,
                vm_scale_set_name=vm_scale_set_name,
                api_version=api_version,
                cls=lambda x, y, z: x,
                headers=_headers,
                params=_params,
                **kwargs
            )
        kwargs.pop("error_map", None)

        def get_long_running_output(pipeline_response):  # pylint: disable=inconsistent-return-statements
            if cls:
                return cls(pipeline_response, None, {})

        if polling is True:
            polling_method = cast(AsyncPollingMethod, AsyncARMPolling(lro_delay, **kwargs))  # type: AsyncPollingMethod
        elif polling is False:
            polling_method = cast(AsyncPollingMethod, AsyncNoPolling())
        else:
            polling_method = polling
        if cont_token:
            return AsyncLROPoller.from_continuation_token(
                polling_method=polling_method,
                continuation_token=cont_token,
                client=self._client,
                deserialization_callback=get_long_running_output,
            )
        return AsyncLROPoller(self._client, raw_result, get_long_running_output, polling_method)

    begin_cancel.metadata = {"url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachineScaleSets/{vmScaleSetName}/rollingUpgrades/cancel"}  # type: ignore

    async def _start_os_upgrade_initial(  # pylint: disable=inconsistent-return-statements
        self, resource_group_name: str, vm_scale_set_name: str, **kwargs: Any
    ) -> None:
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop("api_version", _params.pop("api-version", "2021-07-01"))  # type: str
        cls = kwargs.pop("cls", None)  # type: ClsType[None]

        request = build_start_os_upgrade_request(
            resource_group_name=resource_group_name,
            vm_scale_set_name=vm_scale_set_name,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            template_url=self._start_os_upgrade_initial.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200, 202]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    _start_os_upgrade_initial.metadata = {"url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachineScaleSets/{vmScaleSetName}/osRollingUpgrade"}  # type: ignore

    @distributed_trace_async
    async def begin_start_os_upgrade(
        self, resource_group_name: str, vm_scale_set_name: str, **kwargs: Any
    ) -> AsyncLROPoller[None]:
        """Starts a rolling upgrade to move all virtual machine scale set instances to the latest
        available Platform Image OS version. Instances which are already running the latest available
        OS version are not affected.

        :param resource_group_name: The name of the resource group. Required.
        :type resource_group_name: str
        :param vm_scale_set_name: The name of the VM scale set. Required.
        :type vm_scale_set_name: str
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
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop("api_version", _params.pop("api-version", "2021-07-01"))  # type: str
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        polling = kwargs.pop("polling", True)  # type: Union[bool, AsyncPollingMethod]
        lro_delay = kwargs.pop("polling_interval", self._config.polling_interval)
        cont_token = kwargs.pop("continuation_token", None)  # type: Optional[str]
        if cont_token is None:
            raw_result = await self._start_os_upgrade_initial(  # type: ignore
                resource_group_name=resource_group_name,
                vm_scale_set_name=vm_scale_set_name,
                api_version=api_version,
                cls=lambda x, y, z: x,
                headers=_headers,
                params=_params,
                **kwargs
            )
        kwargs.pop("error_map", None)

        def get_long_running_output(pipeline_response):  # pylint: disable=inconsistent-return-statements
            if cls:
                return cls(pipeline_response, None, {})

        if polling is True:
            polling_method = cast(AsyncPollingMethod, AsyncARMPolling(lro_delay, **kwargs))  # type: AsyncPollingMethod
        elif polling is False:
            polling_method = cast(AsyncPollingMethod, AsyncNoPolling())
        else:
            polling_method = polling
        if cont_token:
            return AsyncLROPoller.from_continuation_token(
                polling_method=polling_method,
                continuation_token=cont_token,
                client=self._client,
                deserialization_callback=get_long_running_output,
            )
        return AsyncLROPoller(self._client, raw_result, get_long_running_output, polling_method)

    begin_start_os_upgrade.metadata = {"url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachineScaleSets/{vmScaleSetName}/osRollingUpgrade"}  # type: ignore

    async def _start_extension_upgrade_initial(  # pylint: disable=inconsistent-return-statements
        self, resource_group_name: str, vm_scale_set_name: str, **kwargs: Any
    ) -> None:
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop("api_version", _params.pop("api-version", "2021-07-01"))  # type: str
        cls = kwargs.pop("cls", None)  # type: ClsType[None]

        request = build_start_extension_upgrade_request(
            resource_group_name=resource_group_name,
            vm_scale_set_name=vm_scale_set_name,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            template_url=self._start_extension_upgrade_initial.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200, 202]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    _start_extension_upgrade_initial.metadata = {"url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachineScaleSets/{vmScaleSetName}/extensionRollingUpgrade"}  # type: ignore

    @distributed_trace_async
    async def begin_start_extension_upgrade(
        self, resource_group_name: str, vm_scale_set_name: str, **kwargs: Any
    ) -> AsyncLROPoller[None]:
        """Starts a rolling upgrade to move all extensions for all virtual machine scale set instances to
        the latest available extension version. Instances which are already running the latest
        extension versions are not affected.

        :param resource_group_name: The name of the resource group. Required.
        :type resource_group_name: str
        :param vm_scale_set_name: The name of the VM scale set. Required.
        :type vm_scale_set_name: str
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
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop("api_version", _params.pop("api-version", "2021-07-01"))  # type: str
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        polling = kwargs.pop("polling", True)  # type: Union[bool, AsyncPollingMethod]
        lro_delay = kwargs.pop("polling_interval", self._config.polling_interval)
        cont_token = kwargs.pop("continuation_token", None)  # type: Optional[str]
        if cont_token is None:
            raw_result = await self._start_extension_upgrade_initial(  # type: ignore
                resource_group_name=resource_group_name,
                vm_scale_set_name=vm_scale_set_name,
                api_version=api_version,
                cls=lambda x, y, z: x,
                headers=_headers,
                params=_params,
                **kwargs
            )
        kwargs.pop("error_map", None)

        def get_long_running_output(pipeline_response):  # pylint: disable=inconsistent-return-statements
            if cls:
                return cls(pipeline_response, None, {})

        if polling is True:
            polling_method = cast(AsyncPollingMethod, AsyncARMPolling(lro_delay, **kwargs))  # type: AsyncPollingMethod
        elif polling is False:
            polling_method = cast(AsyncPollingMethod, AsyncNoPolling())
        else:
            polling_method = polling
        if cont_token:
            return AsyncLROPoller.from_continuation_token(
                polling_method=polling_method,
                continuation_token=cont_token,
                client=self._client,
                deserialization_callback=get_long_running_output,
            )
        return AsyncLROPoller(self._client, raw_result, get_long_running_output, polling_method)

    begin_start_extension_upgrade.metadata = {"url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachineScaleSets/{vmScaleSetName}/extensionRollingUpgrade"}  # type: ignore

    @distributed_trace_async
    async def get_latest(
        self, resource_group_name: str, vm_scale_set_name: str, **kwargs: Any
    ) -> _models.RollingUpgradeStatusInfo:
        """Gets the status of the latest virtual machine scale set rolling upgrade.

        :param resource_group_name: The name of the resource group. Required.
        :type resource_group_name: str
        :param vm_scale_set_name: The name of the VM scale set. Required.
        :type vm_scale_set_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: RollingUpgradeStatusInfo or the result of cls(response)
        :rtype: ~azure.mgmt.compute.v2021_07_01.models.RollingUpgradeStatusInfo
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

        api_version = kwargs.pop("api_version", _params.pop("api-version", "2021-07-01"))  # type: str
        cls = kwargs.pop("cls", None)  # type: ClsType[_models.RollingUpgradeStatusInfo]

        request = build_get_latest_request(
            resource_group_name=resource_group_name,
            vm_scale_set_name=vm_scale_set_name,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            template_url=self.get_latest.metadata["url"],
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

        deserialized = self._deserialize("RollingUpgradeStatusInfo", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_latest.metadata = {"url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachineScaleSets/{vmScaleSetName}/rollingUpgrades/latest"}  # type: ignore
