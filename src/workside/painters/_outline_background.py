"""WorkSide - Painters - OutlineBackground
Invoking this painter draws the outline surrounding the viewport."""
#  Copyright (c) 2023 Asger Jon Vistisen
#  MIT Licence
from __future__ import annotations

from typing import TYPE_CHECKING

from icecream import ic

from workside.painters import AbstractPainter
from workside.settings import blankBrush

if TYPE_CHECKING:
  from workside.widgets import AbstractWidget
else:
  from PySide6.QtWidgets import QWidget as AbstractWidget

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
