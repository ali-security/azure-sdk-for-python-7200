# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft and contributors.  All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class EndpointUpdateParameters(Model):
    """
    Endpoint properties required for new endpoint creation.

    :param tags: Endpoint tags
    :type tags: dict
    :param origin_host_header: The host header the CDN provider will send
     along with content requests to origins. The default value is the host
     name of the origin.
    :type origin_host_header: str
    :param origin_path: The path used for origin requests.
    :type origin_path: str
    :param content_types_to_compress: List of content types on which
     compression will be applied. The value for the elements should be a
     valid MIME type.
    :type content_types_to_compress: list of str
    :param is_compression_enabled: Indicates whether content compression is
     enabled. Default value is false. If compression is enabled, the content
     transferred from the CDN endpoint to the end user will be compressed.
     The requested content must be larger than 1 byte and smaller than 1 MB.
    :type is_compression_enabled: bool
    :param is_http_allowed: Indicates whether HTTP traffic is allowed on the
     endpoint. Default value is true. At least one protocol (HTTP or HTTPS)
     must be allowed.
    :type is_http_allowed: bool
    :param is_https_allowed: Indicates whether HTTPS traffic is allowed on
     the endpoint. Default value is true. At least one protocol (HTTP or
     HTTPS) must be allowed.
    :type is_https_allowed: bool
    :param query_string_caching_behavior: Defines the query string caching
     behavior. Possible values include: 'IgnoreQueryString', 'BypassCaching',
     'UseQueryString', 'NotSet'
    :type query_string_caching_behavior: str
    """ 

    _attribute_map = {
        'tags': {'key': 'tags', 'type': '{str}'},
        'origin_host_header': {'key': 'properties.originHostHeader', 'type': 'str'},
        'origin_path': {'key': 'properties.originPath', 'type': 'str'},
        'content_types_to_compress': {'key': 'properties.contentTypesToCompress', 'type': '[str]'},
        'is_compression_enabled': {'key': 'properties.isCompressionEnabled', 'type': 'bool'},
        'is_http_allowed': {'key': 'properties.isHttpAllowed', 'type': 'bool'},
        'is_https_allowed': {'key': 'properties.isHttpsAllowed', 'type': 'bool'},
        'query_string_caching_behavior': {'key': 'properties.queryStringCachingBehavior', 'type': 'QueryStringCachingBehavior'},
    }

    def __init__(self, tags=None, origin_host_header=None, origin_path=None, content_types_to_compress=None, is_compression_enabled=None, is_http_allowed=None, is_https_allowed=None, query_string_caching_behavior=None, **kwargs):
        self.tags = tags
        self.origin_host_header = origin_host_header
        self.origin_path = origin_path
        self.content_types_to_compress = content_types_to_compress
        self.is_compression_enabled = is_compression_enabled
        self.is_http_allowed = is_http_allowed
        self.is_https_allowed = is_https_allowed
        self.query_string_caching_behavior = query_string_caching_behavior
