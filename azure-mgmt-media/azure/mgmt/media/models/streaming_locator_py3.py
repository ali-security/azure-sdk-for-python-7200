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

from .proxy_resource_py3 import ProxyResource


class StreamingLocator(ProxyResource):
    """A Streaming Locator resource.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Fully qualified resource ID for the resource.
    :vartype id: str
    :ivar name: The name of the resource.
    :vartype name: str
    :ivar type: The type of the resource.
    :vartype type: str
    :param asset_name: Required. Asset Name
    :type asset_name: str
    :ivar created: Creation time of Streaming Locator
    :vartype created: datetime
    :param start_time: StartTime of Streaming Locator
    :type start_time: datetime
    :param end_time: EndTime of Streaming Locator
    :type end_time: datetime
    :param streaming_locator_id: StreamingLocatorId of Streaming Locator
    :type streaming_locator_id: str
    :param streaming_policy_name: Required. Streaming policy name used by this
     streaming locator. Either specify the name of streaming policy you created
     or use one of the predefined streaming polices. The predefined streaming
     policies available are: 'Predefined_DownloadOnly',
     'Predefined_ClearStreamingOnly', 'Predefined_DownloadAndClearStreaming',
     'Predefined_ClearKey', 'Predefined_SecureStreaming' and
     'Predefined_SecureStreamingWithFairPlay'
    :type streaming_policy_name: str
    :param default_content_key_policy_name: Default ContentKeyPolicy used by
     this Streaming Locator
    :type default_content_key_policy_name: str
    :param content_keys: ContentKeys used by this Streaming Locator
    :type content_keys:
     list[~azure.mgmt.media.models.StreamingLocatorContentKey]
    :param alternative_media_id: An Alternative Media Identifier associated
     with the StreamingLocator.  This identifier can be used to distinguish
     different StreamingLocators for the same Asset for authorization purposes
     in the CustomLicenseAcquisitionUrlTemplate or the
     CustomKeyAcquisitionUrlTemplate of the StreamingPolicy specified in the
     StreamingPolicyName field.
    :type alternative_media_id: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'asset_name': {'required': True},
        'created': {'readonly': True},
        'streaming_policy_name': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'asset_name': {'key': 'properties.assetName', 'type': 'str'},
        'created': {'key': 'properties.created', 'type': 'iso-8601'},
        'start_time': {'key': 'properties.startTime', 'type': 'iso-8601'},
        'end_time': {'key': 'properties.endTime', 'type': 'iso-8601'},
        'streaming_locator_id': {'key': 'properties.streamingLocatorId', 'type': 'str'},
        'streaming_policy_name': {'key': 'properties.streamingPolicyName', 'type': 'str'},
        'default_content_key_policy_name': {'key': 'properties.defaultContentKeyPolicyName', 'type': 'str'},
        'content_keys': {'key': 'properties.contentKeys', 'type': '[StreamingLocatorContentKey]'},
        'alternative_media_id': {'key': 'properties.alternativeMediaId', 'type': 'str'},
    }

    def __init__(self, *, asset_name: str, streaming_policy_name: str, start_time=None, end_time=None, streaming_locator_id: str=None, default_content_key_policy_name: str=None, content_keys=None, alternative_media_id: str=None, **kwargs) -> None:
        super(StreamingLocator, self).__init__(**kwargs)
        self.asset_name = asset_name
        self.created = None
        self.start_time = start_time
        self.end_time = end_time
        self.streaming_locator_id = streaming_locator_id
        self.streaming_policy_name = streaming_policy_name
        self.default_content_key_policy_name = default_content_key_policy_name
        self.content_keys = content_keys
        self.alternative_media_id = alternative_media_id
