# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import pytest
from azure.mgmt.netapp.aio import NetAppManagementClient

from devtools_testutils import AzureMgmtRecordedTestCase, RandomNameResourceGroupPreparer
from devtools_testutils.aio import recorded_by_proxy_async

AZURE_LOCATION = "eastus"


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestNetAppManagementBackupPoliciesOperationsAsync(AzureMgmtRecordedTestCase):
    def setup_method(self, method):
        self.client = self.create_mgmt_client(NetAppManagementClient, is_async=True)

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_list(self, resource_group):
        response = self.client.backup_policies.list(
            resource_group_name=resource_group.name,
            account_name="str",
            api_version="2024-03-01",
        )
        result = [r async for r in response]
        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_get(self, resource_group):
        response = await self.client.backup_policies.get(
            resource_group_name=resource_group.name,
            account_name="str",
            backup_policy_name="str",
            api_version="2024-03-01",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_begin_create(self, resource_group):
        response = await (
            await self.client.backup_policies.begin_create(
                resource_group_name=resource_group.name,
                account_name="str",
                backup_policy_name="str",
                body={
                    "location": "str",
                    "backupPolicyId": "str",
                    "dailyBackupsToKeep": 0,
                    "enabled": bool,
                    "etag": "str",
                    "id": "str",
                    "monthlyBackupsToKeep": 0,
                    "name": "str",
                    "provisioningState": "str",
                    "systemData": {
                        "createdAt": "2020-02-20 00:00:00",
                        "createdBy": "str",
                        "createdByType": "str",
                        "lastModifiedAt": "2020-02-20 00:00:00",
                        "lastModifiedBy": "str",
                        "lastModifiedByType": "str",
                    },
                    "tags": {"str": "str"},
                    "type": "str",
                    "volumeBackups": [
                        {"backupsCount": 0, "policyEnabled": bool, "volumeName": "str", "volumeResourceId": "str"}
                    ],
                    "volumesAssigned": 0,
                    "weeklyBackupsToKeep": 0,
                },
                api_version="2024-03-01",
            )
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_begin_update(self, resource_group):
        response = await (
            await self.client.backup_policies.begin_update(
                resource_group_name=resource_group.name,
                account_name="str",
                backup_policy_name="str",
                body={
                    "backupPolicyId": "str",
                    "dailyBackupsToKeep": 0,
                    "enabled": bool,
                    "id": "str",
                    "location": "str",
                    "monthlyBackupsToKeep": 0,
                    "name": "str",
                    "provisioningState": "str",
                    "tags": {"str": "str"},
                    "type": "str",
                    "volumeBackups": [
                        {"backupsCount": 0, "policyEnabled": bool, "volumeName": "str", "volumeResourceId": "str"}
                    ],
                    "volumesAssigned": 0,
                    "weeklyBackupsToKeep": 0,
                },
                api_version="2024-03-01",
            )
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_begin_delete(self, resource_group):
        response = await (
            await self.client.backup_policies.begin_delete(
                resource_group_name=resource_group.name,
                account_name="str",
                backup_policy_name="str",
                api_version="2024-03-01",
            )
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...
