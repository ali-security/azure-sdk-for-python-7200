# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ContainerServiceDiagnosticsProfile(Model):
    """ContainerServiceDiagnosticsProfile.

    :param vm_diagnostics: Profile for container service VM diagnostic agent
    :type vm_diagnostics: :class:`ContainerServiceVMDiagnostics
     <azure.mgmt.compute.models.ContainerServiceVMDiagnostics>`
    """ 

    _validation = {
        'vm_diagnostics': {'required': True},
    }

    _attribute_map = {
        'vm_diagnostics': {'key': 'vmDiagnostics', 'type': 'ContainerServiceVMDiagnostics'},
    }

    def __init__(self, vm_diagnostics):
        self.vm_diagnostics = vm_diagnostics
