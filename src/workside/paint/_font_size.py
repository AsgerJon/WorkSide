"""WorkSide - Paint - FontSize
Class representation of font size."""
#  Copyright (c) 2023 Asger Jon Vistisen
#  MIT Licence
from __future__ import annotations

from worktoy.descriptors import Field
from worktoy.worktoyclass import WorkToyClass


class FontSize(WorkToyClass):
  """WorkSide - Paint - FontSize
  Class representation of font size."""

  size = Field()

  @size.GET
  def getFontSize(self) -> int:
    """Getter-function for the font size"""
    return self._innerValue

  @size.SET
  def setFontSize(self, size: int) -> None:
    """Setter-function for the font size"""
    self._innerValue = size

  def __init__(self, *args, **kwargs) -> None:
    WorkToyClass.__init__(self, *args, **kwargs)
    intArg = self.maybeType(int, *args)
    intKwarg = self.searchKey('size, fontSize, pointSize', **kwargs)
    intDefault = 16
    self._innerValue = self.maybe(intArg, intKwarg, intDefault)
