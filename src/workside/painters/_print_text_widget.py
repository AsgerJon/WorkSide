"""WorkSide - Painters - PrintText
Prints text on the paint device."""
#  MIT Licence
#  Copyright (c) 2023 Asger Jon Vistisen
from __future__ import annotations

from typing import TYPE_CHECKING

from PySide6.QtCore import Qt, QMargins
from PySide6.QtGui import QFont, QBrush, QColor, QPen
from icecream import ic

from workside.painters import AbstractPainter
from workside.settings import blankBrush, Fill, Line, Black, getBaseBrush, \
  Platinum
from worktoy.settings import AlignCenter, AlignLeft, AlignTop

if TYPE_CHECKING:
  from workside.widgets import TextWidget


class PrintTextWidget(AbstractPainter):
  """WorkSide - Painters - PrintText
  Prints text on the paint device."""

  def __init__(self, *args, **kwargs) -> None:
    AbstractPainter.__init__(self, *args, **kwargs)

  def preparePainting(self,
                      widget: TextWidget,
                      *args) -> TextWidget:
    """Prepares the painter by setting styles if defined"""
    self.begin(widget)
    self.setFont(widget.textFont)
    self.setPen(widget.fontPen)
    self.setBackground(getBaseBrush(Platinum))
    self.setBackgroundMode(Qt.BGMode.TransparentMode)
    self.setBrush(blankBrush)
    widget = self.paintMeLike(widget)
    self.end()
    return widget

  def paintMeLike(self, widget: TextWidget) -> TextWidget:
    """Prints the contents of the 'currentText' attribute on the text
    widget."""
    self.drawText(self.viewport(), widget.alignment, widget.currentText)
    return widget
