# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.identity import DefaultAzureCredential
from azure.mgmt.network import NetworkManagementClient

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-network
# USAGE
    python virtual_hub_route_table_v2_put.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = NetworkManagementClient(
        credential=DefaultAzureCredential(),
        subscription_id="subid",
    )

    response = client.virtual_hub_route_table_v2_s.begin_create_or_update(
        resource_group_name="rg1",
        virtual_hub_name="virtualHub1",
        route_table_name="virtualHubRouteTable1a",
        virtual_hub_route_table_v2_parameters={
            "properties": {
                "attachedConnections": ["All_Vnets"],
                "routes": [
                    {
                        "destinationType": "CIDR",
                        "destinations": ["20.10.0.0/16", "20.20.0.0/16"],
                        "nextHopType": "IPAddress",
                        "nextHops": ["10.0.0.68"],
                    },
                    {
                        "destinationType": "CIDR",
                        "destinations": ["0.0.0.0/0"],
                        "nextHopType": "IPAddress",
                        "nextHops": ["10.0.0.68"],
                    },
                ],
            }
        },
    ).result()
    print(response)


# x-ms-original-file: specification/network/resource-manager/Microsoft.Network/stable/2022-07-01/examples/VirtualHubRouteTableV2Put.json
if __name__ == "__main__":
    main()
