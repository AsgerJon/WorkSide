"""WorkSide - Painters - HoverPainter
This painter applies hover effect to mouse regions"""
#  Copyright (c) 2023 Asger Jon Vistisen
#  MIT Licence
from __future__ import annotations

from typing import cast, TYPE_CHECKING

from workside.painters import AbstractPainter, MouseBaseLine, MouseHoverLine
from workside.painters import MouseHoverFill, MouseBaseFill

if TYPE_CHECKING:
  from workside.widgets import AbstractWidget, AbstractButton
else:
  from PySide6.QtWidgets import QWidget as AbstractWidget
  from PySide6.QtWidgets import QWidget as AbstractButton


class HoverPainter(AbstractPainter):
  """This painter applies hover effect to mouse regions"""

  def __init__(self, *args, **kwargs) -> None:
    AbstractPainter.__init__(self, *args, **kwargs)

  def paintMeLike(self, widget: AbstractWidget, *args, ) -> AbstractWidget:
    """This painter applies hover effect to mouse regions"""
    widget = cast(AbstractButton, widget)
    self.setPen(MouseHoverLine if widget.underMouse else MouseBaseLine)
    self.setBrush(MouseBaseFill if widget.underMouse else MouseHoverFill)
    mouseRect = widget.mouseRegion
    self.drawRoundedRect(mouseRect, 1, 1)
    return widget
