"""WorkSide - Painters - PaintRect
Primitive painting on rectangles."""
#  MIT Licence
#  Copyright (c) 2023 Asger Jon Vistisen
from __future__ import annotations

from PySide6.QtCore import QRectF, QRect, QMargins
from icecream import ic

from workside.painters import AbstractPainter
from workside.widgets import AbstractWidget

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
