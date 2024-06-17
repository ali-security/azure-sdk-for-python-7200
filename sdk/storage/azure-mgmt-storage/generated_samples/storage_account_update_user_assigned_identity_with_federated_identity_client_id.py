# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Any, IO, Union

from azure.identity import DefaultAzureCredential

from azure.mgmt.storage import StorageManagementClient

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-storage
# USAGE
    python storage_account_update_user_assigned_identity_with_federated_identity_client_id.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = StorageManagementClient(
        credential=DefaultAzureCredential(),
        subscription_id="{subscription-id}",
    )

    response = client.storage_accounts.update(
        resource_group_name="res131918",
        account_name="sto131918",
        parameters={
            "identity": {
                "type": "UserAssigned",
                "userAssignedIdentities": {
                    "/subscriptions/{subscription-id}/resourceGroups/res9101/providers/Microsoft.ManagedIdentity/userAssignedIdentities/{managed-identity-name}": {}
                },
            },
            "kind": "Storage",
            "properties": {
                "encryption": {
                    "identity": {
                        "federatedIdentityClientId": "3109d1c4-a5de-4d84-8832-feabb916a4b6",
                        "userAssignedIdentity": "/subscriptions/{subscription-id}/resourceGroups/res9101/providers/Microsoft.ManagedIdentity/userAssignedIdentities/{managed-identity-name}",
                    },
                    "keySource": "Microsoft.Keyvault",
                    "keyvaultproperties": {
                        "keyname": "wrappingKey",
                        "keyvaulturi": "https://myvault8569.vault.azure.net",
                        "keyversion": "",
                    },
                    "services": {
                        "blob": {"enabled": True, "keyType": "Account"},
                        "file": {"enabled": True, "keyType": "Account"},
                    },
                }
            },
            "sku": {"name": "Standard_LRS"},
        },
    )
    print(response)


# x-ms-original-file: specification/storage/resource-manager/Microsoft.Storage/stable/2023-05-01/examples/StorageAccountUpdateUserAssignedIdentityWithFederatedIdentityClientId.json
if __name__ == "__main__":
    main()
