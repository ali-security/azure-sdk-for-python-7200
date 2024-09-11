#!/usr/bin/env python

# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from typing import List, Optional, NamedTuple, Protocol, runtime_checkable, Union

class BreakingChange(NamedTuple):
    message: str
    change_type: str
    module: str
    class_name: Optional[str] = None
    function_name: Optional[str] = None
    parameter_name: Optional[str] = None

class Suppression(NamedTuple):
    change_type: str
    module: str
    class_name: Optional[str] = None
    function_name: Optional[str] = None
    parameter_or_property_name: Optional[str] = None

class CheckerType:
    MODULE = "module"
    CLASS = "class"
    FUNCTION_OR_METHOD = "function_or_method"

@runtime_checkable
class ChangesChecker(Protocol):
    node_type: CheckerType
    name: str
    is_breaking: bool
    message: Union[str, dict]

    def run_check(self, diff: dict, stable_nodes: dict, current_nodes: dict, **kwargs) -> List[BreakingChange]:
        ...
