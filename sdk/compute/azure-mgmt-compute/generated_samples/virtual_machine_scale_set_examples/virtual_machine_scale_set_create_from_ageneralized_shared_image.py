# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Any, IO, Union

from azure.identity import DefaultAzureCredential

from azure.mgmt.compute import ComputeManagementClient

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-compute
# USAGE
    python virtual_machine_scale_set_create_from_ageneralized_shared_image.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = ComputeManagementClient(
        credential=DefaultAzureCredential(),
        subscription_id="{subscription-id}",
    )

    response = client.virtual_machine_scale_sets.begin_create_or_update(
        resource_group_name="myResourceGroup",
        vm_scale_set_name="{vmss-name}",
        parameters={
            "location": "westus",
            "properties": {
                "overprovision": True,
                "upgradePolicy": {"mode": "Manual"},
                "virtualMachineProfile": {
                    "networkProfile": {
                        "networkInterfaceConfigurations": [
                            {
                                "name": "{vmss-name}",
                                "properties": {
                                    "enableIPForwarding": True,
                                    "ipConfigurations": [
                                        {
                                            "name": "{vmss-name}",
                                            "properties": {
                                                "subnet": {
                                                    "id": "/subscriptions/{subscription-id}/resourceGroups/myResourceGroup/providers/Microsoft.Network/virtualNetworks/{existing-virtual-network-name}/subnets/{existing-subnet-name}"
                                                }
                                            },
                                        }
                                    ],
                                    "primary": True,
                                },
                            }
                        ]
                    },
                    "osProfile": {
                        "adminPassword": "{your-password}",
                        "adminUsername": "{your-username}",
                        "computerNamePrefix": "{vmss-name}",
                    },
                    "storageProfile": {
                        "imageReference": {
                            "id": "/subscriptions/{subscription-id}/resourceGroups/myResourceGroup/providers/Microsoft.Compute/galleries/mySharedGallery/images/mySharedImage"
                        },
                        "osDisk": {
                            "caching": "ReadWrite",
                            "createOption": "FromImage",
                            "managedDisk": {"storageAccountType": "Standard_LRS"},
                        },
                    },
                },
            },
            "sku": {"capacity": 3, "name": "Standard_D1_v2", "tier": "Standard"},
        },
    ).result()
    print(response)


# x-ms-original-file: specification/compute/resource-manager/Microsoft.Compute/ComputeRP/stable/2023-09-01/examples/virtualMachineScaleSetExamples/VirtualMachineScaleSet_Create_FromAGeneralizedSharedImage.json
if __name__ == "__main__":
    main()
