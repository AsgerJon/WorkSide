"""WorkSide - Paint - Color
Class representation of colors"""
#  Copyright (c) 2023 Asger Jon Vistisen
#  MIT Licence
from __future__ import annotations

import json
from typing import Any
from warnings import warn

from icecream import ic
from worktoy.descriptors import DataField
from worktoy.worktoyclass import WorkToyClass

ic.configureOutput(includeContext=True)


class UsedArg:
  """Used to indicate that a positional argument has already been used."""

  def __init__(self, originalArg: Any) -> None:
    self._originalArg = originalArg

  def getOriginalArg(self) -> Any:
    """Getter-function for the original argument. """
    return self._originalArg


class ColorField(WorkToyClass):
  """WorkSide - Paint - Color
  Class representation of colors"""

  @classmethod
  def BLACK(cls) -> ColorField:
    """Standard color"""
    return cls(0, 0, 0)

  @classmethod
  def GREY(cls) -> ColorField:
    """Standard color"""
    return cls(191, 191, 191)

  @classmethod
  def ORANGE(cls) -> ColorField:
    """Standard color"""
    return cls(255, 144, 0, 255)

  @classmethod
  def MINT(cls) -> ColorField:
    """Standard color"""
    return cls(0, 255, 144, 255)

  @classmethod
  def PURPLE(cls) -> ColorField:
    """Standard color"""
    return cls(144, 0, 255, 255)

  @classmethod
  def LIME(cls) -> ColorField:
    """Standard color"""
    return cls(144, 255, 0, 255)

  @classmethod
  def ROYALBLUE(cls) -> ColorField:
    """Standard color"""
    return cls(0, 144, 255, 255)

  @classmethod
  def PINK(cls) -> ColorField:
    """Standard color"""
    return cls(255, 0, 144, 255)

  @classmethod
  def RED(cls) -> ColorField:
    """Standard color"""
    return cls(255, 0, 0, 255)

  @classmethod
  def GREEN(cls) -> ColorField:
    """Standard color"""
    return cls(0, 255, 0, 255)

  @classmethod
  def BLUE(cls) -> ColorField:
    """Standard color"""
    return cls(0, 0, 255, 255)

  @classmethod
  def MAGENTA(cls) -> ColorField:
    """Standard color"""
    return cls(255, 0, 255, 255)

  @classmethod
  def CYAN(cls) -> ColorField:
    """Standard color"""
    return cls(0, 255, 255, 255)

  @classmethod
  def YELLOW(cls) -> ColorField:
    """Standard color"""
    return cls(255, 255, 0, 255)

  red = DataField(0)
  green = DataField(0)
  blue = DataField(0)
  alpha = DataField(255)

  def hexify(self, uint8: int) -> str:
    """Returns a string representation of the value given in HEX code."""
    H = self.stringList('0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E, F')
    return '%s%s' % (H[int(uint8 // 16)], H[int(uint8 % 16)])

  def __str__(self, ) -> str:
    red = self.hexify(self.red)
    green = self.hexify(self.green)
    blue = self.hexify(self.blue)
    alpha = self.hexify(self.alpha)
    if self.alpha < 255:
      return '#%s%s%s%s' % (red, green, blue, alpha)
    return '#%s%s%s' % (red, green, blue,)

  def __repr__(self, ) -> str:
    if self.alpha < 255:
      red, green, blue, alpha = self.red, self.green, self.blue, self.alpha
      return 'Color(%s, %s, %s, %s)' % (red, green, blue, alpha)

  def encode(self) -> str:
    """ENCODER"""
    return json.dumps(dict(red=self.red, green=self.green, blue=self.blue,
                           alpha=self.alpha))

  def decode(self: Any, dataStr: Any = None) -> Any:
    """DECODER"""
    if isinstance(dataStr, str):
      data = json.loads(dataStr)
      red = data.get('red', 0)
      green = data.get('green', 0)
      blue = data.get('blue', 0)
      alpha = data.get('alpha', 255)
      self.red, self.green, self.blue, self.alpha = red, green, blue, alpha
    else:
      if isinstance(self, str) and dataStr is None:
        obj = ColorField()
        obj.decode(self)
        return obj
