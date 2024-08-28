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
class TestComputeManagementVirtualMachineScaleSetVMsOperations(AzureMgmtRecordedTestCase):
    def setup_method(self, method):
        self.client = self.create_mgmt_client(ComputeManagementClient)

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_begin_reimage(self, resource_group):
        response = self.client.virtual_machine_scale_set_vms.begin_reimage(
            resource_group_name=resource_group.name,
            vm_scale_set_name="str",
            instance_id="str",
            api_version="2024-07-01",
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_begin_reimage_all(self, resource_group):
        response = self.client.virtual_machine_scale_set_vms.begin_reimage_all(
            resource_group_name=resource_group.name,
            vm_scale_set_name="str",
            instance_id="str",
            api_version="2024-07-01",
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_begin_approve_rolling_upgrade(self, resource_group):
        response = self.client.virtual_machine_scale_set_vms.begin_approve_rolling_upgrade(
            resource_group_name=resource_group.name,
            vm_scale_set_name="str",
            instance_id="str",
            api_version="2024-07-01",
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_begin_deallocate(self, resource_group):
        response = self.client.virtual_machine_scale_set_vms.begin_deallocate(
            resource_group_name=resource_group.name,
            vm_scale_set_name="str",
            instance_id="str",
            api_version="2024-07-01",
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_begin_update(self, resource_group):
        response = self.client.virtual_machine_scale_set_vms.begin_update(
            resource_group_name=resource_group.name,
            vm_scale_set_name="str",
            instance_id="str",
            parameters={
                "location": "str",
                "additionalCapabilities": {"hibernationEnabled": bool, "ultraSSDEnabled": bool},
                "availabilitySet": {"id": "str"},
                "diagnosticsProfile": {"bootDiagnostics": {"enabled": bool, "storageUri": "str"}},
                "etag": "str",
                "hardwareProfile": {"vmSize": "str", "vmSizeProperties": {"vCPUsAvailable": 0, "vCPUsPerCore": 0}},
                "id": "str",
                "identity": {
                    "principalId": "str",
                    "tenantId": "str",
                    "type": "str",
                    "userAssignedIdentities": {"str": {"clientId": "str", "principalId": "str"}},
                },
                "instanceId": "str",
                "instanceView": {
                    "assignedHost": "str",
                    "bootDiagnostics": {
                        "consoleScreenshotBlobUri": "str",
                        "serialConsoleLogBlobUri": "str",
                        "status": {
                            "code": "str",
                            "displayStatus": "str",
                            "level": "str",
                            "message": "str",
                            "time": "2020-02-20 00:00:00",
                        },
                    },
                    "computerName": "str",
                    "disks": [
                        {
                            "encryptionSettings": [
                                {
                                    "diskEncryptionKey": {"secretUrl": "str", "sourceVault": {"id": "str"}},
                                    "enabled": bool,
                                    "keyEncryptionKey": {"keyUrl": "str", "sourceVault": {"id": "str"}},
                                }
                            ],
                            "name": "str",
                            "statuses": [
                                {
                                    "code": "str",
                                    "displayStatus": "str",
                                    "level": "str",
                                    "message": "str",
                                    "time": "2020-02-20 00:00:00",
                                }
                            ],
                        }
                    ],
                    "extensions": [
                        {
                            "name": "str",
                            "statuses": [
                                {
                                    "code": "str",
                                    "displayStatus": "str",
                                    "level": "str",
                                    "message": "str",
                                    "time": "2020-02-20 00:00:00",
                                }
                            ],
                            "substatuses": [
                                {
                                    "code": "str",
                                    "displayStatus": "str",
                                    "level": "str",
                                    "message": "str",
                                    "time": "2020-02-20 00:00:00",
                                }
                            ],
                            "type": "str",
                            "typeHandlerVersion": "str",
                        }
                    ],
                    "hyperVGeneration": "str",
                    "maintenanceRedeployStatus": {
                        "isCustomerInitiatedMaintenanceAllowed": bool,
                        "lastOperationMessage": "str",
                        "lastOperationResultCode": "str",
                        "maintenanceWindowEndTime": "2020-02-20 00:00:00",
                        "maintenanceWindowStartTime": "2020-02-20 00:00:00",
                        "preMaintenanceWindowEndTime": "2020-02-20 00:00:00",
                        "preMaintenanceWindowStartTime": "2020-02-20 00:00:00",
                    },
                    "osName": "str",
                    "osVersion": "str",
                    "placementGroupId": "str",
                    "platformFaultDomain": 0,
                    "platformUpdateDomain": 0,
                    "rdpThumbPrint": "str",
                    "statuses": [
                        {
                            "code": "str",
                            "displayStatus": "str",
                            "level": "str",
                            "message": "str",
                            "time": "2020-02-20 00:00:00",
                        }
                    ],
                    "vmAgent": {
                        "extensionHandlers": [
                            {
                                "status": {
                                    "code": "str",
                                    "displayStatus": "str",
                                    "level": "str",
                                    "message": "str",
                                    "time": "2020-02-20 00:00:00",
                                },
                                "type": "str",
                                "typeHandlerVersion": "str",
                            }
                        ],
                        "statuses": [
                            {
                                "code": "str",
                                "displayStatus": "str",
                                "level": "str",
                                "message": "str",
                                "time": "2020-02-20 00:00:00",
                            }
                        ],
                        "vmAgentVersion": "str",
                    },
                    "vmHealth": {
                        "status": {
                            "code": "str",
                            "displayStatus": "str",
                            "level": "str",
                            "message": "str",
                            "time": "2020-02-20 00:00:00",
                        }
                    },
                },
                "latestModelApplied": bool,
                "licenseType": "str",
                "modelDefinitionApplied": "str",
                "name": "str",
                "networkProfile": {
                    "networkApiVersion": "str",
                    "networkInterfaceConfigurations": [
                        {
                            "name": "str",
                            "auxiliaryMode": "str",
                            "auxiliarySku": "str",
                            "deleteOption": "str",
                            "disableTcpStateTracking": bool,
                            "dnsSettings": {"dnsServers": ["str"]},
                            "dscpConfiguration": {"id": "str"},
                            "enableAcceleratedNetworking": bool,
                            "enableFpga": bool,
                            "enableIPForwarding": bool,
                            "ipConfigurations": [
                                {
                                    "name": "str",
                                    "applicationGatewayBackendAddressPools": [{"id": "str"}],
                                    "applicationSecurityGroups": [{"id": "str"}],
                                    "loadBalancerBackendAddressPools": [{"id": "str"}],
                                    "primary": bool,
                                    "privateIPAddressVersion": "str",
                                    "publicIPAddressConfiguration": {
                                        "name": "str",
                                        "deleteOption": "str",
                                        "dnsSettings": {"domainNameLabel": "str", "domainNameLabelScope": "str"},
                                        "idleTimeoutInMinutes": 0,
                                        "ipTags": [{"ipTagType": "str", "tag": "str"}],
                                        "publicIPAddressVersion": "str",
                                        "publicIPAllocationMethod": "str",
                                        "publicIPPrefix": {"id": "str"},
                                        "sku": {"name": "str", "tier": "str"},
                                    },
                                    "subnet": {"id": "str"},
                                }
                            ],
                            "networkSecurityGroup": {"id": "str"},
                            "primary": bool,
                        }
                    ],
                    "networkInterfaces": [{"deleteOption": "str", "id": "str", "primary": bool}],
                },
                "networkProfileConfiguration": {
                    "networkInterfaceConfigurations": [
                        {
                            "name": "str",
                            "auxiliaryMode": "str",
                            "auxiliarySku": "str",
                            "deleteOption": "str",
                            "disableTcpStateTracking": bool,
                            "dnsSettings": {"dnsServers": ["str"]},
                            "enableAcceleratedNetworking": bool,
                            "enableFpga": bool,
                            "enableIPForwarding": bool,
                            "ipConfigurations": [
                                {
                                    "name": "str",
                                    "applicationGatewayBackendAddressPools": [{"id": "str"}],
                                    "applicationSecurityGroups": [{"id": "str"}],
                                    "loadBalancerBackendAddressPools": [{"id": "str"}],
                                    "loadBalancerInboundNatPools": [{"id": "str"}],
                                    "primary": bool,
                                    "privateIPAddressVersion": "str",
                                    "publicIPAddressConfiguration": {
                                        "name": "str",
                                        "deleteOption": "str",
                                        "dnsSettings": {"domainNameLabel": "str", "domainNameLabelScope": "str"},
                                        "idleTimeoutInMinutes": 0,
                                        "ipTags": [{"ipTagType": "str", "tag": "str"}],
                                        "publicIPAddressVersion": "str",
                                        "publicIPPrefix": {"id": "str"},
                                        "sku": {"name": "str", "tier": "str"},
                                    },
                                    "subnet": {"id": "str"},
                                }
                            ],
                            "networkSecurityGroup": {"id": "str"},
                            "primary": bool,
                        }
                    ]
                },
                "osProfile": {
                    "adminPassword": "str",
                    "adminUsername": "str",
                    "allowExtensionOperations": bool,
                    "computerName": "str",
                    "customData": "str",
                    "linuxConfiguration": {
                        "disablePasswordAuthentication": bool,
                        "enableVMAgentPlatformUpdates": bool,
                        "patchSettings": {
                            "assessmentMode": "str",
                            "automaticByPlatformSettings": {
                                "bypassPlatformSafetyChecksOnUserSchedule": bool,
                                "rebootSetting": "str",
                            },
                            "patchMode": "str",
                        },
                        "provisionVMAgent": bool,
                        "ssh": {"publicKeys": [{"keyData": "str", "path": "str"}]},
                    },
                    "requireGuestProvisionSignal": bool,
                    "secrets": [
                        {
                            "sourceVault": {"id": "str"},
                            "vaultCertificates": [{"certificateStore": "str", "certificateUrl": "str"}],
                        }
                    ],
                    "windowsConfiguration": {
                        "additionalUnattendContent": [
                            {
                                "componentName": "Microsoft-Windows-Shell-Setup",
                                "content": "str",
                                "passName": "OobeSystem",
                                "settingName": "str",
                            }
                        ],
                        "enableAutomaticUpdates": bool,
                        "enableVMAgentPlatformUpdates": bool,
                        "patchSettings": {
                            "assessmentMode": "str",
                            "automaticByPlatformSettings": {
                                "bypassPlatformSafetyChecksOnUserSchedule": bool,
                                "rebootSetting": "str",
                            },
                            "enableHotpatching": bool,
                            "patchMode": "str",
                        },
                        "provisionVMAgent": bool,
                        "timeZone": "str",
                        "winRM": {"listeners": [{"certificateUrl": "str", "protocol": "str"}]},
                    },
                },
                "plan": {"name": "str", "product": "str", "promotionCode": "str", "publisher": "str"},
                "protectionPolicy": {"protectFromScaleIn": bool, "protectFromScaleSetActions": bool},
                "provisioningState": "str",
                "resources": [
                    {
                        "autoUpgradeMinorVersion": bool,
                        "enableAutomaticUpgrade": bool,
                        "forceUpdateTag": "str",
                        "id": "str",
                        "instanceView": {
                            "name": "str",
                            "statuses": [
                                {
                                    "code": "str",
                                    "displayStatus": "str",
                                    "level": "str",
                                    "message": "str",
                                    "time": "2020-02-20 00:00:00",
                                }
                            ],
                            "substatuses": [
                                {
                                    "code": "str",
                                    "displayStatus": "str",
                                    "level": "str",
                                    "message": "str",
                                    "time": "2020-02-20 00:00:00",
                                }
                            ],
                            "type": "str",
                            "typeHandlerVersion": "str",
                        },
                        "location": "str",
                        "name": "str",
                        "protectedSettings": {},
                        "protectedSettingsFromKeyVault": {"secretUrl": "str", "sourceVault": {"id": "str"}},
                        "provisionAfterExtensions": ["str"],
                        "provisioningState": "str",
                        "publisher": "str",
                        "settings": {},
                        "suppressFailures": bool,
                        "tags": {"str": "str"},
                        "type": "str",
                        "typeHandlerVersion": "str",
                    }
                ],
                "securityProfile": {
                    "encryptionAtHost": bool,
                    "encryptionIdentity": {"userAssignedIdentityResourceId": "str"},
                    "proxyAgentSettings": {"enabled": bool, "keyIncarnationId": 0, "mode": "str"},
                    "securityType": "str",
                    "uefiSettings": {"secureBootEnabled": bool, "vTpmEnabled": bool},
                },
                "sku": {"capacity": 0, "name": "str", "tier": "str"},
                "storageProfile": {
                    "dataDisks": [
                        {
                            "createOption": "str",
                            "lun": 0,
                            "caching": "str",
                            "deleteOption": "str",
                            "detachOption": "str",
                            "diskIOPSReadWrite": 0,
                            "diskMBpsReadWrite": 0,
                            "diskSizeGB": 0,
                            "image": {"uri": "str"},
                            "managedDisk": {
                                "diskEncryptionSet": {"id": "str"},
                                "id": "str",
                                "securityProfile": {
                                    "diskEncryptionSet": {"id": "str"},
                                    "securityEncryptionType": "str",
                                },
                                "storageAccountType": "str",
                            },
                            "name": "str",
                            "sourceResource": {"id": "str"},
                            "toBeDetached": bool,
                            "vhd": {"uri": "str"},
                            "writeAcceleratorEnabled": bool,
                        }
                    ],
                    "diskControllerType": "str",
                    "imageReference": {
                        "communityGalleryImageId": "str",
                        "exactVersion": "str",
                        "id": "str",
                        "offer": "str",
                        "publisher": "str",
                        "sharedGalleryImageId": "str",
                        "sku": "str",
                        "version": "str",
                    },
                    "osDisk": {
                        "createOption": "str",
                        "caching": "str",
                        "deleteOption": "str",
                        "diffDiskSettings": {"option": "str", "placement": "str"},
                        "diskSizeGB": 0,
                        "encryptionSettings": {
                            "diskEncryptionKey": {"secretUrl": "str", "sourceVault": {"id": "str"}},
                            "enabled": bool,
                            "keyEncryptionKey": {"keyUrl": "str", "sourceVault": {"id": "str"}},
                        },
                        "image": {"uri": "str"},
                        "managedDisk": {
                            "diskEncryptionSet": {"id": "str"},
                            "id": "str",
                            "securityProfile": {"diskEncryptionSet": {"id": "str"}, "securityEncryptionType": "str"},
                            "storageAccountType": "str",
                        },
                        "name": "str",
                        "osType": "str",
                        "vhd": {"uri": "str"},
                        "writeAcceleratorEnabled": bool,
                    },
                },
                "tags": {"str": "str"},
                "timeCreated": "2020-02-20 00:00:00",
                "type": "str",
                "userData": "str",
                "vmId": "str",
                "zones": ["str"],
            },
            api_version="2024-07-01",
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_begin_delete(self, resource_group):
        response = self.client.virtual_machine_scale_set_vms.begin_delete(
            resource_group_name=resource_group.name,
            vm_scale_set_name="str",
            instance_id="str",
            api_version="2024-07-01",
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_get(self, resource_group):
        response = self.client.virtual_machine_scale_set_vms.get(
            resource_group_name=resource_group.name,
            vm_scale_set_name="str",
            instance_id="str",
            api_version="2024-07-01",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_get_instance_view(self, resource_group):
        response = self.client.virtual_machine_scale_set_vms.get_instance_view(
            resource_group_name=resource_group.name,
            vm_scale_set_name="str",
            instance_id="str",
            api_version="2024-07-01",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_list(self, resource_group):
        response = self.client.virtual_machine_scale_set_vms.list(
            resource_group_name=resource_group.name,
            virtual_machine_scale_set_name="str",
            api_version="2024-07-01",
        )
        result = [r for r in response]
        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_begin_power_off(self, resource_group):
        response = self.client.virtual_machine_scale_set_vms.begin_power_off(
            resource_group_name=resource_group.name,
            vm_scale_set_name="str",
            instance_id="str",
            api_version="2024-07-01",
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_begin_restart(self, resource_group):
        response = self.client.virtual_machine_scale_set_vms.begin_restart(
            resource_group_name=resource_group.name,
            vm_scale_set_name="str",
            instance_id="str",
            api_version="2024-07-01",
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_begin_start(self, resource_group):
        response = self.client.virtual_machine_scale_set_vms.begin_start(
            resource_group_name=resource_group.name,
            vm_scale_set_name="str",
            instance_id="str",
            api_version="2024-07-01",
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_begin_redeploy(self, resource_group):
        response = self.client.virtual_machine_scale_set_vms.begin_redeploy(
            resource_group_name=resource_group.name,
            vm_scale_set_name="str",
            instance_id="str",
            api_version="2024-07-01",
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_retrieve_boot_diagnostics_data(self, resource_group):
        response = self.client.virtual_machine_scale_set_vms.retrieve_boot_diagnostics_data(
            resource_group_name=resource_group.name,
            vm_scale_set_name="str",
            instance_id="str",
            api_version="2024-07-01",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_begin_perform_maintenance(self, resource_group):
        response = self.client.virtual_machine_scale_set_vms.begin_perform_maintenance(
            resource_group_name=resource_group.name,
            vm_scale_set_name="str",
            instance_id="str",
            api_version="2024-07-01",
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_simulate_eviction(self, resource_group):
        response = self.client.virtual_machine_scale_set_vms.simulate_eviction(
            resource_group_name=resource_group.name,
            vm_scale_set_name="str",
            instance_id="str",
            api_version="2024-07-01",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_begin_attach_detach_data_disks(self, resource_group):
        response = self.client.virtual_machine_scale_set_vms.begin_attach_detach_data_disks(
            resource_group_name=resource_group.name,
            vm_scale_set_name="str",
            instance_id="str",
            parameters={
                "dataDisksToAttach": [
                    {
                        "diskId": "str",
                        "caching": "str",
                        "deleteOption": "str",
                        "diskEncryptionSet": {"id": "str"},
                        "lun": 0,
                        "writeAcceleratorEnabled": bool,
                    }
                ],
                "dataDisksToDetach": [{"diskId": "str", "detachOption": "str"}],
            },
            api_version="2024-07-01",
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_begin_run_command(self, resource_group):
        response = self.client.virtual_machine_scale_set_vms.begin_run_command(
            resource_group_name=resource_group.name,
            vm_scale_set_name="str",
            instance_id="str",
            parameters={"commandId": "str", "parameters": [{"name": "str", "value": "str"}], "script": ["str"]},
            api_version="2024-07-01",
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...
