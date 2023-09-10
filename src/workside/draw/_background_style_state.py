"""WorkSide - Draw - BackgroundStyleState
Class representation of background style."""
#  Copyright (c) 2023 Asger Jon Vistisen
#  MIT Licence
from __future__ import annotations

from typing import Optional

from PySide6.QtCore import Qt
from PySide6.QtGui import QColor, QPainter, QPen, QBrush
from PySide6.QtWidgets import QWidget
from worktoy.descriptors import IntAttribute, Field, StrAttribute
from worktoy.worktoyclass import WorkToyClass

from workside.draw import Color


class BackgroundStyleState(WorkToyClass):
  """Class representation of the styles required to specify a background
  painting. """

  @staticmethod
  def paintwidgetGuard(widget: QWidget) -> Optional[QWidget]:
    """Custom guard ensuring that the widget given is a QWidget. This
    guard allows widget to be None."""
    if widget is None:
      return
    if isinstance(widget, QWidget):
      return widget
    from worktoy.waitaminute import TypeSupportError
    expectedType = QWidget
    actualValue = widget
    argName = 'widget'
    raise TypeSupportError(expectedType, actualValue, argName)

  @staticmethod
  def painterGuard(painter: QPainter) -> Optional[QPainter]:
    """Custom guard ensuring that the painter given is a QPainter
    instance. This guard allows painter to be None."""
    if painter is None:
      return
    if isinstance(painter, QPainter):
      return painter
    from worktoy.waitaminute import TypeSupportError
    expectedType = QPainter
    actualValue = painter
    argName = 'painter'
    raise TypeSupportError(expectedType, actualValue, argName)

  stateName = StrAttribute()

  cornerRadius = IntAttribute(5)
  borderWidth = IntAttribute(2)
  fillRed = IntAttribute(255)
  fillGreen = IntAttribute(255)
  fillBlue = IntAttribute(255)
  borderRed = IntAttribute(0)
  borderGreen = IntAttribute(0)
  borderBlue = IntAttribute(0)

  fillColor = Field()
  borderColor = Field()

  fillQColor = Field()
  borderQColor = Field()

  pen = Field()
  brush = Field()
  painter = Field()

  @pen.getter
  def getPen(self) -> QPen:
    """Getter-function for the pen."""
    pen = QPen()
    pen.setStyle(Qt.PenStyle.SolidLine, )
    pen.setColor(self.borderQColor)
    pen.setWidth(self.borderWidth)
    return pen

  @brush.getter
  def getBrush(self) -> QBrush:
    """Getter-function for the brush."""
    brush = QBrush()
    brush.setStyle(Qt.BrushStyle.SolidPattern)
    brush.setColor(self.fillQColor)
    return brush

  @painter.getter
  def applyPainter(self, *args) -> QPainter:
    """Applies the styles to the painter. If no painter is given a new
    painter is created with styles applied. If a paint widget is given,
    that painter is initialised on it. Then the painter draws the
    background on the paint widget with the styles defined in this class."""
    painter = self.maybeType(QPainter, *args)
    widget = self.maybeType(QWidget, *args)
    painter = self.painterGuard(painter)
    widget = self.paintwidgetGuard(widget)
    if painter is None:
      painter = QPainter()
    painter.setPen(self.pen)
    painter.setBrush(self.brush)
    if widget is None:
      return painter
    if isinstance(widget, QWidget):
      region = widget.visibleRegion()
      fillRect = region.boundingRect()
      painter.begin(widget)
      painter.drawRect(fillRect)
      radius = self.cornerRadius
      painter.drawRoundedRect(fillRect, radius, radius)
      return painter

  def getPainter(self) -> QPainter:
    """Getter-function for the painter."""
    painter = QPainter()
    painter.setPen(self.pen)
    painter.setBrush(self.brush)
    return painter

  @borderColor.getter
  def getBorderColor(self, ) -> Color:
    """Getter-function for border color"""
    return Color(self.borderRed, self.borderGreen, self.borderBlue)

  @borderQColor.getter
  def getBorderQColor(self) -> QColor:
    return QColor(self.borderRed, self.borderGreen, self.borderBlue)

  @fillColor.getter
  def getFillColor(self, ) -> Color:
    """Getter-function for border color"""
    return Color(self.fillRed, self.fillGreen, self.fillBlue)

  @fillQColor.getter
  def getFillQColor(self) -> QColor:
    return QColor(self.fillRed, self.fillGreen, self.fillBlue)

  @borderColor.setter
  def setBorderColor(self, color: Color) -> None:
    """Setter-function for the border color."""
    self.borderRed = color.red
    self.borderGreen = color.green
    self.borderBlue = color.blue

  @fillColor.setter
  def setFillColor(self, color: Color) -> None:
    """Setter-function for the border color."""
    self.fillRed = color.red
    self.fillGreen = color.green
    self.fillBlue = color.blue

  @borderQColor.setter
  def setBorderQColor(self, color: QColor) -> None:
    """Setter-function for the border color."""
    self.borderRed = color.red()
    self.borderGreen = color.green()
    self.borderBlue = color.blue()

  @fillQColor.setter
  def setFillQColor(self, color: QColor) -> None:
    """Setter-function for the border color."""
    self.fillRed = color.red()
    self.fillGreen = color.green()
    self.fillBlue = color.blue()

  @staticmethod
  def dictColor(rgb: dict) -> Color:
    """Loads a color from the rgb data"""
    red = rgb.get('red', 255)
    green = rgb.get('green', 255)
    blue = rgb.get('blue', 255)
    return Color(red, green, blue)

  @classmethod
  def fromJson(cls, data: dict, keyName: str) -> BackgroundStyleState:
    """Creates an instance from the data in the json data entry. """
    cls.__core_instance__ = cls()
    state = cls()
    state.cornerRadius = data.get('cornerRadius', state.cornerRadius)
    state.borderWidth = data.get('borderWidth', state.borderWidth)
    borderData = data.get('border', {})
    borderColor = cls.dictColor(borderData)
    state.borderColor = borderColor
    state.fillColor = cls.dictColor(data.get('fill', {}))
    state.stateName = keyName
    return state

  def __str__(self, ) -> str:
    """String representation"""
    msg = """%s:<br>
    Fill Color: %s, Border Color: %s, Corner Radius: %s, Border 
      Width: %s"""
    fill, border = self.fillColor, self.borderColor
    radius, width = self.cornerRadius, self.borderWidth
    msg = msg % (self.stateName, fill, border, radius, width)
    return self.monoSpace(msg)

  def __repr__(self, ) -> str:
    """Code representation."""
    fill, border = self.fillColor, self.borderColor
    radius, width = self.cornerRadius, self.borderWidth
    name = self.__class__.__qualname__
    return '%s(%s, %s, %s, %s)' % (name, fill, border, radius, width)
