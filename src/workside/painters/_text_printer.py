"""workside - Core - TextPrinter
Code writing assistant"""
#  Copyright (c) 2023 Asger Jon Vistisen
#  MIT Licence
from __future__ import annotations

from typing import TYPE_CHECKING
from PySide6.QtCore import QRect, QSize
from PySide6.QtGui import QPainter, QFont, QPen, QFontMetrics
from worktoy.descriptors import Attribute
from worktoy.settings import AlignCenter
from worktoy.worktoyclass import WorkToyClass

from workside.settings import Black, getBasePen, Line

if TYPE_CHECKING:
  from workside.quickwidgets import TextLabel


class TextPrinter(WorkToyClass, QPainter):
  """Takes a widget and prints the text in the 'currentText' attribute on 
  the widget. """

  def __init__(self, *args, **kwargs) -> None:
    WorkToyClass.__init__(self, *args, **kwargs)
    QPainter.__init__(self, )

  def wordListLength(self, wordList: list[str], *words) -> int:
    """Measures the length of the words in the length including spaces"""
    return len(' '.join([*wordList, *words]))

  def paintMeLike(self, widget: TextLabel) -> TextLabel:
    """Describes the painting operation."""
    self.begin(widget)
    self.setFont(widget.textFont)
    self.setPen(widget.fontPen)
    viewRect = self.viewport()
    flags = widget.alignmentFlags
    text = widget.currentText
    textRect = self.boundingRect(viewRect, flags, text)
    self.drawText(viewRect, flags, text)
    return widget
