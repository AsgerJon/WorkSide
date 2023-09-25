"""workside - Core - TextPrinter
Code writing assistant"""
#  Copyright (c) 2023 Asger Jon Vistisen
#  MIT Licence
from __future__ import annotations

from PySide6.QtCore import QRect, QSize
from PySide6.QtGui import QPainter, QFont, QPen, QFontMetrics
from worktoy.descriptors import Attribute
from worktoy.settings import AlignCenter
from worktoy.worktoyclass import WorkToyClass

from workside.quickwidgets import TextLabel
from workside.settings import Black, getBasePen, Line


class TextPrinter(WorkToyClass, QPainter):
  """Takes a widget and prints the text in the 'currentText' attribute on 
  the widget. """

  fontFamily = Attribute()
  fontSize = Attribute()
  fontWeight = Attribute()
  fontColor = Attribute()
  fontPen = Attribute()
  lineLen = Attribute()
  textFont = Attribute()
  fontMetrics = Attribute()
  alignmentFlags = Attribute()

  _styleKeys = [
    'fontFamily',
    'fontSize',
    'fontWeight',
    'fontColor',
    'fontPen',
    'lineLen',
    'textFont',
  ]

  @classmethod
  def getStyleSettings(cls) -> list[str]:
    """Getter-function for a list of style settings"""
    return cls._styleKeys

  def __init__(self, *args, **kwargs) -> None:
    WorkToyClass.__init__(self, *args, **kwargs)
    QPainter.__init__(self, )
    self.fontFamily = 'Courier'
    self.fontSize = 20
    self.fontWeight = QFont.Weight.Normal
    self.fontColor = Black
    self.lineLen = 40
    self.alignmentFlags = AlignCenter

  @textFont.GET
  def getTextFont(self) -> QFont:
    """Getter-function for the text font."""
    textFont = QFont()
    textFont.setFamily(self.fontFamily)
    textFont.setPointSize(self.fontSize)
    textFont.setWeight = self.fontWeight
    return textFont

  @fontMetrics.GET
  def getFontMetrics(self) -> QFontMetrics:
    """Getter-function for the QFontMetrics"""
    return QFontMetrics(self.textFont)

  @fontPen.GET
  def getFontPen(self) -> QPen:
    """Getter-function for the font pen"""
    fontPen = getBasePen(Black, 1, Line)
    fontPen.setColor(Black)
    return fontPen

  def getBoundedRect(self, text: str) -> QRect:
    """Getter-function for the bounding rectangle"""
    return self.fontMetrics.tightBoundingRect(text)

  def getBoundedSize(self, text: str) -> QSize:
    """Getter-function for the bounding size"""
    return self.getBoundedRect(text).size()

  def wordListLength(self, wordList: list[str], *words) -> int:
    """Measures the length of the words in the length including spaces"""
    return len(' '.join([*wordList, *words]))

  def paintMeLike(self, widget: TextLabel) -> TextLabel:
    """Describes the painting operation."""
    self.begin(widget)
    lines = self.wordWrap(widget.currentText, self.lineLen)
    text = '\n'.join(lines)
    self.setFont(self.textFont)
    self.setPen(self.fontPen)
    viewRect = self.viewport()
    textRect = self.boundingRect(viewRect, self.alignmentFlags, text)
    self.drawText(viewRect, self.alignmentFlags, text)
    return widget
