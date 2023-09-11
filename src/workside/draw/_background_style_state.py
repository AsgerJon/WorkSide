"""WorkSide - Draw - BackgroundStyleState
Instances of this data class describe the styles required to draw the
background."""
#  Copyright (c) 2023 Asger Jon Vistisen
#  MIT Licence
from __future__ import annotations

from typing import Union

from PySide6.QtCore import Qt
from PySide6.QtGui import QColor, QPen, QBrush
from worktoy.descriptors import IntAttribute, Field
from worktoy.worktoyclass import WorkToyClass

from workside.draw import Color


class BackgroundStyleState(WorkToyClass):
  """WorkSide - Draw - BackgroundStyleState
  Instances of this data class describe the styles required to draw the
  background."""

  pen = Field()
  brush = Field()

  radius = IntAttribute(5)
  width = IntAttribute(2)

  borderRed = IntAttribute(0)
  borderGreen = IntAttribute(0)
  borderBlue = IntAttribute(0)

  fillRed = IntAttribute(191)
  fillGreen = IntAttribute(191)
  fillBlue = IntAttribute(191)

  def setBorderColor(self, color: Union[Color, QColor]) -> None:
    """Setter-function for the border color"""
    red, green, blue = self.borderRed, self.borderGreen, self.borderBlue
    if isinstance(color, QColor):
      red, green, blue = color.red(), color.green(), color.blue()
    elif isinstance(color, Color):
      red, green, blue = color.red, color.green, color.blue

    self.borderRed = red
    self.borderGreen = green
    self.borderBlue = blue

  def getBorderColor(self, ) -> Color:
    """Getter-function for Color of the border"""
    return Color(self.borderRed, self.borderGreen, self.borderBlue)

  def getBorderQColor(self, ) -> QColor:
    """Getter-function for Color of the border as a QColor instance"""
    return QColor(self.borderRed, self.borderGreen, self.borderBlue)

  def setFillColor(self, color: Union[Color, QColor]) -> None:
    """Setter-function for the border color"""
    red, green, blue = self.fillRed, self.fillGreen, self.fillBlue
    if isinstance(color, QColor):
      red, green, blue = color.red(), color.green(), color.blue()
    elif isinstance(color, Color):
      red, green, blue = color.red, color.green, color.blue
    self.fillRed = red
    self.fillGreen = green
    self.fillBlue = blue

  def getFillColor(self, ) -> Color:
    """Getter-function for Color of the fill"""
    return Color(self.fillRed, self.fillGreen, self.fillBlue)

  def getFillQColor(self, ) -> QColor:
    """Getter-function for Color of the border as a QColor instance"""
    return QColor(self.fillRed, self.fillGreen, self.fillBlue)

  @pen.GET
  def getPen(self, *_) -> QPen:
    """Getter-function for the pen"""
    pen = QPen()
    pen.setStyle(Qt.PenStyle.SolidLine)
    pen.setColor(self.getBorderQColor())
    pen.setWidth(self.width)
    return pen

  @brush.GET
  def getBrush(self, *_) -> QBrush:
    """Getter-function for the brush"""
    brush = QBrush()
    brush.setStyle(Qt.BrushStyle.SolidPattern)
    brush.setColor(self.getFillQColor())
    return brush
