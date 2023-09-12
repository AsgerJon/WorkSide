"""WorkSide - Paint - FontStyle
The parent class FontSpec provides the data and the encoding and decoding
to and from json. FontStyle exposes this data to QPainter, QPen and so
forth. """
#  Copyright (c) 2023 Asger Jon Vistisen
#  MIT Licence
from __future__ import annotations

import json
import os

from PySide6.QtCore import Qt
from PySide6.QtGui import QPainter, QFont, QPen, QBrush, QFontMetrics, QColor
from icecream import ic
from worktoy.descriptors import Field

from workside.paint import FontSpec

ic.configureOutput(includeContext=True)


# from workside.widgets import LabelWidget


class FontStyle(FontSpec):
  """WorkSide - Paint - FontStyle
  The parent class FontSpec provides the data and the encoding and decoding
  to and from json. FontStyle exposes this data to QPainter, QPen and so
  forth. """

  @classmethod
  def getBaseSpec(cls) -> FontStyle:
    """Getter-function for base specification"""

    fileName = 'base_spec.json'
    here = os.path.dirname(__file__)
    filePath = os.path.join(here, fileName)
    with open(filePath, 'r') as f:
      data = json.loads(f.read())
    print(type(data))
    return FontStyle(**data)

  metrics = Field()
  font = Field()
  fontPen = Field()
  borderPen = Field()
  fillBrush = Field()
  blankBrush = Field()
  blankPen = Field()

  @blankBrush.GET
  def getBlankBrush(self) -> QBrush:
    """Getter-function for the blank brush"""
    brush = QBrush()
    brush.setStyle(Qt.BrushStyle.NoBrush)
    # brush.setColor(QColor(0, 0, 0, 0))
    return brush

  @blankPen.GET
  def getBlankPen(self) -> QPen:
    """Getter-function for blank pen"""
    pen = QPen()
    pen.setStyle(Qt.PenStyle.NoPen)
    pen.setColor(QColor(0, 0, 0, 0))
    pen.setWidth(1)
    return pen

  @metrics.GET
  def getFontMetrics(self) -> QFontMetrics:
    """Getter-function for the font metrics"""
    return QFontMetrics(self.font)

  @font.GET
  def getFont(self, ) -> QFont:
    """Getter-function for the font """
    out = QFont()
    out.setFamily(self.fontFamily)
    out.setPointSize(self.fontSize)
    out.setWeight(self.fontWeight)
    return out

  @fontPen.GET
  def getFontPen(self) -> QPen:
    """Getter-function for the font pen"""
    pen = QPen()
    pen.setStyle(Qt.PenStyle.SolidLine)
    pen.setWidth(1)
    pen.setColor(self.fontColor.Q)
    return pen

  @borderPen.GET
  def getBorderPen(self, ) -> QPen:
    """Getter-function for the border pen"""
    pen = QPen()
    pen.setStyle(Qt.PenStyle.SolidLine)
    pen.setWidth(self.borderWidth)
    pen.setColor(self.borderColor.Q)
    return pen

  @fillBrush.GET
  def getFillBrush(self) -> QBrush:
    """Getter-function for the fill brush"""
    brush = QBrush()
    brush.setStyle(Qt.BrushStyle.SolidPattern)
    brush.setColor(self.backgroundColor.Q)
    return brush

  def __init__(self, *args, **kwargs) -> None:
    ic(kwargs)
    FontSpec.__init__(self, *args, **kwargs)

  def apply(self, painter: QPainter) -> None:
    """This method provides the interface with the instance of QPainter.
    The paint event method on the widget defines the text and the QPainter
    provides the viewport."""
    if painter.isActive():
      widget = painter.device()
      if not widget.__class__.__qualname__ == 'LabelWidget':
        print(widget.__class__.__qualname__)
        return
      text = widget.getText()
      viewRect = painter.viewport()
      flags = self.alignFlags
      textRect = self.metrics.boundingRect(viewRect, flags, text)
      painter.setBrush(self.fillBrush)
      ic(self.fillBrush)
      painter.setPen(self.borderPen)
      xR, yR = self.cornerRadiusX, self.cornerRadiusY
      painter.drawRoundedRect(textRect, xR, yR)
      painter.setBrush(self.blankBrush)
      painter.setPen(self.fontPen)
      painter.setFont(self.font)
      painter.drawText(textRect, flags, text)
      painter.end()
