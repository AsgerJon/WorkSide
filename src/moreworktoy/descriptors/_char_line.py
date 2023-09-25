"""WorkSide - MoreWorkToy - Field - FieldInstanceHeader
Formatted code header"""
#  Copyright (c) 2023 Asger Jon Vistisen
#  MIT Licence
from __future__ import annotations

from worktoy.descriptors import Attribute
from worktoy.worktoyclass import WorkToyClass

from moreworktoy.texttools import maxLineLen


class CharLine(WorkToyClass):
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
  left = Attribute()
  right = Attribute()

  currentText = Attribute()

  @right.GET
  def getRight(self) -> str:
    """Getter-function for left part side"""
    margin = self.rightMargin
    fill = self.rightFill
    border = self.rightBorder
    pad = self.rightPad
    return '%s%s%s%s' % (margin, fill, border, pad)

  @left.GET
  def getLeft(self) -> str:
    """Getter-function for left part side"""
    margin = self.leftMargin
    fill = self.leftFill
    border = self.leftBorder
    pad = self.leftPad
    return '%s%s%s%s' % (margin, fill, border, pad)

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

  def getCenterLine(self) -> str:
    """Getter-function for center line"""
    return '%s%s%s' % (self.left, self.currentText, self.right)

  def getTopLine(self) -> str:
    """Getter-function for top line"""

  def __init__(self, *args, **kwargs) -> None:
    WorkToyClass.__init__(self, *args, **kwargs)

    _text = self.maybeType(str, *args)
    self.currentText = self.maybe(_text, 'LMAO')

  def __str__(self) -> str:
    return
