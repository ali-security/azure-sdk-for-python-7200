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


class DataDisk(Model):
    """Describes a data disk.

    :param lun: Specifies the logical unit number of the data disk. This value
     is used to identify data disks within the VM and therefore must be unique
     for each data disk attached to a VM.
    :type lun: int
    :param name: The disk name.
    :type name: str
    :param vhd: The virtual hard disk..
    :type vhd: :class:`VirtualHardDisk
     <azure.mgmt.compute.compute.v2017_03_30.models.VirtualHardDisk>`
    :param image: The source user image virtual hard disk. The virtual hard
     disk will be copied before being attached to the virtual machine. If
     SourceImage is provided, the destination virtual hard drive must not
     exist.
    :type image: :class:`VirtualHardDisk
     <azure.mgmt.compute.compute.v2017_03_30.models.VirtualHardDisk>`
    :param caching: Specifies the caching requirements. <br><br> Possible
     values are: <br><br> **None** <br><br> **ReadOnly** <br><br> **ReadWrite**
     <br><br> Default: **None for Standard storage. ReadOnly for Premium
     storage**. Possible values include: 'None', 'ReadOnly', 'ReadWrite'
    :type caching: str or :class:`CachingTypes
     <azure.mgmt.compute.compute.v2017_03_30.models.CachingTypes>`
    :param create_option: Specifies how the virtual machine should be
     created.<br><br> Possible values are:<br><br> **Attach** \\u2013 This
     value is used when you are using a specialized disk to create the virtual
     machine.<br><br> **FromImage** \\u2013 This value is used when you are
     using an image to create the virtual machine. If you are using a platform
     image, you also use the imageReference element described above. If you are
     using a marketplace image, you  also use the plan element previously
     described. Possible values include: 'fromImage', 'empty', 'attach'
    :type create_option: str or :class:`DiskCreateOptionTypes
     <azure.mgmt.compute.compute.v2017_03_30.models.DiskCreateOptionTypes>`
    :param disk_size_gb: Specifies the size of an empty data disk in
     gigabytes. This element can be used to overwrite the name of the disk in a
     virtual machine image. <br><br> This value cannot be larger than 1023 GB
    :type disk_size_gb: int
    :param managed_disk: The managed disk parameters.
    :type managed_disk: :class:`ManagedDiskParameters
     <azure.mgmt.compute.compute.v2017_03_30.models.ManagedDiskParameters>`
    """

    _validation = {
        'lun': {'required': True},
        'create_option': {'required': True},
    }

    _attribute_map = {
        'lun': {'key': 'lun', 'type': 'int'},
        'name': {'key': 'name', 'type': 'str'},
        'vhd': {'key': 'vhd', 'type': 'VirtualHardDisk'},
        'image': {'key': 'image', 'type': 'VirtualHardDisk'},
        'caching': {'key': 'caching', 'type': 'CachingTypes'},
        'create_option': {'key': 'createOption', 'type': 'DiskCreateOptionTypes'},
        'disk_size_gb': {'key': 'diskSizeGB', 'type': 'int'},
        'managed_disk': {'key': 'managedDisk', 'type': 'ManagedDiskParameters'},
    }

    def __init__(self, lun, create_option, name=None, vhd=None, image=None, caching=None, disk_size_gb=None, managed_disk=None):
        self.lun = lun
        self.name = name
        self.vhd = vhd
        self.image = image
        self.caching = caching
        self.create_option = create_option
        self.disk_size_gb = disk_size_gb
        self.managed_disk = managed_disk
