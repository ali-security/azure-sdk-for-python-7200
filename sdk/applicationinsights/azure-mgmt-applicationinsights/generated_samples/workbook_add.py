# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.identity import DefaultAzureCredential
from azure.mgmt.applicationinsights import ApplicationInsightsManagementClient

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-applicationinsights
# USAGE
    python workbook_add.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = ApplicationInsightsManagementClient(
        credential=DefaultAzureCredential(),
        subscription_id="6b643656-33eb-422f-aee8-3ac145d124af",
    )

    response = client.workbooks.create_or_update(
        resource_group_name="my-resource-group",
        resource_name="deadb33f-5e0d-4064-8ebb-1a4ed0313eb2",
        workbook_properties={
            "kind": "shared",
            "location": "westus",
            "properties": {
                "category": "workbook",
                "description": "Sample workbook",
                "displayName": "Sample workbook",
                "serializedData": '{"version":"Notebook/1.0","items":[{"type":1,"content":"{"json":"## New workbook\\r\\n---\\r\\n\\r\\nWelcome to your new workbook.  This area will display text formatted as markdown.\\r\\n\\r\\n\\r\\nWe\'ve included a basic analytics query to get you started. Use the `Edit` button below each section to configure it or add more sections."}","halfWidth":null,"conditionalVisibility":null},{"type":3,"content":"{"version":"KqlItem/1.0","query":"union withsource=TableName *\\n| summarize Count=count() by TableName\\n| render barchart","showQuery":false,"size":1,"aggregation":0,"showAnnotations":false}","halfWidth":null,"conditionalVisibility":null}],"isLocked":false}',
            },
            "tags": {"TagSample01": "sample01", "TagSample02": "sample02"},
        },
    )
    print(response)


# x-ms-original-file: specification/applicationinsights/resource-manager/Microsoft.Insights/stable/2022-04-01/examples/WorkbookAdd.json
if __name__ == "__main__":
    main()
