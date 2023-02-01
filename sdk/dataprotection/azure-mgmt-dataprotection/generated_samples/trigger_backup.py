# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.identity import DefaultAzureCredential
from azure.mgmt.dataprotection import DataProtectionClient

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-dataprotection
# USAGE
    python trigger_backup.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = DataProtectionClient(
        credential=DefaultAzureCredential(),
        subscription_id="04cf684a-d41f-4550-9f70-7708a3a2283b",
    )

    response = client.backup_instances.begin_adhoc_backup(
        resource_group_name="000pikumar",
        vault_name="PratikPrivatePreviewVault1",
        backup_instance_name="testInstance1",
        parameters={
            "backupRuleOptions": {"ruleName": "BackupWeekly", "triggerOption": {"retentionTagOverride": "yearly"}}
        },
    ).result()
    print(response)


# x-ms-original-file: specification/dataprotection/resource-manager/Microsoft.DataProtection/preview/2022-11-01-preview/examples/BackupInstanceOperations/TriggerBackup.json
if __name__ == "__main__":
    main()
