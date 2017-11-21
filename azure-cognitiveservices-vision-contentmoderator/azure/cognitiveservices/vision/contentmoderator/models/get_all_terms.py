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


class GetAllTerms(Model):
    """Gets all term Id response properties.

    :param data: Term data details.
    :type data:
     ~azure.cognitiveservices.vision.contentmoderator.models.TermData
    :param paging: Paging details.
    :type paging:
     ~azure.cognitiveservices.vision.contentmoderator.models.GetAllTermsPaging
    """

    _attribute_map = {
        'data': {'key': 'data', 'type': 'TermData'},
        'paging': {'key': 'paging', 'type': 'GetAllTermsPaging'},
    }

    def __init__(self, data=None, paging=None):
        self.data = data
        self.paging = paging
