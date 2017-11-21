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


class AddImage(Model):
    """Add Image Response.

    :param content_id: Content Id.
    :type content_id: str
    :param additional_info: Advanced info list.
    :type additional_info:
     list[~azure.cognitiveservices.vision.contentmoderator.models.AddImageAdditionalInfoItem]
    :param status: Add image response status.
    :type status:
     ~azure.cognitiveservices.vision.contentmoderator.models.AddGetRefreshStatus
    :param tracking_id: Tracking Id.
    :type tracking_id: str
    """

    _attribute_map = {
        'content_id': {'key': 'contentId', 'type': 'str'},
        'additional_info': {'key': 'additionalInfo', 'type': '[AddImageAdditionalInfoItem]'},
        'status': {'key': 'status', 'type': 'AddGetRefreshStatus'},
        'tracking_id': {'key': 'trackingId', 'type': 'str'},
    }

    def __init__(self, content_id=None, additional_info=None, status=None, tracking_id=None):
        self.content_id = content_id
        self.additional_info = additional_info
        self.status = status
        self.tracking_id = tracking_id
