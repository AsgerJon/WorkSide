"""workside - Core - TextLabel
Simplest label implementation"""
#  Copyright (c) 2023 Asger Jon Vistisen
#  MIT Licence
from __future__ import annotations

import random
from string import ascii_letters

from PySide6.QtCore import QRect, QSize, QMargins, QTimer
from icecream import ic
from worktoy.settings import AlignCenter
from PySide6.QtGui import QPaintEvent, QFont, QFontMetrics, QPen, QPainter
from PySide6.QtWidgets import QWidget
from worktoy.descriptors import Attribute
from worktoy.worktoyclass import WorkToyClass

from workside.settings import Black, Line, getBasePen, getBaseBrush, Color, \
  Pink, Precise

ic.configureOutput(includeContext=True)


class TextLabel(QWidget, WorkToyClass):
  """Simplest label implementation"""

  fontFamily = Attribute()
  fontSize = Attribute()
  fontWeight = Attribute()
  fontColor = Attribute()
  fontPen = Attribute()
  lineLen = Attribute()
  textFont = Attribute()
  fontMetrics = Attribute()
  alignmentFlags = Attribute()
  boundedRect = Attribute()
  boundedSize = Attribute()
  currentText = Attribute()
  sampleText = Attribute()
  paddedRect = Attribute()
  paddedSize = Attribute()

  @sampleText.GET
  def getSampleText(self) -> str:
    """Getter-function for the sample text. """
    return ''.join([*random.choices(ascii_letters, k=self.lineLen)])

  @currentText.SET
  def setCurrentText(self, text: str) -> None:
    """Getter-function for the current text"""
    setattr(self, '__current_text__', text)
    self.update()

  @currentText.GET
  def getCurrentText(self, ) -> str:
    """Getter-function for the current text"""
    return getattr(self, '__current_text__', 'LMAO')

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
    fontPen.setColor(Black.Q)
    return fontPen

  @paddedRect.GET
  def getPaddedRect(self) -> QRect:
    """Getter-function for the rectangle that would bound the full text."""
    r = self.geometry()
    flags = self.alignmentFlags
    return self.fontMetrics.boundingRect(r, flags, self.sampleText)

  @paddedSize.GET
  def getPaddedSize(self) -> QSize:
    """Getter-function for the size that would bound the full text"""
    return self.paddedRect.size()

  @boundedRect.GET
  def getBoundedRect(self, text: str = None) -> QRect:
    """Getter-function for the rectangle that would bound the current
    text."""
    r = self.geometry()
    flags = self.alignmentFlags
    return self.fontMetrics.boundingRect(r, flags, self.currentText)

  @boundedSize.GET
  def getBoundedSize(self, text: str = None) -> QSize:
    """Getter-function for the size that would bound the current text"""
    return self.getBoundedRect(text).size()

  def __init__(self, *args, **kwargs) -> None:
    WorkToyClass.__init__(self, *args, **kwargs)
    parent = self.maybeType(QWidget, *args)
    QWidget.__init__(self, parent)
    self.fontFamily = 'Courier'
    self.fontSize = 20
    self.fontWeight = QFont.Weight.Normal
    self.fontColor = Black
    self.lineLen = 40
    self.alignmentFlags = AlignCenter
    text = self.maybeType(str, *args)
    self.currentText = text
    self.timer = QTimer()
    self.timer.setTimerType(Precise)
    self.timer.setInterval(250)
    self.timer.setSingleShot(True)
    self.timer.timeout.connect(self.adjustSize())
    self.timer.start()

  def paintEvent(self, event: QPaintEvent) -> None:
    """The paint event uses the printer painter"""
    painter = QPainter()
    painter.begin(self)
    painter.setFont(self.textFont)
    painter.setPen(self.fontPen)
    painter.drawRect(painter.viewport() - QMargins(2, 2, 2, 2))
    painter.setBrush(getBaseBrush(Pink))
    flags = self.alignmentFlags
    viewRect = painter.viewport()
    painter.drawRect(self.boundedRect)
    painter.drawText(self.boundedRect, flags, self.currentText)
    painter.end()
