"""WorkToy - Core - FlexFill
Code writing assistant"""
#  MIT Licence
#  Copyright (c) 2023 Asger Jon Vistisen
from __future__ import annotations

from abc import abstractmethod

from worktoy.descriptors import Attribute
from worktoy.texttools import AbstractSegment


class FlexFill(AbstractSegment):
  """WorkToy - Core - FlexFill
  Code writing assistant"""

  firstChar = Attribute(1)
  lastChar = Attribute(1)
  fillChar = Attribute(' ')

  def __init__(self, startLim: str, endLim: str, fillChar: str = None,
               *args, **kwargs) -> None:
    AbstractSegment.__init__(self, *args, **kwargs)
    fillChar = self.maybe(fillChar, ' ')
    self.firstChar = startLim
    self.lastChar = endLim

  def render(self, n: int) -> str:
    """Abstract method responsible for rendering a segment on a line."""
    if n < self.minSize:
      raise ValueError
    return '%s%s%s' % (self.firstChar, self.getFill(n), self.lastChar)

  def getFill(self, n: int) -> str:
    """Getter-function for n characters of fill"""
    fillNum = n - self.minSize
    lenFill = len(self.fillChar)
    wholeFills = int(fillNum // lenFill)
    partialFill = fillNum % lenFill
    return wholeFills * self.fillChar + self.fillChar[:partialFill]

  def reflect(self, n: int) -> str:
    """Returns this segment reversed. If this operation is not supported,
    the instance raises an exception."""
    if n < self.minSize:
      raise ValueError
    return '%s%s%s' % (self.lastChar, self.getFill(n), self.firstChar)

  def getMinSize(self) -> int:
    """Minimum size"""
    return len(self.firstChar + self.lastChar)

  def getMaxSize(self) -> int:
    """Maximum size"""
    return 2 ** 16
