# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.identity import DefaultAzureCredential
from azure.mgmt.reservations import AzureReservationAPI

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-reservations
# USAGE
    python get_reservation_order_details_with_expand_plan_information.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = AzureReservationAPI(
        credential=DefaultAzureCredential(),
    )

    response = client.reservation_order.get(
        reservation_order_id="a075419f-44cc-497f-b68a-14ee811d48b9",
    )
    print(response)


# x-ms-original-file: specification/reservations/resource-manager/Microsoft.Capacity/stable/2022-03-01/examples/GetReservationOrderDetailsWithExpandPlanInformation.json
if __name__ == "__main__":
    main()
