# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum
from azure.core import CaseInsensitiveEnumMeta


class AgentPoolMode(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """A cluster must have at least one 'System' Agent Pool at all times. For additional information
    on agent pool restrictions and best practices, see:
    https://docs.microsoft.com/azure/aks/use-system-pools.
    """

    SYSTEM = "System"
    """System agent pools are primarily for hosting critical system pods such as CoreDNS and
    #: metrics-server. System agent pools osType must be Linux. System agent pools VM SKU must have at
    #: least 2vCPUs and 4GB of memory."""
    USER = "User"
    """User agent pools are primarily for hosting your application pods."""


class AgentPoolType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The type of Agent Pool."""

    VIRTUAL_MACHINE_SCALE_SETS = "VirtualMachineScaleSets"
    """Create an Agent Pool backed by a Virtual Machine Scale Set."""
    AVAILABILITY_SET = "AvailabilitySet"
    """Use of this is strongly discouraged."""


class Code(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Tells whether the cluster is Running or Stopped."""

    RUNNING = "Running"
    """The cluster is running."""
    STOPPED = "Stopped"
    """The cluster is stopped."""


class ConnectionStatus(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The private link service connection status."""

    PENDING = "Pending"
    APPROVED = "Approved"
    REJECTED = "Rejected"
    DISCONNECTED = "Disconnected"


class CreatedByType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The type of identity that created the resource."""

    USER = "User"
    APPLICATION = "Application"
    MANAGED_IDENTITY = "ManagedIdentity"
    KEY = "Key"


class Expander(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """If not specified, the default is 'random'. See `expanders
    <https://github.com/kubernetes/autoscaler/blob/master/cluster-autoscaler/FAQ.md#what-are-expanders>`_
    for more information.
    """

    LEAST_WASTE = "least-waste"
    """Selects the node group that will have the least idle CPU (if tied, unused memory) after
    #: scale-up. This is useful when you have different classes of nodes, for example, high CPU or
    #: high memory nodes, and only want to expand those when there are pending pods that need a lot of
    #: those resources."""
    MOST_PODS = "most-pods"
    """Selects the node group that would be able to schedule the most pods when scaling up. This is
    #: useful when you are using nodeSelector to make sure certain pods land on certain nodes. Note
    #: that this won't cause the autoscaler to select bigger nodes vs. smaller, as it can add multiple
    #: smaller nodes at once."""
    PRIORITY = "priority"
    """Selects the node group that has the highest priority assigned by the user. It's configuration
    #: is described in more details `here
    #: <https://github.com/kubernetes/autoscaler/blob/master/cluster-autoscaler/expander/priority/readme.md>`_."""
    RANDOM = "random"
    """Used when you don't have a particular need for the node groups to scale differently."""


class ExtendedLocationTypes(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The type of extendedLocation."""

    EDGE_ZONE = "EdgeZone"


class Format(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Format."""

    AZURE = "azure"
    """Return azure auth-provider kubeconfig. This format is deprecated in v1.22 and will be fully
    #: removed in v1.26. See: https://aka.ms/k8s/changes-1-26."""
    EXEC = "exec"
    """Return exec format kubeconfig. This format requires kubelogin binary in the path."""


class GPUInstanceProfile(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """GPUInstanceProfile to be used to specify GPU MIG instance profile for supported GPU VM SKU."""

    MIG1_G = "MIG1g"
    MIG2_G = "MIG2g"
    MIG3_G = "MIG3g"
    MIG4_G = "MIG4g"
    MIG7_G = "MIG7g"


class IpFamily(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The IP version to use for cluster networking and IP assignment."""

    I_PV4 = "IPv4"
    I_PV6 = "IPv6"


class KeyVaultNetworkAccessTypes(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Network access of key vault. The possible values are ``Public`` and ``Private``. ``Public``
    means the key vault allows public access from all networks. ``Private`` means the key vault
    disables public access and enables private link. The default value is ``Public``.
    """

    PUBLIC = "Public"
    PRIVATE = "Private"


class KubeletDiskType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Determines the placement of emptyDir volumes, container runtime data root, and Kubelet
    ephemeral storage.
    """

    OS = "OS"
    """Kubelet will use the OS disk for its data."""
    TEMPORARY = "Temporary"
    """Kubelet will use the temporary disk for its data."""


class LicenseType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The license type to use for Windows VMs. See `Azure Hybrid User Benefits
    <https://azure.microsoft.com/pricing/hybrid-benefit/faq/>`_ for more details.
    """

    NONE = "None"
    """No additional licensing is applied."""
    WINDOWS_SERVER = "Windows_Server"
    """Enables Azure Hybrid User Benefits for Windows VMs."""


class LoadBalancerSku(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The default is 'standard'. See `Azure Load Balancer SKUs
    <https://docs.microsoft.com/azure/load-balancer/skus>`_ for more information about the
    differences between load balancer SKUs.
    """

    STANDARD = "standard"
    """Use a a standard Load Balancer. This is the recommended Load Balancer SKU. For more information
    #: about on working with the load balancer in the managed cluster, see the `standard Load Balancer
    #: <https://docs.microsoft.com/azure/aks/load-balancer-standard>`_ article."""
    BASIC = "basic"
    """Use a basic Load Balancer with limited functionality."""


class ManagedClusterPodIdentityProvisioningState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The current provisioning state of the pod identity."""

    ASSIGNED = "Assigned"
    CANCELED = "Canceled"
    DELETING = "Deleting"
    FAILED = "Failed"
    SUCCEEDED = "Succeeded"
    UPDATING = "Updating"


class ManagedClusterSKUName(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The name of a managed cluster SKU."""

    BASE = "Base"
    """Base option for the AKS control plane."""


class ManagedClusterSKUTier(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """If not specified, the default is 'Free'. See `AKS Pricing Tier
    <https://learn.microsoft.com/azure/aks/free-standard-pricing-tiers>`_ for more details.
    """

    STANDARD = "Standard"
    """Recommended for mission-critical and production workloads. Includes Kubernetes control plane
    #: autoscaling, workload-intensive testing, and up to 5,000 nodes per cluster. Guarantees 99.95%
    #: availability of the Kubernetes API server endpoint for clusters that use Availability Zones and
    #: 99.9% of availability for clusters that don't use Availability Zones."""
    FREE = "Free"
    """The cluster management is free, but charged for VM, storage, and networking usage. Best for
    #: experimenting, learning, simple testing, or workloads with fewer than 10 nodes. Not recommended
    #: for production use cases."""


class NetworkDataplane(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Network dataplane used in the Kubernetes cluster."""

    AZURE = "azure"
    """Use Azure network dataplane."""
    CILIUM = "cilium"
    """Use Cilium network dataplane. See `Azure CNI Powered by Cilium
    #: <https://learn.microsoft.com/azure/aks/azure-cni-powered-by-cilium>`_ for more information."""


class NetworkMode(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """This cannot be specified if networkPlugin is anything other than 'azure'."""

    TRANSPARENT = "transparent"
    """No bridge is created. Intra-VM Pod to Pod communication is through IP routes created by Azure
    #: CNI. See `Transparent Mode <https://docs.microsoft.com/azure/aks/faq#transparent-mode>`_ for
    #: more information."""
    BRIDGE = "bridge"
    """This is no longer supported"""


class NetworkPlugin(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Network plugin used for building the Kubernetes network."""

    AZURE = "azure"
    """Use the Azure CNI network plugin. See `Azure CNI (advanced) networking
    #: <https://docs.microsoft.com/azure/aks/concepts-network#azure-cni-advanced-networking>`_ for
    #: more information."""
    KUBENET = "kubenet"
    """Use the Kubenet network plugin. See `Kubenet (basic) networking
    #: <https://docs.microsoft.com/azure/aks/concepts-network#kubenet-basic-networking>`_ for more
    #: information."""
    NONE = "none"
    """No CNI plugin is pre-installed. See `BYO CNI
    #: <https://docs.microsoft.com/en-us/azure/aks/use-byo-cni>`_ for more information."""


class NetworkPluginMode(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The mode the network plugin should use."""

    OVERLAY = "overlay"
    """Used with networkPlugin=azure, pods are given IPs from the PodCIDR address space but use Azure
    #: Routing Domains rather than Kubenet's method of route tables. For more information visit
    #: https://aka.ms/aks/azure-cni-overlay."""


class NetworkPolicy(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Network policy used for building the Kubernetes network."""

    CALICO = "calico"
    """Use Calico network policies. See `differences between Azure and Calico policies
    #: <https://docs.microsoft.com/azure/aks/use-network-policies#differences-between-azure-and-calico-policies-and-their-capabilities>`_
    #: for more information."""
    AZURE = "azure"
    """Use Azure network policies. See `differences between Azure and Calico policies
    #: <https://docs.microsoft.com/azure/aks/use-network-policies#differences-between-azure-and-calico-policies-and-their-capabilities>`_
    #: for more information."""
    CILIUM = "cilium"
    """Use Cilium to enforce network policies. This requires networkDataplane to be 'cilium'."""


class OSDiskType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The default is 'Ephemeral' if the VM supports it and has a cache disk larger than the requested
    OSDiskSizeGB. Otherwise, defaults to 'Managed'. May not be changed after creation. For more
    information see `Ephemeral OS
    <https://docs.microsoft.com/azure/aks/cluster-configuration#ephemeral-os>`_.
    """

    MANAGED = "Managed"
    """Azure replicates the operating system disk for a virtual machine to Azure storage to avoid data
    #: loss should the VM need to be relocated to another host. Since containers aren't designed to
    #: have local state persisted, this behavior offers limited value while providing some drawbacks,
    #: including slower node provisioning and higher read/write latency."""
    EPHEMERAL = "Ephemeral"
    """Ephemeral OS disks are stored only on the host machine, just like a temporary disk. This
    #: provides lower read/write latency, along with faster node scaling and cluster upgrades."""


class OSSKU(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Specifies the OS SKU used by the agent pool. The default is Ubuntu if OSType is Linux. The
    default is Windows2019 when Kubernetes <= 1.24 or Windows2022 when Kubernetes >= 1.25 if OSType
    is Windows.
    """

    UBUNTU = "Ubuntu"
    CBL_MARINER = "CBLMariner"
    WINDOWS2019 = "Windows2019"
    WINDOWS2022 = "Windows2022"


class OSType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The operating system type. The default is Linux."""

    LINUX = "Linux"
    """Use Linux."""
    WINDOWS = "Windows"
    """Use Windows."""


class OutboundType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """This can only be set at cluster creation time and cannot be changed later. For more information
    see `egress outbound type <https://docs.microsoft.com/azure/aks/egress-outboundtype>`_.
    """

    LOAD_BALANCER = "loadBalancer"
    """The load balancer is used for egress through an AKS assigned public IP. This supports
    #: Kubernetes services of type 'loadBalancer'. For more information see `outbound type
    #: loadbalancer
    #: <https://docs.microsoft.com/azure/aks/egress-outboundtype#outbound-type-of-loadbalancer>`_."""
    USER_DEFINED_ROUTING = "userDefinedRouting"
    """Egress paths must be defined by the user. This is an advanced scenario and requires proper
    #: network configuration. For more information see `outbound type userDefinedRouting
    #: <https://docs.microsoft.com/azure/aks/egress-outboundtype#outbound-type-of-userdefinedrouting>`_."""
    MANAGED_NAT_GATEWAY = "managedNATGateway"
    """The AKS-managed NAT gateway is used for egress."""
    USER_ASSIGNED_NAT_GATEWAY = "userAssignedNATGateway"
    """The user-assigned NAT gateway associated to the cluster subnet is used for egress. This is an
    #: advanced scenario and requires proper network configuration."""


class PrivateEndpointConnectionProvisioningState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The current provisioning state."""

    CANCELED = "Canceled"
    CREATING = "Creating"
    DELETING = "Deleting"
    FAILED = "Failed"
    SUCCEEDED = "Succeeded"


class PublicNetworkAccess(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Allow or deny public network access for AKS."""

    ENABLED = "Enabled"
    DISABLED = "Disabled"


class ResourceIdentityType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """For more information see `use managed identities in AKS
    <https://docs.microsoft.com/azure/aks/use-managed-identity>`_.
    """

    SYSTEM_ASSIGNED = "SystemAssigned"
    """Use an implicitly created system assigned managed identity to manage cluster resources. Master
    #: components in the control plane such as kube-controller-manager will use the system assigned
    #: managed identity to manipulate Azure resources."""
    USER_ASSIGNED = "UserAssigned"
    """Use a user-specified identity to manage cluster resources. Master components in the control
    #: plane such as kube-controller-manager will use the specified user assigned managed identity to
    #: manipulate Azure resources."""
    NONE = "None"
    """Do not use a managed identity for the Managed Cluster, service principal will be used instead."""


class ScaleDownMode(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Describes how VMs are added to or removed from Agent Pools. See `billing states
    <https://docs.microsoft.com/azure/virtual-machines/states-billing>`_.
    """

    DELETE = "Delete"
    """Create new instances during scale up and remove instances during scale down."""
    DEALLOCATE = "Deallocate"
    """Attempt to start deallocated instances (if they exist) during scale up and deallocate instances
    #: during scale down."""


class ScaleSetEvictionPolicy(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The eviction policy specifies what to do with the VM when it is evicted. The default is Delete.
    For more information about eviction see `spot VMs
    <https://docs.microsoft.com/azure/virtual-machines/spot-vms>`_.
    """

    DELETE = "Delete"
    """Nodes in the underlying Scale Set of the node pool are deleted when they're evicted."""
    DEALLOCATE = "Deallocate"
    """Nodes in the underlying Scale Set of the node pool are set to the stopped-deallocated state
    #: upon eviction. Nodes in the stopped-deallocated state count against your compute quota and can
    #: cause issues with cluster scaling or upgrading."""


class ScaleSetPriority(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The Virtual Machine Scale Set priority."""

    SPOT = "Spot"
    """Spot priority VMs will be used. There is no SLA for spot nodes. See `spot on AKS
    #: <https://docs.microsoft.com/azure/aks/spot-node-pool>`_ for more information."""
    REGULAR = "Regular"
    """Regular VMs will be used."""


class SnapshotType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The type of a snapshot. The default is NodePool."""

    NODE_POOL = "NodePool"
    """The snapshot is a snapshot of a node pool."""


class UpgradeChannel(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """For more information see `setting the AKS cluster auto-upgrade channel
    <https://docs.microsoft.com/azure/aks/upgrade-cluster#set-auto-upgrade-channel>`_.
    """

    RAPID = "rapid"
    """Automatically upgrade the cluster to the latest supported patch release on the latest supported
    #: minor version. In cases where the cluster is at a version of Kubernetes that is at an N-2 minor
    #: version where N is the latest supported minor version, the cluster first upgrades to the latest
    #: supported patch version on N-1 minor version. For example, if a cluster is running version
    #: 1.17.7 and versions 1.17.9, 1.18.4, 1.18.6, and 1.19.1 are available, your cluster first is
    #: upgraded to 1.18.6, then is upgraded to 1.19.1."""
    STABLE = "stable"
    """Automatically upgrade the cluster to the latest supported patch release on minor version N-1,
    #: where N is the latest supported minor version. For example, if a cluster is running version
    #: 1.17.7 and versions 1.17.9, 1.18.4, 1.18.6, and 1.19.1 are available, your cluster is upgraded
    #: to 1.18.6."""
    PATCH = "patch"
    """Automatically upgrade the cluster to the latest supported patch version when it becomes
    #: available while keeping the minor version the same. For example, if a cluster is running
    #: version 1.17.7 and versions 1.17.9, 1.18.4, 1.18.6, and 1.19.1 are available, your cluster is
    #: upgraded to 1.17.9."""
    NODE_IMAGE = "node-image"
    """Automatically upgrade the node image to the latest version available. Microsoft provides
    #: patches and new images for image nodes frequently (usually weekly), but your running nodes
    #: won't get the new images unless you do a node image upgrade. Turning on the node-image channel
    #: will automatically update your node images whenever a new version is available."""
    NONE = "none"
    """Disables auto-upgrades and keeps the cluster at its current version of Kubernetes."""


class WeekDay(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The weekday enum."""

    SUNDAY = "Sunday"
    MONDAY = "Monday"
    TUESDAY = "Tuesday"
    WEDNESDAY = "Wednesday"
    THURSDAY = "Thursday"
    FRIDAY = "Friday"
    SATURDAY = "Saturday"


class WorkloadRuntime(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Determines the type of workload a node can run."""

    OCI_CONTAINER = "OCIContainer"
    """Nodes will use Kubelet to run standard OCI container workloads."""
    WASM_WASI = "WasmWasi"
    """Nodes will use Krustlet to run WASM workloads using the WASI provider (Preview)."""
