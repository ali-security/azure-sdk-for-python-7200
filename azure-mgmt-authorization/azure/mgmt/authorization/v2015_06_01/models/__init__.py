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

try:
    from .classic_administrator_py3 import ClassicAdministrator
except (SyntaxError, ImportError):
    from .classic_administrator import ClassicAdministrator
from .classic_administrator_paged import ClassicAdministratorPaged

__all__ = [
    'ClassicAdministrator',
    'ClassicAdministratorPaged',
]
