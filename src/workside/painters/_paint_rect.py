"""WorkSide - Painters - PaintRect
Primitive painting on rectangles."""
#  Copyright (c) 2023 Asger Jon Vistisen
#  MIT Licence
from __future__ import annotations

from PySide6.QtCore import QRectF, QRect, QMargins
from icecream import ic
from typing import TYPE_CHECKING

from workside.painters import AbstractPainter

if TYPE_CHECKING:
  from workside.widgets import AbstractWidget
else:
  from PySide6.QtWidgets import QWidget as AbstractWidget

ic.configureOutput(includeContext=True)


class PaintRect(AbstractPainter):
  """WorkSide - Painters - PaintRect
  Primitive painting on rectangles."""

  def __init__(self, *args, **kwargs) -> None:
    rect = None
    for arg in args:
      if isinstance(arg, (QRect, QRectF)) and rect is None:
        rect = arg
        if isinstance(arg, QRectF):
          rect = rect.toRect()
    self._rect = rect

    AbstractPainter.__init__(self, *args, **kwargs)

  def getRect(self) -> QRect:
    """Get RECT!!"""
    return self._rect

  def paintMeLike(self, widget: AbstractWidget, ) -> AbstractWidget:
    """Primitive painting on rectangles"""
    viewMargined = self.viewport()
    self.drawRect(self.maybe(self.getRect(), viewMargined))
    return widget
