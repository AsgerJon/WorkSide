"""WorkSide - Widgets - AbstractWidget
Provides the abstract base class for the widget classes"""
#  Copyright (c) 2023 Asger Jon Vistisen
#  MIT Licence
from __future__ import annotations

from typing import Any, Never

from PySide6.QtCore import QMargins, QRect, QPoint
from PySide6.QtGui import QResizeEvent, QPaintEvent
from PySide6.QtWidgets import QSizePolicy
from icecream import ic

from workside.widgets import AbstractWidgetVirtuals
from worktoy.descriptors import Attribute
from worktoy.settings import AlignCenter, AlignRects

ic.configureOutput(includeContext=True)


class AbstractWidget(AbstractWidgetVirtuals):
  """WorkSide - Widgets - AbstractWidget
  Provides the abstract base class for the widget classes"""

  paintMargins = Attribute()
  alignment = Attribute()
  alignRects = Attribute()

  def __init__(self, *args, **kwargs) -> None:
    AbstractWidgetVirtuals.__init__(self, *args, **kwargs)
    self.setMouseTracking(True)
    minRect = self.outerRect + QMargins(2, 2, 2, 2)
    self.alignment = AlignCenter
    self.setMinimumSize(minRect.size())
    self.setSizePolicy(QSizePolicy.Policy.MinimumExpanding,
                       QSizePolicy.Policy.MinimumExpanding, )

  @paintMargins.GET
  def getPaintMargins(self) -> QMargins:
    """Getter-function for paint margins"""
    margins = QMargins(1, 1, 1, 1)
    return margins

  @alignRects.GET
  def getAlignRects(self) -> AlignRects:
    """Getter-function for QRect alignment"""
    alignRectangles = AlignRects()
    alignRectangles.alignment = self.alignment
    return alignRectangles

  def alignmentRule(self, dynRect: QRect, statRect: QRect) -> QRect:
    """Aligns the rectangles"""
    return self.alignRects(dynRect, statRect)

  def resizeEvent(self, event: QResizeEvent) -> None:
    """Implementation"""
    origin = QPoint(0, 0)
    dynRect = QRect(origin, self.outerSize)
    statRect = QRect(origin, event.size())
    newRect = self.alignmentRule(dynRect, statRect)
    self.outerLeft = newRect.left()
    self.outerTop = newRect.top()
    minRect = self.outerRect + QMargins(2, 2, 2, 2)
    self.setMinimumSize(minRect.size())
    self.update()

  def paintEvent(self, event: QPaintEvent) -> None:
    """Adds state dependent fill to the inner rectangle."""
    AbstractWidgetVirtuals.paintEvent(self, event)
