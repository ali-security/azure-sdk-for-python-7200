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

from azure.mgmt.core import ARMPipelineClient
from msrest import Serializer, Deserializer

from azure.profiles import KnownProfiles, ProfileDefinition
from azure.profiles.multiapiclient import MultiApiClientMixin
from ._configuration import ApplicationInsightsManagementClientConfiguration

class _SDKClient(object):
    def __init__(self, *args, **kwargs):
        """This is a fake class to support current implemetation of MultiApiClientMixin."
        Will be removed in final version of multiapi azure-core based client
        """
        pass

class ApplicationInsightsManagementClient(MultiApiClientMixin, _SDKClient):
    """Composite Swagger for Application Insights Management Client.

    This ready contains multiple API versions, to help you deal with all of the Azure clouds
    (Azure Stack, Azure Government, Azure China, etc.).
    By default, it uses the latest API version available on public Azure.
    For production, you should stick to a particular api-version and/or profile.
    The profile sets a mapping between an operation group and its API version.
    The api-version parameter sets the default API version if the operation
    group is not described in the profile.

    :param credential: Credential needed for the client to connect to Azure.
    :type credential: ~azure.core.credentials.TokenCredential
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param str api_version: API version to use if no profile is provided, or if
     missing in profile.
    :param str base_url: Service URL
    :param profile: A profile definition, from KnownProfiles to dict.
    :type profile: azure.profiles.KnownProfiles
    """

    DEFAULT_API_VERSION = '2017-10-01'
    _PROFILE_TAG = "azure.mgmt.applicationinsights.ApplicationInsightsManagementClient"
    LATEST_PROFILE = ProfileDefinition({
        _PROFILE_TAG: {
            None: DEFAULT_API_VERSION,
            'analytics_items': '2015-05-01',
            'annotations': '2015-05-01',
            'api_keys': '2015-05-01',
            'component_available_features': '2015-05-01',
            'component_current_billing_features': '2015-05-01',
            'component_feature_capabilities': '2015-05-01',
            'component_quota_status': '2015-05-01',
            'components': '2015-05-01',
            'export_configurations': '2015-05-01',
            'favorites': '2015-05-01',
            'my_workbooks': '2015-05-01',
            'operations': '2015-05-01',
            'proactive_detection_configurations': '2015-05-01',
            'web_test_locations': '2015-05-01',
            'web_tests': '2015-05-01',
            'work_item_configurations': '2015-05-01',
            'workbooks': '2015-05-01',
        }},
        _PROFILE_TAG + " latest"
    )

    def __init__(
        self,
        credential,  # type: "TokenCredential"
        subscription_id,  # type: str
        api_version=None,
        base_url=None,
        profile=KnownProfiles.default,
        **kwargs  # type: Any
    ):
        if not base_url:
            base_url = 'https://management.azure.com'
        self._config = ApplicationInsightsManagementClientConfiguration(credential, subscription_id, **kwargs)
        self._client = ARMPipelineClient(base_url=base_url, config=self._config, **kwargs)
        super(ApplicationInsightsManagementClient, self).__init__(
            api_version=api_version,
            profile=profile
        )

    @classmethod
    def _models_dict(cls, api_version):
        return {k: v for k, v in cls.models(api_version).__dict__.items() if isinstance(v, type)}

    @classmethod
    def models(cls, api_version=DEFAULT_API_VERSION):
        """Module depends on the API version:

           * 2015-05-01: :mod:`v2015_05_01.models<azure.mgmt.applicationinsights.v2015_05_01.models>`
           * 2017-10-01: :mod:`v2017_10_01.models<azure.mgmt.applicationinsights.v2017_10_01.models>`
           * 2018-05-01-preview: :mod:`v2018_05_01_preview.models<azure.mgmt.applicationinsights.v2018_05_01_preview.models>`
           * 2018-06-17-preview: :mod:`v2018_06_17_preview.models<azure.mgmt.applicationinsights.v2018_06_17_preview.models>`
           * 2019-09-01-preview: :mod:`v2019_09_01_preview.models<azure.mgmt.applicationinsights.v2019_09_01_preview.models>`
           * 2019-10-17-preview: :mod:`v2019_10_17_preview.models<azure.mgmt.applicationinsights.v2019_10_17_preview.models>`
           * 2020-06-02-preview: :mod:`v2020-06-02-preview.models<azure.mgmt.applicationinsights.v2020-06-02-preview.models>`
           * 2020-02-02-preview: :mod:`v2020_02_02_preview.models<azure.mgmt.applicationinsights.v2020_02_02_preview.models>`
           * 2020-03-01-preview: :mod:`v2020_03_01_preview.models<azure.mgmt.applicationinsights.v2020_03_01_preview.models>`
        """
        if api_version == '2015-05-01':
            from .v2015_05_01 import models
            return models
        elif api_version == '2017-10-01':
            from .v2017_10_01 import models
            return models
        elif api_version == '2018-05-01-preview':
            from .v2018_05_01_preview import models
            return models
        elif api_version == '2018-06-17-preview':
            from .v2018_06_17_preview import models
            return models
        elif api_version == '2019-09-01-preview':
            from .v2019_09_01_preview import models
            return models
        elif api_version == '2019-10-17-preview':
            from .v2019_10_17_preview import models
            return models
        elif api_version == '2020-06-02-preview':
            from .v2020-06-02-preview import models
            return models
        elif api_version == '2020-02-02-preview':
            from .v2020_02_02_preview import models
            return models
        elif api_version == '2020-03-01-preview':
            from .v2020_03_01_preview import models
            return models
        raise ValueError("API version {} is not available".format(api_version))

    @property
    def analytics_items(self):
        """Instance depends on the API version:

           * 2015-05-01: :class:`AnalyticsItemsOperations<azure.mgmt.applicationinsights.v2015_05_01.operations.AnalyticsItemsOperations>`
        """
        api_version = self._get_api_version('analytics_items')
        if api_version == '2015-05-01':
            from .v2015_05_01.operations import AnalyticsItemsOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'analytics_items'".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def annotations(self):
        """Instance depends on the API version:

           * 2015-05-01: :class:`AnnotationsOperations<azure.mgmt.applicationinsights.v2015_05_01.operations.AnnotationsOperations>`
        """
        api_version = self._get_api_version('annotations')
        if api_version == '2015-05-01':
            from .v2015_05_01.operations import AnnotationsOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'annotations'".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def api_keys(self):
        """Instance depends on the API version:

           * 2015-05-01: :class:`APIKeysOperations<azure.mgmt.applicationinsights.v2015_05_01.operations.APIKeysOperations>`
        """
        api_version = self._get_api_version('api_keys')
        if api_version == '2015-05-01':
            from .v2015_05_01.operations import APIKeysOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'api_keys'".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def component_available_features(self):
        """Instance depends on the API version:

           * 2015-05-01: :class:`ComponentAvailableFeaturesOperations<azure.mgmt.applicationinsights.v2015_05_01.operations.ComponentAvailableFeaturesOperations>`
        """
        api_version = self._get_api_version('component_available_features')
        if api_version == '2015-05-01':
            from .v2015_05_01.operations import ComponentAvailableFeaturesOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'component_available_features'".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def component_current_billing_features(self):
        """Instance depends on the API version:

           * 2015-05-01: :class:`ComponentCurrentBillingFeaturesOperations<azure.mgmt.applicationinsights.v2015_05_01.operations.ComponentCurrentBillingFeaturesOperations>`
        """
        api_version = self._get_api_version('component_current_billing_features')
        if api_version == '2015-05-01':
            from .v2015_05_01.operations import ComponentCurrentBillingFeaturesOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'component_current_billing_features'".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def component_current_pricing_plan(self):
        """Instance depends on the API version:

           * 2017-10-01: :class:`ComponentCurrentPricingPlanOperations<azure.mgmt.applicationinsights.v2017_10_01.operations.ComponentCurrentPricingPlanOperations>`
        """
        api_version = self._get_api_version('component_current_pricing_plan')
        if api_version == '2017-10-01':
            from .v2017_10_01.operations import ComponentCurrentPricingPlanOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'component_current_pricing_plan'".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def component_feature_capabilities(self):
        """Instance depends on the API version:

           * 2015-05-01: :class:`ComponentFeatureCapabilitiesOperations<azure.mgmt.applicationinsights.v2015_05_01.operations.ComponentFeatureCapabilitiesOperations>`
        """
        api_version = self._get_api_version('component_feature_capabilities')
        if api_version == '2015-05-01':
            from .v2015_05_01.operations import ComponentFeatureCapabilitiesOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'component_feature_capabilities'".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def component_linked_storage_accounts(self):
        """Instance depends on the API version:

           * 2020-03-01-preview: :class:`ComponentLinkedStorageAccountsOperations<azure.mgmt.applicationinsights.v2020_03_01_preview.operations.ComponentLinkedStorageAccountsOperations>`
        """
        api_version = self._get_api_version('component_linked_storage_accounts')
        if api_version == '2020-03-01-preview':
            from .v2020_03_01_preview.operations import ComponentLinkedStorageAccountsOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'component_linked_storage_accounts'".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def component_quota_status(self):
        """Instance depends on the API version:

           * 2015-05-01: :class:`ComponentQuotaStatusOperations<azure.mgmt.applicationinsights.v2015_05_01.operations.ComponentQuotaStatusOperations>`
        """
        api_version = self._get_api_version('component_quota_status')
        if api_version == '2015-05-01':
            from .v2015_05_01.operations import ComponentQuotaStatusOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'component_quota_status'".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def components(self):
        """Instance depends on the API version:

           * 2015-05-01: :class:`ComponentsOperations<azure.mgmt.applicationinsights.v2015_05_01.operations.ComponentsOperations>`
           * 2018-05-01-preview: :class:`ComponentsOperations<azure.mgmt.applicationinsights.v2018_05_01_preview.operations.ComponentsOperations>`
           * 2020-02-02-preview: :class:`ComponentsOperations<azure.mgmt.applicationinsights.v2020_02_02_preview.operations.ComponentsOperations>`
        """
        api_version = self._get_api_version('components')
        if api_version == '2015-05-01':
            from .v2015_05_01.operations import ComponentsOperations as OperationClass
        elif api_version == '2018-05-01-preview':
            from .v2018_05_01_preview.operations import ComponentsOperations as OperationClass
        elif api_version == '2020-02-02-preview':
            from .v2020_02_02_preview.operations import ComponentsOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'components'".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def ea_subscription_list_migration_date(self):
        """Instance depends on the API version:

           * 2017-10-01: :class:`EASubscriptionListMigrationDateOperations<azure.mgmt.applicationinsights.v2017_10_01.operations.EASubscriptionListMigrationDateOperations>`
        """
        api_version = self._get_api_version('ea_subscription_list_migration_date')
        if api_version == '2017-10-01':
            from .v2017_10_01.operations import EASubscriptionListMigrationDateOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'ea_subscription_list_migration_date'".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def ea_subscription_migrate_to_new_pricing_model(self):
        """Instance depends on the API version:

           * 2017-10-01: :class:`EASubscriptionMigrateToNewPricingModelOperations<azure.mgmt.applicationinsights.v2017_10_01.operations.EASubscriptionMigrateToNewPricingModelOperations>`
        """
        api_version = self._get_api_version('ea_subscription_migrate_to_new_pricing_model')
        if api_version == '2017-10-01':
            from .v2017_10_01.operations import EASubscriptionMigrateToNewPricingModelOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'ea_subscription_migrate_to_new_pricing_model'".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def ea_subscription_rollback_to_legacy_pricing_model(self):
        """Instance depends on the API version:

           * 2017-10-01: :class:`EASubscriptionRollbackToLegacyPricingModelOperations<azure.mgmt.applicationinsights.v2017_10_01.operations.EASubscriptionRollbackToLegacyPricingModelOperations>`
        """
        api_version = self._get_api_version('ea_subscription_rollback_to_legacy_pricing_model')
        if api_version == '2017-10-01':
            from .v2017_10_01.operations import EASubscriptionRollbackToLegacyPricingModelOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'ea_subscription_rollback_to_legacy_pricing_model'".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def export_configurations(self):
        """Instance depends on the API version:

           * 2015-05-01: :class:`ExportConfigurationsOperations<azure.mgmt.applicationinsights.v2015_05_01.operations.ExportConfigurationsOperations>`
        """
        api_version = self._get_api_version('export_configurations')
        if api_version == '2015-05-01':
            from .v2015_05_01.operations import ExportConfigurationsOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'export_configurations'".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def favorites(self):
        """Instance depends on the API version:

           * 2015-05-01: :class:`FavoritesOperations<azure.mgmt.applicationinsights.v2015_05_01.operations.FavoritesOperations>`
        """
        api_version = self._get_api_version('favorites')
        if api_version == '2015-05-01':
            from .v2015_05_01.operations import FavoritesOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'favorites'".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def live_token(self):
        """Instance depends on the API version:

           * 2020-06-02-preview: :class:`LiveTokenOperations<azure.mgmt.applicationinsights.v2020-06-02-preview.operations.LiveTokenOperations>`
        """
        api_version = self._get_api_version('live_token')
        if api_version == '2020-06-02-preview':
            from .v2020-06-02-preview.operations import LiveTokenOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'live_token'".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def my_workbooks(self):
        """Instance depends on the API version:

           * 2015-05-01: :class:`MyWorkbooksOperations<azure.mgmt.applicationinsights.v2015_05_01.operations.MyWorkbooksOperations>`
        """
        api_version = self._get_api_version('my_workbooks')
        if api_version == '2015-05-01':
            from .v2015_05_01.operations import MyWorkbooksOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'my_workbooks'".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def operations(self):
        """Instance depends on the API version:

           * 2015-05-01: :class:`Operations<azure.mgmt.applicationinsights.v2015_05_01.operations.Operations>`
           * 2019-09-01-preview: :class:`Operations<azure.mgmt.applicationinsights.v2019_09_01_preview.operations.Operations>`
           * 2020-06-02-preview: :class:`Operations<azure.mgmt.applicationinsights.v2020-06-02-preview.operations.Operations>`
        """
        api_version = self._get_api_version('operations')
        if api_version == '2015-05-01':
            from .v2015_05_01.operations import Operations as OperationClass
        elif api_version == '2019-09-01-preview':
            from .v2019_09_01_preview.operations import Operations as OperationClass
        elif api_version == '2020-06-02-preview':
            from .v2020-06-02-preview.operations import Operations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'operations'".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def proactive_detection_configurations(self):
        """Instance depends on the API version:

           * 2015-05-01: :class:`ProactiveDetectionConfigurationsOperations<azure.mgmt.applicationinsights.v2015_05_01.operations.ProactiveDetectionConfigurationsOperations>`
           * 2018-05-01-preview: :class:`ProactiveDetectionConfigurationsOperations<azure.mgmt.applicationinsights.v2018_05_01_preview.operations.ProactiveDetectionConfigurationsOperations>`
        """
        api_version = self._get_api_version('proactive_detection_configurations')
        if api_version == '2015-05-01':
            from .v2015_05_01.operations import ProactiveDetectionConfigurationsOperations as OperationClass
        elif api_version == '2018-05-01-preview':
            from .v2018_05_01_preview.operations import ProactiveDetectionConfigurationsOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'proactive_detection_configurations'".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def queries(self):
        """Instance depends on the API version:

           * 2019-09-01-preview: :class:`QueriesOperations<azure.mgmt.applicationinsights.v2019_09_01_preview.operations.QueriesOperations>`
        """
        api_version = self._get_api_version('queries')
        if api_version == '2019-09-01-preview':
            from .v2019_09_01_preview.operations import QueriesOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'queries'".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def query_packs(self):
        """Instance depends on the API version:

           * 2019-09-01-preview: :class:`QueryPacksOperations<azure.mgmt.applicationinsights.v2019_09_01_preview.operations.QueryPacksOperations>`
        """
        api_version = self._get_api_version('query_packs')
        if api_version == '2019-09-01-preview':
            from .v2019_09_01_preview.operations import QueryPacksOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'query_packs'".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def web_test_locations(self):
        """Instance depends on the API version:

           * 2015-05-01: :class:`WebTestLocationsOperations<azure.mgmt.applicationinsights.v2015_05_01.operations.WebTestLocationsOperations>`
        """
        api_version = self._get_api_version('web_test_locations')
        if api_version == '2015-05-01':
            from .v2015_05_01.operations import WebTestLocationsOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'web_test_locations'".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def web_tests(self):
        """Instance depends on the API version:

           * 2015-05-01: :class:`WebTestsOperations<azure.mgmt.applicationinsights.v2015_05_01.operations.WebTestsOperations>`
        """
        api_version = self._get_api_version('web_tests')
        if api_version == '2015-05-01':
            from .v2015_05_01.operations import WebTestsOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'web_tests'".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def work_item_configurations(self):
        """Instance depends on the API version:

           * 2015-05-01: :class:`WorkItemConfigurationsOperations<azure.mgmt.applicationinsights.v2015_05_01.operations.WorkItemConfigurationsOperations>`
        """
        api_version = self._get_api_version('work_item_configurations')
        if api_version == '2015-05-01':
            from .v2015_05_01.operations import WorkItemConfigurationsOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'work_item_configurations'".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def workbook_templates(self):
        """Instance depends on the API version:

           * 2019-10-17-preview: :class:`WorkbookTemplatesOperations<azure.mgmt.applicationinsights.v2019_10_17_preview.operations.WorkbookTemplatesOperations>`
        """
        api_version = self._get_api_version('workbook_templates')
        if api_version == '2019-10-17-preview':
            from .v2019_10_17_preview.operations import WorkbookTemplatesOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'workbook_templates'".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def workbooks(self):
        """Instance depends on the API version:

           * 2015-05-01: :class:`WorkbooksOperations<azure.mgmt.applicationinsights.v2015_05_01.operations.WorkbooksOperations>`
           * 2018-06-17-preview: :class:`WorkbooksOperations<azure.mgmt.applicationinsights.v2018_06_17_preview.operations.WorkbooksOperations>`
        """
        api_version = self._get_api_version('workbooks')
        if api_version == '2015-05-01':
            from .v2015_05_01.operations import WorkbooksOperations as OperationClass
        elif api_version == '2018-06-17-preview':
            from .v2018_06_17_preview.operations import WorkbooksOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'workbooks'".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    def close(self):
        self._client.close()
    def __enter__(self):
        self._client.__enter__()
        return self
    def __exit__(self, *exc_details):
        self._client.__exit__(*exc_details)
