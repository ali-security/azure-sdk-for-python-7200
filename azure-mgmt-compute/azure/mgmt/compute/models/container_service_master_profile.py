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


class ContainerServiceMasterProfile(Model):
    """Profile for container service master.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :param count: Number of masters (VMs) in the container cluster. Default
     value: 1 .
    :type count: int
    :param dns_prefix: DNS prefix to be used to create FQDN for master
    :type dns_prefix: str
    :ivar fqdn: FDQN for the master
    :vartype fqdn: str
    """ 

    _validation = {
        'dns_prefix': {'required': True},
        'fqdn': {'readonly': True},
    }

    _attribute_map = {
        'count': {'key': 'count', 'type': 'int'},
        'dns_prefix': {'key': 'dnsPrefix', 'type': 'str'},
        'fqdn': {'key': 'fqdn', 'type': 'str'},
    }

    def __init__(self, dns_prefix, count=1):
        self.count = count
        self.dns_prefix = dns_prefix
        self.fqdn = None
