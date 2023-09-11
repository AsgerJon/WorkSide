"""WorkSide - Draw - FontStyleState
State sensitive font style settings."""
#  Copyright (c) 2023 Asger Jon Vistisen
#  MIT Licence
from __future__ import annotations

import json

from PySide6.QtCore import Qt, QRect
from PySide6.QtGui import QFont, QPen, QColor, QBrush, QFontMetrics
from icecream import ic
from worktoy.descriptors import Field, IntAttribute, StrAttribute, Flag
from worktoy.worktoyclass import WorkToyClass

from workside.draw import Color

ic.configureOutput(includeContext=True)


class FontStyleState(WorkToyClass):
  """WorkSide - Draw - FontStyleState
  State sensitive font style settings."""

  fillRect = True
  drawText = False

  font = Field()
  fontMetrics = Field()
  #  Border color on background
  fillPenRed = IntAttribute()
  fillPenGreen = IntAttribute()
  fillPenBlue = IntAttribute()
  fillPenColor = Field()
  fillPenQColor = Field()
  fillPen = Field()
  #  _____________________________
  #  text color
  fontPenRed = IntAttribute()
  fontPenGreen = IntAttribute()
  fontPenBlue = IntAttribute()
  fontPenColor = Field()
  fontPenQColor = Field()
  fontPen = Field()
  #  __________________________
  #  fill color on background
  fontFillRed = IntAttribute()
  fontFillGreen = IntAttribute()
  fontFillBlue = IntAttribute()
  fontFillColor = Field()
  fontFillQColor = Field()
  fillBrush = Field()
  #

  bold = Flag()
  italic = Flag()
  family = StrAttribute()
  size = IntAttribute()
  state = StrAttribute()

  @fillPenColor.GET
  def getFillPenColor(self) -> Color:
    """Getter-function for the fill pen color that outlines the background
    behind the textbox."""
    red = self.fillPenRed
    green = self.fillPenGreen
    blue = self.fillPenBlue
    return Color(red, green, blue)

  @fillPenColor.SET
  def setFillPenColor(self, color: Color) -> None:
    """Setter-function for the fill pen"""
    self.fillPenRed = color.red
    self.fillPenGreen = color.green
    self.fillPenBlue = color.blue

  @fillPenQColor.GET
  def getFillPenQColor(self) -> QColor:
    red = self.fillPenRed
    green = self.fillPenGreen
    blue = self.fillPenBlue
    return QColor(red, green, blue)

  @fillPenQColor.SET
  def setFillPenQColor(self, color: QColor) -> None:
    """Setter-function for the fill pen"""
    self.fillPenRed = color.red()
    self.fillPenGreen = color.green()
    self.fillPenBlue = color.blue()

  @fontFillColor.GET
  def getFontFillColor(self) -> Color:
    """Getter-function for the font pen color"""
    red = self.fontFillRed
    green = self.fontFillGreen
    blue = self.fontFillBlue
    return Color(red, green, blue)

  @fontFillColor.SET
  def setFontFillColor(self, color: Color) -> None:
    """Setter-function for the font pen color"""
    self.fontFillRed = color.red
    self.fontFillGreen = color.green
    self.fontFillBlue = color.blue

  @fontFillQColor.GET
  def getFontFillQColor(self) -> Color:
    """Getter-function for the font pen color"""
    red = self.fontFillRed
    green = self.fontFillGreen
    blue = self.fontFillBlue
    return QColor(red, green, blue)

  @fontFillQColor.SET
  def setFontFillQColor(self, color: QColor) -> None:
    """Setter-function for the font pen color"""
    self.fontFillRed = color.red()
    self.fontFillGreen = color.green()
    self.fontFillBlue = color.blue()

  @fontPenColor.GET
  def getFontPenColor(self) -> Color:
    """Getter-function for the font pen color"""
    return Color(self.fontPenRed, self.fontPenGreen, self.fontPenBlue)

  @fontPenColor.SET
  def setFontPenColor(self, color: Color) -> None:
    """Setter-function for the font pen color"""
    self.fontPenRed = color.red
    self.fontPenGreen = color.green
    self.fontPenBlue = color.blue

  @fontPenQColor.GET
  def getFontPenQColor(self) -> QColor:
    """Getter-function for the font pen color as QColor"""
    return QColor(self.fontPenRed, self.fontPenGreen, self.fontPenBlue)

  @fontPenQColor.SET
  def setFontPenQColor(self, color: QColor) -> None:
    """Setter-function for the font pen color"""
    self.fontPenRed = color.red()
    self.fontPenGreen = color.green()
    self.fontPenBlue = color.blue()

  @fontPen.GET
  def getFontPen(self) -> QPen:
    """Getter-function for the font pen"""
    pen = QPen()
    pen.setStyle(Qt.PenStyle.SolidLine)
    pen.setColor(self.fontPenQColor)
    pen.setWidth(1)
    return pen

  @fillBrush.GET
  def getFillBrush(self) -> QBrush:
    """Getter-function for fill brush"""
    brush = QBrush()
    brush.setStyle(Qt.BrushStyle.SolidPattern)
    brush.setColor(self.fontFillQColor)
    return brush

  @fillPen.GET
  def getFillPen(self, ) -> QPen:
    """Getter-function for the pen drawing the outline around the textbox."""
    pen = QPen()
    pen.setStyle(Qt.PenStyle.SolidLine)
    pen.setColor(self.fillPenQColor)
    pen.setWidth(1)
    return pen

  @fontMetrics.GET
  def getFontMetrics(self) -> QFontMetrics:
    """Getter-function for the QFontMetrics"""
    return QFontMetrics(self.font, )

  @font.GET
  def getFont(self) -> QFont:
    """Getter-function for font as QFont instance."""
    font = QFont()
    font.setFamily(self.family)
    font.setPointSize(self.size)
    font.setBold(self.bold)
    font.setItalic(self.italic)
    return font

  @font.SET
  def setFont(self, font: QFont) -> None:
    """Setter-function for QFont"""
    self.family = font.family()
    self.size = font.pointSize()
    self.bold = True if font.bold() else False
    self.italic = True if font.italic() else False

  def __init__(self, *args, **kwargs) -> None:
    WorkToyClass.__init__(self, *args, **kwargs)

  def getRect(self, text: str, targetRect: QRect = None, ) -> QRect:
    """Get rect!! LMAO!"""
    baseBoundingRect = self.fontMetrics.boundingRect(text)
    if targetRect is None:
      return baseBoundingRect

  @classmethod
  def fromJson(cls, data: str) -> FontStyleState:
    """Creates a QFont from the json entry"""
    state = cls()
    if not isinstance(data, dict):
      data = json.loads(data)
    family = data.get('family', None)
    fontSize = data.get('size', None)
    boldFlag = data.get('bold', None)
    italicFlag = data.get('italic', None)
    fontPenColorDict = data.get('penColor', None)
    fillPenColorDict = data.get('fillPenColor', None)
    fillColorDict = data.get('fillColor', None)
    vals = [family, fontSize, boldFlag, italicFlag, fontPenColorDict,
            fillColorDict]
    names = """family, size, bold, italic, penColor, fillColor"""
    names = state.stringList(names)
    if any([i is None for i in vals]):
      for name, val in zip(names, vals):
        if val is None:
          from worktoy.waitaminute import MissingArgumentException
          raise MissingArgumentException(name)
    state.family = family
    state.size = fontSize
    state.bold = boldFlag
    state.italic = italicFlag
    state.fontPenRed = fontPenColorDict.get('red', None)
    state.fontPenGreen = fontPenColorDict.get('green', None)
    state.fontPenBlue = fontPenColorDict.get('blue', None)
    state.fontFillRed = fillColorDict.get('red', None)
    state.fontFillGreen = fillColorDict.get('green', None)
    state.fontFillBlue = fillColorDict.get('blue', None)

    state.fillPenRed = fillPenColorDict.get('red', None)
    state.fillPenGreen = fillPenColorDict.get('green', None)
    state.fillPenBlue = fillPenColorDict.get('blue', None)
    return state
