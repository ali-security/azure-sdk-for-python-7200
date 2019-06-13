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

from msrest.service_client import SDKClient
from msrest import Serializer, Deserializer

from azure.profiles import KnownProfiles, ProfileDefinition
from azure.profiles.multiapiclient import MultiApiClientMixin
from .version import VERSION
from ._configuration import {{ client_name }}Configuration
{% if mixin_operations %}from ._operations_mixin import {{ client_name }}OperationsMixin{% endif %}


class {{ client_name }}({% if mixin_operations %}{{ client_name }}OperationsMixin, {% endif %}MultiApiClientMixin, SDKClient):
    """{{ client_doc }}

    This ready contains multiple API versions, to help you deal with all Azure clouds
    (Azure Stack, Azure Government, Azure China, etc.).
    By default, uses latest API version available on public Azure.
    For production, you should stick a particular api-version and/or profile.
    The profile sets a mapping between the operation group and an API version.
    The api-version parameter sets the default API version if the operation
    group is not described in the profile.

    :ivar config: Configuration for client.
    :vartype config: {{ client_name }}Configuration

    :param credentials: Credentials needed for the client to connect to Azure.
    :type credentials: :mod:`A msrestazure Credentials
     object<msrestazure.azure_active_directory>`
    :param subscription_id: Subscription credentials which uniquely identify
     Microsoft Azure subscription. The subscription ID forms part of the URI
     for every service call.
    :type subscription_id: str
    :param str api_version: API version to use if no profile is provided, or if
     missing in profile.
    :param str base_url: Service URL
    :param profile: A profile definition, from KnownProfiles to dict.
    :type profile: azure.profiles.KnownProfiles
    """

    DEFAULT_API_VERSION = '{{ last_api_version }}'
    _PROFILE_TAG = "{{ module_name }}.{{ client_name }}"
    LATEST_PROFILE = ProfileDefinition({
        _PROFILE_TAG: {
            None: DEFAULT_API_VERSION,
{%- for rt_name, api_version in last_rt_list|dictsort %}
            '{{ rt_name }}': '{{ api_version }}',
{%- endfor %}
        }},
        _PROFILE_TAG + " latest"
    )

    def __init__(self, credentials, subscription_id, api_version=None, base_url=None, profile=KnownProfiles.default):
        self.config = {{ client_name }}Configuration(credentials, subscription_id, base_url)
        super({{ client_name }}, self).__init__(
            credentials,
            self.config,
            api_version=api_version,
            profile=profile
        )

    @classmethod
    def _models_dict(cls, api_version):
        return {k: v for k, v in cls.models(api_version).__dict__.items() if isinstance(v, type)}

    @classmethod
    def models(cls, api_version=DEFAULT_API_VERSION):
        """Module depends on the API version:
{% for mod_api_version, api_version in mod_to_api_version|dictsort %}
           * {{ api_version }}: :mod:`{{ mod_api_version }}.models<{{ module_name }}.{{ mod_api_version }}.models>`
{%- endfor %}
        """
{%- for mod_api_version, api_version in mod_to_api_version|dictsort %}
        {% if not loop.first %}el{% endif %}if api_version == '{{ api_version }}':
            from .{{ mod_api_version }} import models
            return models
{%- endfor %}
        raise NotImplementedError("APIVersion {} is not available".format(api_version))
{% for operation_name, available_apis in operations|dictsort %}
    @property
    def {{ operation_name }}(self):
        """Instance depends on the API version:
{% for api in available_apis %}
           * {{ mod_to_api_version[api[0]] }}: :class:`{{ api[1] }}<{{ module_name }}.{{ api[0] }}.operations.{{ api[1] }}>`
{%- endfor %}
        """
        api_version = self._get_api_version('{{ operation_name }}')
{%- for api in available_apis %}
        {% if not loop.first %}el{% endif %}if api_version == '{{ mod_to_api_version[api[0]] }}':
            from .{{ api[0] }}.operations import {{ api[1] }} as OperationClass
{%- endfor %}
        else:
            raise NotImplementedError("APIVersion {} is not available".format(api_version))
        return OperationClass(self._client, self.config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))
{% endfor %}