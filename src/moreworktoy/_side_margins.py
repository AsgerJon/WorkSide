"""WorkToy - Core - SideMargins
Creates a reversible margin for use in the sides"""
#  MIT Licence
#  Copyright (c) 2023 Asger Jon Vistisen
from __future__ import annotations

from worktoy.descriptors import Attribute
from worktoy.texttools import AbstractSegment


class SideMargins(AbstractSegment):
  """WorkToy - Core - SideMargins
  Creates a reversible margin for use in the sides"""

  def __init__(self, *args, **kwargs) -> None:
    AbstractSegment.__init__(self, *args, **kwargs)
    self._base = '  # | '
    self._fillChar = ' '

  def getMinSize(self) -> int:
    """Minimum size"""
    return len(self._base)

  def getMaxSize(self) -> int:
    return len(self._base)

  def render(self, n: int = None) -> str:
    """Returns the segment at the given length if it is in range of the
    supported sizes of this segment. """
    return self._base

  def reflect(self) -> str:
    """Reflects the margin"""
    return ''.join([c for c in reversed([k for k in self._base])])
