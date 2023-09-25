"""WorkToy - Core - PrintRectText
Code writing assistant"""
#  Copyright (c) 2023 Asger Jon Vistisen
#  MIT Licence
from __future__ import annotations

from typing import Any
from typing import TYPE_CHECKING

from PySide6.QtCore import QRect
from worktoy.settings import AlignCenter

from workside.painters import AbstractPainter

if TYPE_CHECKING:
  from workside.widgets import AbstractWidget
else:
  from PySide6.QtWidgets import QWidget as AbstractWidget


class PrintRectText(AbstractPainter):
  """Flexible printing given a widget providing the style settings, 
  a QRect and a text."""

  def __init__(self, *args, **kwargs) -> None:
    AbstractPainter.__init__(self, *args, **kwargs)

  def paintMeLike(self, *args, ) -> Any:
    """Collects text and QRect from the positional arguments,"""
    rectArg = self.maybeType(QRect, *args)
    widgetRect = None
    widgetText = None
    widgetArg = self.maybeType(AbstractWidget, *args)
    if isinstance(widgetArg, AbstractWidget):
      widgetRect = widgetArg.rect()
      widgetText = getattr(widgetArg, 'currentText', None)
    rect = self.maybe(rectArg, widgetRect, self.viewport())
    text = self.maybe(widgetText, 'LMAO')
    self.drawText(self.viewport(), AlignCenter, text)
    return widgetArg
