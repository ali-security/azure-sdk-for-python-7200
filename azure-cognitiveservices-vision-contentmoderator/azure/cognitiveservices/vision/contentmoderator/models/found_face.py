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


class FoundFace(Model):
    """Coordinates to the found face.

    :param bottom: The bottom coordinate.
    :type bottom: int
    :param left: The left coordinate.
    :type left: int
    :param right: The right coordinate.
    :type right: int
    :param top: The top coordinate.
    :type top: int
    """

    _attribute_map = {
        'bottom': {'key': 'bottom', 'type': 'int'},
        'left': {'key': 'left', 'type': 'int'},
        'right': {'key': 'right', 'type': 'int'},
        'top': {'key': 'top', 'type': 'int'},
    }

    def __init__(self, bottom=None, left=None, right=None, top=None):
        self.bottom = bottom
        self.left = left
        self.right = right
        self.top = top
