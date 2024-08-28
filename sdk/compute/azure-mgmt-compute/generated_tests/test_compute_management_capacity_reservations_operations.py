# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import pytest
from azure.mgmt.compute import ComputeManagementClient

from devtools_testutils import AzureMgmtRecordedTestCase, RandomNameResourceGroupPreparer, recorded_by_proxy

AZURE_LOCATION = "eastus"


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestComputeManagementCapacityReservationsOperations(AzureMgmtRecordedTestCase):
    def setup_method(self, method):
        self.client = self.create_mgmt_client(ComputeManagementClient)

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_begin_create_or_update(self, resource_group):
        response = self.client.capacity_reservations.begin_create_or_update(
            resource_group_name=resource_group.name,
            capacity_reservation_group_name="str",
            capacity_reservation_name="str",
            parameters={
                "location": "str",
                "sku": {"capacity": 0, "name": "str", "tier": "str"},
                "id": "str",
                "instanceView": {
                    "statuses": [
                        {
                            "code": "str",
                            "displayStatus": "str",
                            "level": "str",
                            "message": "str",
                            "time": "2020-02-20 00:00:00",
                        }
                    ],
                    "utilizationInfo": {"currentCapacity": 0, "virtualMachinesAllocated": [{"id": "str"}]},
                },
                "name": "str",
                "platformFaultDomainCount": 0,
                "provisioningState": "str",
                "provisioningTime": "2020-02-20 00:00:00",
                "reservationId": "str",
                "tags": {"str": "str"},
                "timeCreated": "2020-02-20 00:00:00",
                "type": "str",
                "virtualMachinesAssociated": [{"id": "str"}],
                "zones": ["str"],
            },
            api_version="2024-07-01",
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_begin_update(self, resource_group):
        response = self.client.capacity_reservations.begin_update(
            resource_group_name=resource_group.name,
            capacity_reservation_group_name="str",
            capacity_reservation_name="str",
            parameters={
                "instanceView": {
                    "statuses": [
                        {
                            "code": "str",
                            "displayStatus": "str",
                            "level": "str",
                            "message": "str",
                            "time": "2020-02-20 00:00:00",
                        }
                    ],
                    "utilizationInfo": {"currentCapacity": 0, "virtualMachinesAllocated": [{"id": "str"}]},
                },
                "platformFaultDomainCount": 0,
                "provisioningState": "str",
                "provisioningTime": "2020-02-20 00:00:00",
                "reservationId": "str",
                "sku": {"capacity": 0, "name": "str", "tier": "str"},
                "tags": {"str": "str"},
                "timeCreated": "2020-02-20 00:00:00",
                "virtualMachinesAssociated": [{"id": "str"}],
            },
            api_version="2024-07-01",
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_begin_delete(self, resource_group):
        response = self.client.capacity_reservations.begin_delete(
            resource_group_name=resource_group.name,
            capacity_reservation_group_name="str",
            capacity_reservation_name="str",
            api_version="2024-07-01",
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_get(self, resource_group):
        response = self.client.capacity_reservations.get(
            resource_group_name=resource_group.name,
            capacity_reservation_group_name="str",
            capacity_reservation_name="str",
            api_version="2024-07-01",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_list_by_capacity_reservation_group(self, resource_group):
        response = self.client.capacity_reservations.list_by_capacity_reservation_group(
            resource_group_name=resource_group.name,
            capacity_reservation_group_name="str",
            api_version="2024-07-01",
        )
        result = [r for r in response]
        # please add some check logic here by yourself
        # ...
