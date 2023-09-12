"""WorkSide - Paint - FontSpec
Enhanced subclass of QFont"""
#  Copyright (c) 2023 Asger Jon Vistisen
#  MIT Licence
from __future__ import annotations

import json
import os

from PySide6.QtCore import Qt
from icecream import ic
from worktoy.descriptors import Field
from worktoy.worktoyclass import WorkToyClass

from workside.paint import Color, FontSize, FontFamily, FontWeight

Align = Qt.AlignmentFlag

ic.configureOutput(includeContext=True)


class FontSpec(WorkToyClass):
  """WorkSide - Paint - FontSpec
  Data class specifying a text drawing styles."""

  __default_horizontal_alignment__ = Qt.AlignmentFlag.AlignHCenter
  __default_vertical_alignment__ = Qt.AlignmentFlag.AlignVCenter

  @classmethod
  def _getDefaultHorizontalAlignment(cls) -> Align:
    """Getter-function for default horizontal alignment"""
    return cls.__default_horizontal_alignment__

  @classmethod
  def _getDefaultVerticalAlignment(cls) -> Align:
    """Getter-function for default vertical alignment"""
    return cls.__default_vertical_alignment__

  verticalAlignment = Field()
  horizontalAlignment = Field()
  alignFlags = Field()
  fontFamily = Field()
  fontSize = Field()
  fontWeight = Field()
  fontColor = Field()
  backgroundColor = Field()
  borderColor = Field()
  borderWidth = Field()
  cornerRadiusX = Field()
  cornerRadiusY = Field()

  @alignFlags.GET
  def getAlignFlags(self) -> Align:
    """Getter-function for combined alignment flags"""
    vAlign = self.verticalAlignment
    hAlign = self.horizontalAlignment
    wrap = Qt.TextFlag.TextWordWrap
    return vAlign | hAlign | wrap

  def getDefaultHorizontalAlignment(self) -> Align:
    """Getter-function for default horizontal alignment"""
    return self.__default_horizontal_alignment__

  def getDefaultVerticalAlignment(self) -> Align:
    """Getter-function for default vertical alignment"""
    return self.__default_vertical_alignment__

  @horizontalAlignment.GET
  def getHorizontalAlignment(self) -> Align:
    """Getter-function for the horizontal alignment"""
    return self.maybe(self._horizontalAlignment,
                      self.getDefaultHorizontalAlignment())

  @verticalAlignment.GET
  def getVerticalAlignment(self) -> Align:
    """Getter-function for the horizontal alignment"""
    return self.maybe(self._verticalAlignment,
                      self.getDefaultVerticalAlignment())

  @fontFamily.GET
  def getFontFamily(self, ) -> FontFamily:
    """Getter function for fontFamily"""
    return self._fontFamily

  @fontFamily.SET
  def setFontFamily(self, newValue: FontFamily) -> None:
    """Setter function for fontFamily"""
    self._fontFamily = newValue

  @fontSize.GET
  def getFontSize(self, ) -> FontSize:
    """Getter function for fontSize"""
    return self.maybe(self._fontSize, 16)

  @fontSize.SET
  def setFontSize(self, newValue: FontSize) -> None:
    """Setter function for fontSize"""
    self._fontSize = newValue

  @fontWeight.GET
  def getFontWeight(self, ) -> FontWeight:
    """Getter function for fontWeight"""
    return self.maybe(self._fontWeight, FontWeight()).weight

  @fontWeight.SET
  def setFontWeight(self, newValue: FontWeight) -> None:
    """Setter function for fontWeight"""
    self._fontWeight = newValue

  @fontColor.GET
  def getFontColor(self, ) -> Color:
    """Getter function for fontColor"""
    return self._fontColor

  @fontColor.SET
  def setFontColor(self, newValue: Color) -> None:
    """Setter function for fontColor"""
    self._fontColor = newValue

  @backgroundColor.GET
  def getBackgroundColor(self, ) -> Color:
    """Getter function for backgroundColor"""
    ic(self._backgroundColor)
    return self._backgroundColor

  @backgroundColor.SET
  def setBackgroundColor(self, newValue: Color) -> None:
    """Setter function for backgroundColor"""
    self._backgroundColor = newValue

  @borderColor.GET
  def getBorderColor(self, ) -> Color:
    """Getter function for borderColor"""
    return self._borderColor

  @borderColor.SET
  def setBorderColor(self, newValue: Color) -> None:
    """Setter function for borderColor"""
    self._borderColor = newValue

  @borderWidth.GET
  def getBorderWidth(self, ) -> int:
    """Getter function for borderWidth"""
    return self.maybe(self._borderWidth, 1)

  @borderWidth.SET
  def setBorderWidth(self, newValue: int) -> None:
    """Setter function for borderWidth"""
    self._borderWidth = newValue

  @cornerRadiusX.GET
  def getCornerRadiusX(self, ) -> int:
    """Getter function for cornerRadiusX"""
    return self.maybe(self._cornerRadiusX, 1)

  @cornerRadiusX.SET
  def setCornerRadiusX(self, newValue: int) -> None:
    """Setter function for cornerRadiusX"""
    self._cornerRadiusX = newValue

  @cornerRadiusY.GET
  def getCornerRadiusY(self, ) -> int:
    """Getter function for cornerRadiusY"""
    return self.maybe(self._cornerRadiusY, 1)

  @cornerRadiusY.SET
  def setCornerRadiusY(self, newValue: int) -> None:
    """Setter function for cornerRadiusY"""
    self._cornerRadiusY = newValue

  def __init__(self, *args, **kwargs) -> None:
    WorkToyClass.__init__(self, *args, **kwargs)

    self._fontFamily = FontFamily(kwargs.get('fontFamily', None))
    self._fontSize = kwargs.get('fontSize', None)
    self._fontWeight = FontWeight(kwargs.get('fontWeight', None))
    self._fontColor = Color(**kwargs.get('fontColor', None))
    self._backgroundColor = Color(**kwargs.get('backgroundColor', None))
    self._borderColor = Color(**kwargs.get('borderColor', None))
    self._borderWidth = kwargs.get('borderWidth', None)
    self._cornerRadiusX = kwargs.get('cornerRadiusX', None)
    self._cornerRadiusY = kwargs.get('cornerRadiusY', None)
    self._verticalAlignment = kwargs.get('vertical', None)
    self._horizontalAlignment = kwargs.get('horizontal', None)

  def encode(self, ) -> str:
    """Encodes to json data"""
    return json.dumps(dict(
      fontFamily=self.fontFamily,
      fontSize=self.fontSize,
      fontWeight=self.fontWeight,
      fontColor=self.fontColor,
      backgroundColor=self.backgroundColor,
      borderColor=self.borderColor,
      borderWidth=self.borderWidth,
      cornerRadiusX=self.cornerRadiusX,
      cornerRadiusY=self.cornerRadiusY,
    ))

  @classmethod
  def decode(cls, data: str) -> FontSpec:
    """Decodes the data to an instance of FontStyle"""
    return cls(**json.loads(data))
