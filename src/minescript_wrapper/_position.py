"""MinescriptWrapper - Point
Integer valued location in the minecraft world."""
#  MIT Licence
#  Copyright (c) 2023 Asger Jon Vistisen
from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from mineside.worktoy.base import DefaultClass
from mineside.worktoy.fields import IntAttribute

if TYPE_CHECKING:
  from minescript_wrapper import PositionF


class Position(DefaultClass):
  """Class representation of location in the world as ints"""

  x = IntAttribute()
  y = IntAttribute()
  z = IntAttribute()

  @staticmethod
  def parseIntsFloats(*args) -> Optional[tuple[int, int, int]]:
    """Parses float values."""
    x, y, z = None, None, None
    vals = []
    for arg in args:
      if isinstance(arg, (int, float)):
        vals.append(int(arg))
    if len(vals) > 2:
      x, y, z = vals[:3]
      return (x, y, z)

  @staticmethod
  def parsePositions(*args) -> Optional[tuple[int, int, int]]:
    """Parses position values."""
    for arg in args:
      if isinstance(arg, PositionF):
        return (int(arg.x), int(arg.y), int(arg.z),)
      if isinstance(arg, Position):
        return (arg.x, arg.y, arg.z)

  def __init__(self, *args, **kwargs) -> None:
    DefaultClass.__init__(self, *args, **kwargs)
    vals = self.parsePositions(*args)
    nums = self.parseIntsFloats(*args)
    self.x, self.y, self.z = 0, 63, 0
    if vals:
      self.x, self.y, self.z = vals
    elif nums:
      self.x, self.y, self.z = nums

  def asPointF(self) -> PositionF:
    """Converts to float valued version."""
    from minescript_wrapper import PositionF
    return PositionF(self.x, self.y, self.z)
