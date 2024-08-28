# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import pytest
from azure.mgmt.compute.aio import ComputeManagementClient

from devtools_testutils import AzureMgmtRecordedTestCase, RandomNameResourceGroupPreparer
from devtools_testutils.aio import recorded_by_proxy_async

AZURE_LOCATION = "eastus"


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestComputeManagementAvailabilitySetsOperationsAsync(AzureMgmtRecordedTestCase):
    def setup_method(self, method):
        self.client = self.create_mgmt_client(ComputeManagementClient, is_async=True)

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_create_or_update(self, resource_group):
        response = await self.client.availability_sets.create_or_update(
            resource_group_name=resource_group.name,
            availability_set_name="str",
            parameters={
                "location": "str",
                "id": "str",
                "name": "str",
                "platformFaultDomainCount": 0,
                "platformUpdateDomainCount": 0,
                "proximityPlacementGroup": {"id": "str"},
                "scheduledEventsPolicy": {
                    "scheduledEventsAdditionalPublishingTargets": {"eventGridAndResourceGraph": {"enable": bool}},
                    "userInitiatedReboot": {"automaticallyApprove": bool},
                    "userInitiatedRedeploy": {"automaticallyApprove": bool},
                },
                "sku": {"capacity": 0, "name": "str", "tier": "str"},
                "statuses": [
                    {
                        "code": "str",
                        "displayStatus": "str",
                        "level": "str",
                        "message": "str",
                        "time": "2020-02-20 00:00:00",
                    }
                ],
                "tags": {"str": "str"},
                "type": "str",
                "virtualMachines": [{"id": "str"}],
            },
            api_version="2024-07-01",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_update(self, resource_group):
        response = await self.client.availability_sets.update(
            resource_group_name=resource_group.name,
            availability_set_name="str",
            parameters={
                "platformFaultDomainCount": 0,
                "platformUpdateDomainCount": 0,
                "proximityPlacementGroup": {"id": "str"},
                "scheduledEventsPolicy": {
                    "scheduledEventsAdditionalPublishingTargets": {"eventGridAndResourceGraph": {"enable": bool}},
                    "userInitiatedReboot": {"automaticallyApprove": bool},
                    "userInitiatedRedeploy": {"automaticallyApprove": bool},
                },
                "sku": {"capacity": 0, "name": "str", "tier": "str"},
                "statuses": [
                    {
                        "code": "str",
                        "displayStatus": "str",
                        "level": "str",
                        "message": "str",
                        "time": "2020-02-20 00:00:00",
                    }
                ],
                "tags": {"str": "str"},
                "virtualMachines": [{"id": "str"}],
            },
            api_version="2024-07-01",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_delete(self, resource_group):
        response = await self.client.availability_sets.delete(
            resource_group_name=resource_group.name,
            availability_set_name="str",
            api_version="2024-07-01",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_get(self, resource_group):
        response = await self.client.availability_sets.get(
            resource_group_name=resource_group.name,
            availability_set_name="str",
            api_version="2024-07-01",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_list_by_subscription(self, resource_group):
        response = self.client.availability_sets.list_by_subscription(
            api_version="2024-07-01",
        )
        result = [r async for r in response]
        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_list(self, resource_group):
        response = self.client.availability_sets.list(
            resource_group_name=resource_group.name,
            api_version="2024-07-01",
        )
        result = [r async for r in response]
        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_list_available_sizes(self, resource_group):
        response = self.client.availability_sets.list_available_sizes(
            resource_group_name=resource_group.name,
            availability_set_name="str",
            api_version="2024-07-01",
        )
        result = [r async for r in response]
        # please add some check logic here by yourself
        # ...
