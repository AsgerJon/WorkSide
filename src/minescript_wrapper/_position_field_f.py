"""MinescriptWrapper - PointFieldF
PointF valued descriptor implementation."""
#  MIT Licence
#  Copyright (c) 2023 Asger Jon Vistisen
from __future__ import annotations

from mineside.minescript_wrapper import PositionF
from mineside.worktoy.fields import AbstractField, TypedAttribute


class PositionFieldF(TypedAttribute):
  """MinescriptWrapper - PointField
  Point valued descriptor implementation."""

  def __init__(self, *args, **kwargs) -> None:
    AbstractField.__init__(self, *args, **kwargs)
    self._defaultValue = PositionF(0, 63, 0, )
    self._type = type(self._defaultValue)
