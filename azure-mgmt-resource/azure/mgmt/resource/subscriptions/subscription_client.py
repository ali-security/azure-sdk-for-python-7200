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

from msrest.service_client import ServiceClient
from msrest import Serializer, Deserializer
from msrestazure import AzureConfiguration
from ..version import VERSION


class SubscriptionClientConfiguration(AzureConfiguration):
    """Configuration for SubscriptionClient
    Note that all parameters used to create this instance are saved as instance
    attributes.

    :param credentials: Credentials needed for the client to connect to Azure.
    :type credentials: :mod:`A msrestazure Credentials
     object<msrestazure.azure_active_directory>`
    :param str base_url: Service URL
    """

    def __init__(
            self, credentials, base_url=None):

        if credentials is None:
            raise ValueError("Parameter 'credentials' must not be None.")
        if not base_url:
            base_url = 'https://management.azure.com'

        super(SubscriptionClientConfiguration, self).__init__(base_url)

        self.add_user_agent('subscriptionclient/{}'.format(VERSION))
        self.add_user_agent('Azure-SDK-For-Python')

        self.credentials = credentials


class SubscriptionClient(object):
    """All resource groups and resources exist within subscriptions. These operation enable you get information about your subscriptions and tenants. A tenant is a dedicated instance of Azure Active Directory (Azure AD) for your organization.

    :ivar config: Configuration for client.
    :vartype config: SubscriptionClientConfiguration

    :ivar subscriptions: Subscriptions operations
    :vartype subscriptions: .operations.SubscriptionsOperations
    :ivar tenants: Tenants operations
    :vartype tenants: .operations.TenantsOperations

    :param credentials: Credentials needed for the client to connect to Azure.
    :type credentials: :mod:`A msrestazure Credentials
     object<msrestazure.azure_active_directory>`
    :param str base_url: Service URL
    """

    def __init__(
            self, credentials, api_version = '2016-06-01', base_url=None):

        self.config = SubscriptionClientConfiguration(credentials, base_url)
        self._client = ServiceClient(self.config.credentials, self.config)

        client_models = {k: v for k, v in self.models(api_version).__dict__.items() if isinstance(v, type)}
        self.api_version = api_version
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

    @classmethod
    def models(cls, api_version = '2016-06-01'):
        if api_version =='2016-06-01':
            from .v2016_06_01 import models
            return models
        else:
            raise NotImplementedError("APIVersion {} is not available".format(api_version))

    @property
    def subscriptions(self):
        if self.api_version =='2016-06-01':
            from .v2016_06_01.operations.subscriptions_operations import SubscriptionsOperations as OperationClass
        else:
            raise NotImplementedError("APIVersion {} is not available".format(self.api_version))
        return OperationClass(self._client, self.config, self._serialize, self._deserialize)

    @property
    def tenants(self):
        if self.api_version =='2016-06-01':
            from .v2016_06_01.operations.tenants_operations import TenantsOperations as OperationClass
        else:
            raise NotImplementedError("APIVersion {} is not available".format(self.api_version))
        return OperationClass(self._client, self.config, self._serialize, self._deserialize)