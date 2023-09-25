"""workside - Core - AbstractMouseRegion
Code writing assistant"""
#  Copyright (c) 2023 Asger Jon Vistisen
#  MIT Licence
from __future__ import annotations

from PySide6.QtCore import QPointF, QRectF
from PySide6.QtGui import QPaintEvent

from workside.painters import HoverPainter
from workside.widgets import AbstractMouseRegionProperties


class AbstractMouseRegion(AbstractMouseRegionProperties):
  """Abstract baseclass for mouse sensitive widgets"""

  def _getMouseLeft(self, **kwargs) -> int:
    return self.mouseRegion.left()

  def _getMouseTop(self, **kwargs) -> int:
    return self.mouseRegion.top()

  def _getMouseRight(self, **kwargs) -> int:
    return self.mouseRegion.right()

  def _getMouseBottom(self, **kwargs) -> int:
    return self.mouseRegion.bottom()

  def _getMouseRegion(self, **kwargs) -> QRectF:
    return self.innerRect.toRectF()

  def __init__(self, *args, **kwargs) -> None:
    AbstractMouseRegionProperties.__init__(self, *args, **kwargs)
    self.setMouseTracking(True)

  def __contains__(self, point: QPointF) -> bool:
    """Checks if the point would be inside the mouse region"""
    if self.mouseLeft < point.x() < self.mouseRight:
      if self.mouseTop < point.y() < self.mouseBottom:
        return True
    return False

  def updateCursorPosition(self, mousePoint: QPointF) -> None:
    """This method updates cursor location information."""
    if mousePoint not in self:
      return
    px, py = self.mousePX, self.mousePY
    vx, vy = self.mouseVX, self.mouseVY
    p = mousePoint
    self.mousePX, self.mousePY, self.mousePoint = p.x(), p.y(), p
    dt = 2 ** 32 - 1
    if self._mouseMove:
      dt = max(1, 1000 - self._mouseMove.remainingTime())
    self.mouseVX = (self.mousePX - px) / dt
    self.mouseVY = (self.mousePY - py) / dt
    self.mouseAX = (self.mouseVX - vx) / dt
    self.mouseAY = (self.mouseVY - vy) / dt
    self._mouseMove.start()
    self.update()

  def paintEvent(self, event: QPaintEvent) -> None:
    """Adds state dependent fill to the inner rectangle."""
    if self.underMouse:
      HoverPainter(self)
    AbstractMouseRegionProperties.paintEvent(self, event)
