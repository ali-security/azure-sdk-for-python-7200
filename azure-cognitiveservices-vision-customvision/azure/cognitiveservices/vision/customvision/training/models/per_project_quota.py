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


class PerProjectQuota(Model):
    """Represents a set of quotas for a given project.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar project_id: Gets the project id of the project this quota applies to
    :vartype project_id: str
    :ivar iterations: Gets the iteration quota for the project
    :vartype iterations:
     ~azure.cognitiveservices.vision.customvision.training.models.Quota
    :ivar images: Gets the image quota for the project
    :vartype images:
     ~azure.cognitiveservices.vision.customvision.training.models.Quota
    :ivar tags: Gets the tag quota for the project
    :vartype tags:
     ~azure.cognitiveservices.vision.customvision.training.models.Quota
    """

    _validation = {
        'project_id': {'readonly': True},
        'iterations': {'readonly': True},
        'images': {'readonly': True},
        'tags': {'readonly': True},
    }

    _attribute_map = {
        'project_id': {'key': 'ProjectId', 'type': 'str'},
        'iterations': {'key': 'Iterations', 'type': 'Quota'},
        'images': {'key': 'Images', 'type': 'Quota'},
        'tags': {'key': 'Tags', 'type': 'Quota'},
    }

    def __init__(self):
        super(PerProjectQuota, self).__init__()
        self.project_id = None
        self.iterations = None
        self.images = None
        self.tags = None
