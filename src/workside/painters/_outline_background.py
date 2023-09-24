"""WorkSide - Painters - OutlineBackground
Invoking this painter draws the outline surrounding the viewport."""
#  MIT Licence
#  Copyright (c) 2023 Asger Jon Vistisen
from __future__ import annotations

from PySide6.QtCore import QMargins
from PySide6.QtGui import QPen
from icecream import ic

from workside.painters import AbstractPainter
from workside.settings import blankBrush, NoLine, Line
from workside.widgets import AbstractWidget

ic.configureOutput(includeContext=True)


class OutlineBackground(AbstractPainter):
  """WorkSide - Painters - FillBackground
  Invoking this painter fills the background on the paint device calling."""

  def __init__(self, *args, **kwargs) -> None:
    AbstractPainter.__init__(self, *args, **kwargs)

  def paintMeLike(self, widget: AbstractWidget, *args) -> AbstractWidget:
    """Fills the background on the widget. """
    viewMargins = widget.paintMargins
    viewRect = self.viewport()
    self.setBrush(blankBrush)
    self.drawRoundedRect(viewRect - viewMargins, 0, 0)
    return widget
