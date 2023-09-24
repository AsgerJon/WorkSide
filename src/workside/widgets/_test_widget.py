"""WorkSide - Widgets - TestWidget
Tester Widget"""
#  MIT Licence
#  Copyright (c) 2023 Asger Jon Vistisen
from __future__ import annotations

from PySide6.QtGui import QPaintEvent, QMouseEvent
from icecream import ic

from workside.painters import PaintRect
from workside.settings import getBaseBrush, Pink, Lime
from workside.settings import getBasePen, Black, Orange
from workside.widgets import AbstractWidget

from worktoy.settings import AlignFlag, AlignCenter

ic.configureOutput(includeContext=True)


class TestWidget(AbstractWidget):
  """WorkSide - Widgets - TestWidget
  Tester Widget"""

  def __init__(self, *args, **kwargs) -> None:
    AbstractWidget.__init__(self, *args, **kwargs)
    self.innerHeight = 128
    self.innerWidth = 256
    self.setMouseTracking(True)
    self.__alignment_rule__ = AlignCenter

  def paintEvent(self, event: QPaintEvent) -> None:
    """Implementation"""
    pen = getBasePen()
    PaintRect(self, self.outerRect, pen, getBaseBrush(Lime, ))
    PaintRect(self, self.borderedRect, pen, getBaseBrush(Black, ))
    PaintRect(self, self.paddedRect, pen, getBaseBrush(Pink, ))
    PaintRect(self, self.innerRect, pen, getBaseBrush(Orange, ))

  def __str__(self) -> str:
    msg = """Left: %d, top: %d, right: %d, bottom %d, """
    right, bottom = self.outerRight, self.outerBottom
    left, top = self.outerLeft, self.outerTop
    return msg % (left, top, right, bottom)

  def __repr__(self, ) -> str:
    return self.__str__()

  def mouseReleaseEvent(self, event: QMouseEvent) -> None:
    """Implementation"""

  def mouseDoubleClickEvent(self, event: QMouseEvent) -> None:
    """Implementation"""
