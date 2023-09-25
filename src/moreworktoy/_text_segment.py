"""WorkToy - Core - TextSegment
Text segment containing text."""
#  MIT Licence
#  Copyright (c) 2023 Asger Jon Vistisen
from __future__ import annotations

from worktoy.descriptors import Attribute
from worktoy.settings import Align
from worktoy.texttools import AbstractSegment


class TextSegment(AbstractSegment):
  """DOCSTRING"""

  innerLen = Attribute()
  outerLen = Attribute()
  currentText = Attribute()
  alignment = Attribute(Align.LeftTop)

  def __init__(self, *args, **kwargs) -> None:
    AbstractSegment.__init__(self, *args, **kwargs)

  def getInnerSize(self) -> int:
    """Getter function for the max length of innerSize"""

  def getOuterSize(self) -> int:
    """Getter-function for the max length of outerSize"""

  def getMinSize(self) -> int:
    """Getter-function for minimum size"""
    return 8

  def getMaxSize(self) -> int:
    """Getter-function for maximum size"""
    return 2 ** 16

  def render(self, n: int = None) -> str:
    """Abstract method responsible for rendering a segment on a line."""

  def reflect(self, n: int = None, ) -> str:
    """Returns this segment reversed. If this operation is not supported,
    the instance raises an exception."""
    return self.render(n)

  def __len__(self) -> int:
    """Returns the length of the current text"""
    return len(self.currentText)
