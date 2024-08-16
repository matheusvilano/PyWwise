# Copyright 2024 Matheus Vilano
# SPDX-License-Identifier: Apache-2.0

from pathlib import Path as _Path
from re import Pattern as _Pattern
from typing import (TypeAlias as _TypeAlias, TypeVar as _TypeVar, Union as _Union, List as _List, Tuple as _Tuple,
                    Set as _Set)

SystemPath: _TypeAlias = _Path
"""Represents a filesystem path."""

RegexPattern: _TypeAlias = _Pattern
"""Represents a Regex pattern."""

UnionType: _TypeVar = _TypeVar("UnionType", bound=_Union)
"""Type variable for Unions."""

ListOrTuple: _TypeAlias = _Union[_List[UnionType], _Tuple[UnionType, ...]]
"""Custom type representing both `List` and `Tuple`."""

ListOrTupleOrSet: _TypeAlias = _Union[_List[UnionType], _Tuple[UnionType, ...], _Set[UnionType]]
"""Custom type representing `List`, `Tuple`, and `Set`."""
