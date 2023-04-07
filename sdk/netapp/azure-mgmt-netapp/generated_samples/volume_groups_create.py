# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.identity import DefaultAzureCredential
from azure.mgmt.netapp import NetAppManagementClient

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-netapp
# USAGE
    python volume_groups_create.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = NetAppManagementClient(
        credential=DefaultAzureCredential(),
        subscription_id="D633CC2E-722B-4AE1-B636-BBD9E4C60ED9",
    )

    response = client.volume_groups.begin_create(
        resource_group_name="myRG",
        account_name="account1",
        volume_group_name="group1",
        body={
            "location": "westus",
            "properties": {
                "groupMetaData": {
                    "applicationIdentifier": "DEV",
                    "applicationType": "SAP-HANA",
                    "deploymentSpecId": "20542149-bfca-5618-1879-9863dc6767f1",
                    "groupDescription": "Volume group",
                },
                "volumes": [
                    {
                        "name": "test-data-mnt00001",
                        "properties": {
                            "capacityPoolResourceId": "/subscriptions/d633cc2e-722b-4ae1-b636-bbd9e4c60ed9/resourceGroups/myRG/providers/Microsoft.NetApp/netAppAccounts/account1/capacityPools/pool1",
                            "creationToken": "test-data-mnt00001",
                            "proximityPlacementGroup": "/subscriptions/d633cc2e-722b-4ae1-b636-bbd9e4c60ed9/resourceGroups/cys_sjain_fcp_rg/providers/Microsoft.Compute/proximityPlacementGroups/svlqa_sjain_multivolume_ppg",
                            "serviceLevel": "Premium",
                            "subnetId": "/subscriptions/d633cc2e-722b-4ae1-b636-bbd9e4c60ed9/resourceGroups/myRP/providers/Microsoft.Network/virtualNetworks/testvnet3/subnets/testsubnet3",
                            "throughputMibps": 10,
                            "usageThreshold": 107374182400,
                            "volumeSpecName": "data",
                        },
                    },
                    {
                        "name": "test-log-mnt00001",
                        "properties": {
                            "capacityPoolResourceId": "/subscriptions/d633cc2e-722b-4ae1-b636-bbd9e4c60ed9/resourceGroups/myRG/providers/Microsoft.NetApp/netAppAccounts/account1/capacityPools/pool1",
                            "creationToken": "test-log-mnt00001",
                            "proximityPlacementGroup": "/subscriptions/d633cc2e-722b-4ae1-b636-bbd9e4c60ed9/resourceGroups/cys_sjain_fcp_rg/providers/Microsoft.Compute/proximityPlacementGroups/svlqa_sjain_multivolume_ppg",
                            "serviceLevel": "Premium",
                            "subnetId": "/subscriptions/d633cc2e-722b-4ae1-b636-bbd9e4c60ed9/resourceGroups/myRP/providers/Microsoft.Network/virtualNetworks/testvnet3/subnets/testsubnet3",
                            "throughputMibps": 10,
                            "usageThreshold": 107374182400,
                            "volumeSpecName": "log",
                        },
                    },
                    {
                        "name": "test-shared",
                        "properties": {
                            "capacityPoolResourceId": "/subscriptions/d633cc2e-722b-4ae1-b636-bbd9e4c60ed9/resourceGroups/myRG/providers/Microsoft.NetApp/netAppAccounts/account1/capacityPools/pool1",
                            "creationToken": "test-shared",
                            "proximityPlacementGroup": "/subscriptions/d633cc2e-722b-4ae1-b636-bbd9e4c60ed9/resourceGroups/cys_sjain_fcp_rg/providers/Microsoft.Compute/proximityPlacementGroups/svlqa_sjain_multivolume_ppg",
                            "serviceLevel": "Premium",
                            "subnetId": "/subscriptions/d633cc2e-722b-4ae1-b636-bbd9e4c60ed9/resourceGroups/myRP/providers/Microsoft.Network/virtualNetworks/testvnet3/subnets/testsubnet3",
                            "throughputMibps": 10,
                            "usageThreshold": 107374182400,
                            "volumeSpecName": "shared",
                        },
                    },
                ],
            },
        },
    ).result()
    print(response)


# x-ms-original-file: specification/netapp/resource-manager/Microsoft.NetApp/stable/2022-05-01/examples/VolumeGroups_Create.json
if __name__ == "__main__":
    main()
