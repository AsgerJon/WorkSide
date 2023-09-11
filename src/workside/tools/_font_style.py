"""WorkSide - Tools - FontStyle
Combines the QFont, QPen and QBrush functionality into one tool for use in
writing text with a particular line color on a particular background. The
QPen is restricted to unit width and solid style, but can vary its color.
Similarly, the QBrush is restricted to a solid style, but with varying
color."""
#  Copyright (c) 2023 Asger Jon Vistisen
#  MIT Licence
from __future__ import annotations

from typing import Any

from PySide6.QtGui import QPainter, QPen, QBrush, QFont
from worktoy.descriptors import Field, IntAttribute, Flag

from workside.tools import AbstractTools, FontFamily, FontSize, FontWeight, \
  Color


class FontStyle(AbstractTools):
  """WorkSide - Tools - FontStyle
  Combines the QFont, QPen and QBrush functionality into one tool for use in
  writing text with a particular line color on a particular background. The
  QPen is restricted to unit width and solid style, but can vary its color.
  Similarly, the QBrush is restricted to a solid style, but with varying
  color."""

  __default_background_color__ = Color(191, 191, 191)
  __default_border_color__ = Color(63, 63, 63)
  __default_font_color__ = Color(0, 0, 0)

  defaultBackgroundColor = Field()
  defaultBorderColor = Field()
  defaultFontColor = Field()

  vAlign = Field()
  hAlign = Field()
  cornerRadius = IntAttribute(5)
  borderWidth = IntAttribute(2)

  tools = Field()
  brush = Field()
  fontPen = Field()
  borderPen = Field()

  fontFamily = Field()
  fontSize = Field()
  fontWeight = Field()
  font = Field()

  backgroundColor = Field()
  borderColor = Field()
  fontColor = Field()

  @fontFamily.GET
  def getFontFamily(self) -> FontFamily:
    """Getter-function for font family."""
    return self._fontFamily

  @fontSize.GET
  def getFontSize(self) -> FontSize:
    """Getter-function for font size."""
    return self._fontSize

  @fontWeight.GET
  def getFontWeight(self) -> FontWeight:
    """Getter-function for font weight"""
    return self._fontWeight

  @backgroundColor.GET
  def getBackgroundColor(self) -> Color:
    """Getter-function for background color"""
    return self._backgroundColor

  @borderColor.GET
  def getBorderColor(self) -> Color:
    """Getter-function for border color"""
    return self._borderColor

  @fontColor.GET
  def getFontColor(self) -> Color:
    """Getter-function for font color"""
    return self._fontColor

  @font.GET
  def getFont(self) -> QFont:
    """Getter-function for QFont"""
    font = QFont()
    self.fontFamily >> font
    self.fontSize >> font
    self.fontWeight >> font
    return font

  @brush.GET
  def getBrush(self) -> QBrush:
    """Getter-function for QBrush"""

  @fontPen.GET
  def getFontPen(self, ) -> QPen:
    """Getter-function for QPen"""

  @borderPen.GET
  def getBorderPen(self, ) -> QPen:
    """Getter-function for QPen"""

  @tools.GET
  def getTools(self) -> list[type]:
    """Getter-function for supported tools"""
    return [QPainter, QPen, QBrush, QFont]

  def toolSupport(self, toolType: type) -> bool:
    """Supports QPainter as well as its constituents."""
    return True if toolType in self.tools else False

  def applyTool(self, tool: Any) -> Any:
    """Applies the given tool"""

  def __init__(self, *args, **kwargs) -> None:
    AbstractTools.__init__(self, *args, **kwargs)

  @classmethod
  def saveToJson(cls, instance: FontStyle = None) -> str:
    """Implementation"""
    fontData = dict(family=instance.fontFamily, size=instance.fontSize,
                    weight=instance.fontWeight, color=instance.fontColor)
    border = dict(color=instance.borderColor, width=instance.borderWidth)
    background = dict(color=instance.backgroundColor)
    shape = dict(radius=instance.cornerRadius)
