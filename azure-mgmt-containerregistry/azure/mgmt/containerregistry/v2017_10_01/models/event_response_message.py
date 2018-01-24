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


class EventResponseMessage(Model):
    """The event response message received from the service URI.

    :param content: The content of the event response message.
    :type content: str
    :param headers: The headers of the event response message.
    :type headers: dict[str, str]
    :param reason_phrase: The reason phrase of the event response message.
    :type reason_phrase: str
    :param status_code: The status code of the event response message.
    :type status_code: str
    :param version: The HTTP message version.
    :type version: str
    """

    _attribute_map = {
        'content': {'key': 'content', 'type': 'str'},
        'headers': {'key': 'headers', 'type': '{str}'},
        'reason_phrase': {'key': 'reasonPhrase', 'type': 'str'},
        'status_code': {'key': 'statusCode', 'type': 'str'},
        'version': {'key': 'version', 'type': 'str'},
    }

    def __init__(self, content=None, headers=None, reason_phrase=None, status_code=None, version=None):
        self.content = content
        self.headers = headers
        self.reason_phrase = reason_phrase
        self.status_code = status_code
        self.version = version
