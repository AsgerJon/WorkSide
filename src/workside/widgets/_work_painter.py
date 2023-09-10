"""WorkSide - Widgets - WorkPainter
Custom implementation of QPainter."""
#  Copyright (c) 2023 Asger Jon Vistisen
#  MIT Licence
from __future__ import annotations

from typing import TYPE_CHECKING

from PySide6.QtGui import QColor, QBrush
from PySide6.QtGui import QPainter, Qt, QPen
from PySide6.QtWidgets import QWidget
from icecream import ic

from workside.draw import BackgroundStyleState, FontStyleState

if TYPE_CHECKING:
  from workside.widgets import CoreWidget
else:
  CoreWidget, TextWidget = QWidget, QWidget

from worktoy.descriptors import Field, IntAttribute

ic.configureOutput(includeContext=True)


class WorkPainter(QPainter):
  """WorkSide - Widgets - WorkPainter
  Custom implementation of QPainter."""

  blankPen = Field()
  blankBrush = Field()

  radius = IntAttribute(1)
  width = IntAttribute(1)

  @blankBrush.getter
  def getBlankBrush(self, *args) -> QBrush:
    """Getter-function for the blank brush"""
    brush = QBrush()
    brush.setStyle(Qt.BrushStyle.NoBrush)
    brush.setColor(QColor(255, 255, 255, 0))
    return brush

  @blankPen.getter
  def getBlankPen(self, *args) -> QPen:
    """Getter-function for the blank pen"""
    pen = QPen()
    pen.setStyle(Qt.PenStyle.NoPen)
    pen.setColor(QColor(255, 255, 255, 0))
    pen.setWidth(1)
    return pen

  def __init__(self, *args, **kwargs) -> None:
    QPainter.__init__(self, *args, **kwargs)
    self._widget = None

  def getActiveWidget(self) -> CoreWidget:
    """Getter-function for the widget"""
    return self._widget

  def setActiveWidget(self, widget: CoreWidget) -> None:
    """Setter-function for the widget"""
    self._widget = widget

  def clearWidget(self, ) -> None:
    """Clears the current widget."""
    self._widget = None

  def begin(self, widget: CoreWidget) -> bool:
    """Reimplementation"""
    self._widget = widget
    self.setRenderHint(QPainter.RenderHint.Antialiasing)
    return QPainter.begin(self, widget)

  def end(self) -> None:
    """Reimplementation"""
    self._widget = None
    return QPainter.end(self)

  def __matmul__(self, other: BackgroundStyleState) -> WorkPainter:
    """Applies the style settings from other to self."""
    if isinstance(other, BackgroundStyleState):
      self.setPen(other.pen)
      self.setBrush(other.brush)
      self.radius = other.radius
      self.width = other.width
      return self
    if isinstance(other, FontStyleState):
      if other.fillRect:
        self.setPen(other.fillPen)
        self.setBrush(other.fillBrush)
        other.fillRect = False
        other.drawText = True
        return self
      self.setPen(other.fontPen)
      self.setFont(other.font)
      other.fillRect = True
      other.drawText = False
      return self

  def __rmatmul__(self, other: BackgroundStyleState) -> WorkPainter:
    """Applies the style settings from other to self."""
    return self @ other

  @classmethod
  def paintMeLike(cls, widget: CoreWidget) -> None:
    """Manages the paint event on the widget. The fields and attributes on
    the widgets tells the painter how to paint it."""
    painter = cls()
    painter.begin(widget)
    viewRect = painter.viewport()
    if widget.drawBackground:
      painter = widget.backgroundStyle @ painter
      painter.drawRect(viewRect)
    if widget.drawText:
      textRect = widget.getTextRect()
      textFlags = widget.getAlignmentFlags()
      ic(textFlags)
      painter = widget.fontStyle @ painter
      painter.drawRoundedRect(textRect, 1, 1)
      painter = widget.fontStyle @ painter
      painter.drawText(textRect, textFlags, widget.text)
      painter.end()
