# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.identity import DefaultAzureCredential
from azure.mgmt.kusto import KustoManagementClient

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-kusto
# USAGE
    python kusto_cluster_principal_assignments_create_or_update.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = KustoManagementClient(
        credential=DefaultAzureCredential(),
        subscription_id="12345678-1234-1234-1234-123456789098",
    )

    response = client.cluster_principal_assignments.begin_create_or_update(
        resource_group_name="kustorptest",
        cluster_name="kustoCluster",
        principal_assignment_name="kustoprincipal1",
        parameters={
            "properties": {
                "principalId": "87654321-1234-1234-1234-123456789123",
                "principalType": "App",
                "role": "AllDatabasesAdmin",
                "tenantId": "12345678-1234-1234-1234-123456789123",
            }
        },
    ).result()
    print(response)


# x-ms-original-file: specification/azure-kusto/resource-manager/Microsoft.Kusto/stable/2022-12-29/examples/KustoClusterPrincipalAssignmentsCreateOrUpdate.json
if __name__ == "__main__":
    main()
