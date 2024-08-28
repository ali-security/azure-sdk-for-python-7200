# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import pytest
from azure.mgmt.azurestackhci import AzureStackHCIClient

from devtools_testutils import AzureMgmtRecordedTestCase, RandomNameResourceGroupPreparer, recorded_by_proxy

AZURE_LOCATION = "eastus"


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestAzureStackHCIUpdateSummariesOperations(AzureMgmtRecordedTestCase):
    def setup_method(self, method):
        self.client = self.create_mgmt_client(AzureStackHCIClient)

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_list(self, resource_group):
        response = self.client.update_summaries.list(
            resource_group_name=resource_group.name,
            cluster_name="str",
            api_version="2024-04-01",
        )
        result = [r for r in response]
        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_begin_delete(self, resource_group):
        response = self.client.update_summaries.begin_delete(
            resource_group_name=resource_group.name,
            cluster_name="str",
            api_version="2024-04-01",
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_put(self, resource_group):
        response = self.client.update_summaries.put(
            resource_group_name=resource_group.name,
            cluster_name="str",
            update_location_properties={
                "currentOemVersion": "str",
                "currentSbeVersion": "str",
                "currentVersion": "str",
                "hardwareModel": "str",
                "healthCheckDate": "2020-02-20 00:00:00",
                "healthCheckResult": [
                    {
                        "additionalData": "str",
                        "description": "str",
                        "displayName": "str",
                        "healthCheckSource": "str",
                        "healthCheckTags": {},
                        "name": "str",
                        "remediation": "str",
                        "severity": "str",
                        "status": "str",
                        "tags": {"key": "str", "value": "str"},
                        "targetResourceID": "str",
                        "targetResourceName": "str",
                        "targetResourceType": "str",
                        "timestamp": "2020-02-20 00:00:00",
                        "title": "str",
                    }
                ],
                "healthState": "str",
                "id": "str",
                "lastChecked": "2020-02-20 00:00:00",
                "lastUpdated": "2020-02-20 00:00:00",
                "location": "str",
                "name": "str",
                "oemFamily": "str",
                "packageVersions": [{"lastUpdated": "2020-02-20 00:00:00", "packageType": "str", "version": "str"}],
                "provisioningState": "str",
                "state": "str",
                "systemData": {
                    "createdAt": "2020-02-20 00:00:00",
                    "createdBy": "str",
                    "createdByType": "str",
                    "lastModifiedAt": "2020-02-20 00:00:00",
                    "lastModifiedBy": "str",
                    "lastModifiedByType": "str",
                },
                "type": "str",
            },
            api_version="2024-04-01",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_get(self, resource_group):
        response = self.client.update_summaries.get(
            resource_group_name=resource_group.name,
            cluster_name="str",
            api_version="2024-04-01",
        )

        # please add some check logic here by yourself
        # ...
