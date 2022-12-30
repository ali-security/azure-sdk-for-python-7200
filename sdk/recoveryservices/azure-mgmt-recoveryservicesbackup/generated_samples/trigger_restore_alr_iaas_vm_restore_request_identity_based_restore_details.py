# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.identity import DefaultAzureCredential
from azure.mgmt.recoveryservicesbackup import RecoveryServicesBackupClient

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-recoveryservicesbackup
# USAGE
    python trigger_restore_alr_iaas_vm_restore_request_identity_based_restore_details.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = RecoveryServicesBackupClient(
        credential=DefaultAzureCredential(),
        subscription_id="00000000-0000-0000-0000-000000000000",
    )

    response = client.restores.begin_trigger(
        vault_name="testVault",
        resource_group_name="netsdktestrg",
        fabric_name="Azure",
        container_name="IaasVMContainer;iaasvmcontainerv2;netsdktestrg;netvmtestv2vm1",
        protected_item_name="VM;iaasvmcontainerv2;netsdktestrg;netvmtestv2vm1",
        recovery_point_id="348916168024334",
        parameters={
            "properties": {
                "createNewCloudService": False,
                "encryptionDetails": {"encryptionEnabled": False},
                "identityBasedRestoreDetails": {
                    "targetStorageAccountId": "/subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/testRg/providers/Microsoft.Storage/storageAccounts/testingAccount"
                },
                "identityInfo": {"isSystemAssignedIdentity": True},
                "objectType": "IaasVMRestoreRequest",
                "originalStorageAccountOption": False,
                "recoveryPointId": "348916168024334",
                "recoveryType": "AlternateLocation",
                "region": "southeastasia",
                "sourceResourceId": "/subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/netsdktestrg/providers/Microsoft.Compute/virtualMachines/netvmtestv2vm1",
                "subnetId": "/subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/testRg/providers/Microsoft.Network/virtualNetworks/testNet/subnets/default",
                "targetResourceGroupId": "/subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/netsdktestrg2",
                "targetVirtualMachineId": "/subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/netsdktestrg2/providers/Microsoft.Compute/virtualmachines/RSMDALRVM981435",
                "virtualNetworkId": "/subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/testRg/providers/Microsoft.Network/virtualNetworks/testNet",
            }
        },
    ).result()
    print(response)


# x-ms-original-file: specification/recoveryservicesbackup/resource-manager/Microsoft.RecoveryServices/preview/2022-09-01-preview/examples/AzureIaasVm/TriggerRestore_ALR_IaasVMRestoreRequest_IdentityBasedRestoreDetails.json
if __name__ == "__main__":
    main()
