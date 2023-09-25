"""WorkSide - MoreWorkToy - Field - FieldInstanceHeader
Formatted code header"""
#  Copyright (c) 2023 Asger Jon Vistisen
#  MIT Licence
from __future__ import annotations

from worktoy.descriptors import Attribute
from worktoy.worktoyclass import WorkToyClass

from moreworktoy.texttools import maxLineLen


class FieldInstanceHeader(WorkToyClass):
  """Header"""

  @staticmethod
  def roundLeft(n: int) -> int:
    """Rounds down"""
    return int(0.5 * (n - (n % 2)))

  @staticmethod
  def roundRight(n: int) -> int:
    """Rounds down"""
    return int(0.5 * (n + (n % 2)))

  leftMargin = Attribute('  #')
  rightMargin = Attribute('#  ')
  leftPad = Attribute('  ')
  rightPad = Attribute('  ')
  leftBorder = Attribute('<')
  rightBorder = Attribute('>')
  leftFillChar = Attribute('~')
  rightFillChar = Attribute('~')
  leftFill = Attribute()
  rightFill = Attribute()
  innerLen = Attribute()
  outerLen = Attribute(maxLineLen)
  fillSpace = Attribute()

  currentText = Attribute()

  @fillSpace.GET
  def getFillSpace(self) -> int:
    """Getter-function the total number of fill characters"""
    n = self.outerLen - len(self.leftMargin + self.rightMargin)
    n -= self.outerLen - len(self.leftPad + self.rightPad)
    n -= self.outerLen - len(self.leftBorder + self.rightBorder)
    return n - len(self.currentText)

  def getLeftFill(self) -> str:
    """Getter-function for fill on the left"""
    return self.roundLeft(self.fillSpace) * self.leftFillChar

  def getRightFill(self) -> str:
    """Getter-function for fill on the left"""
    return self.roundRight(self.fillSpace) * self.rightFillChar

  def __init__(self, *args, **kwargs) -> None:
    WorkToyClass.__init__(self, *args, **kwargs)

    _text = self.maybeType(str, *args)
    self.currentText = self.maybe(_text, 'LMAO')

  def __str__(self) -> str:
    return '%s%s%s'
