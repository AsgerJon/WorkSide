"""MinescriptWrapper - PointF
Float valued location in the minecraft world."""
#  MIT Licence
#  Copyright (c) 2023 Asger Jon Vistisen
from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from mineside.worktoy.base import DefaultClass
from mineside.worktoy.fields import FloatAttribute
from mineside.minescript_wrapper import Position

if TYPE_CHECKING:
  pass


class PositionF(DefaultClass):
  """Class representation of location in the world as floats"""

  x = FloatAttribute()
  y = FloatAttribute()
  z = FloatAttribute()

  @staticmethod
  def parseIntsFloats(*args) -> Optional[tuple[float, float, float]]:
    """Parses float values."""
    x, y, z = None, None, None
    vals = []
    for arg in args:
      if isinstance(arg, (int, float)):
        vals.append(float(arg))
    if len(vals) > 2:
      x, y, z = vals[:3]
      return (x, y, z)

  @staticmethod
  def parsePositions(*args) -> Optional[tuple[float, float, float]]:
    """Parses position values."""
    for arg in args:
      if isinstance(arg, Position):
        return (float(arg.x), float(arg.y), float(arg.z),)
      if isinstance(arg, PositionF):
        return (arg.x, arg.y, arg.z)

  def __init__(self, *args, **kwargs) -> None:
    DefaultClass.__init__(self, *args, **kwargs)
    vals = self.parsePositions(*args)
    nums = self.parseIntsFloats(*args)
    self.x, self.y, self.z = .0, 63., .0
    if vals:
      self.x, self.y, self.z = vals
    elif nums:
      self.x, self.y, self.z = nums

  def asPoint(self) -> Position:
    """Converts to float valued version."""
    from minescript_wrapper import Position
    return Position(int(self.x), int(self.y), int(self.z))
