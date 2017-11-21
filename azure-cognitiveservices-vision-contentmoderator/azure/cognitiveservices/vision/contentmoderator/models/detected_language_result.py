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


class DetectedLanguageResult(Model):
    """Detect language result.

    :param detected_language: The detected language.
    :type detected_language: str
    :param status: The detect language status
    :type status:
     ~azure.cognitiveservices.vision.contentmoderator.models.ResponseStatus
    :param tracking_id: The tracking id.
    :type tracking_id: str
    """

    _attribute_map = {
        'detected_language': {'key': 'detectedLanguage', 'type': 'str'},
        'status': {'key': 'status', 'type': 'ResponseStatus'},
        'tracking_id': {'key': 'trackingId', 'type': 'str'},
    }

    def __init__(self, detected_language=None, status=None, tracking_id=None):
        self.detected_language = detected_language
        self.status = status
        self.tracking_id = tracking_id
