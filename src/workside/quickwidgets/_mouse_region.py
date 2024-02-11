"""WorkSide - QuickWidget - MouseRegion
This class provides mouse aware functionality. """
#  Copyright (c) 2023 Asger Jon Vistisen
#  MIT Licence
from __future__ import annotations

from PySide6.QtCore import QRect, QPointF
from PySide6.QtGui import QMouseEvent, QResizeEvent
from PySide6.QtWidgets import QWidget
from worktoy.descriptors import Attribute
from worktoy.worktoyclass import WorkToyClass


class MouseRegion(QWidget, WorkToyClass):
  """This class provides mouse aware functionality"""

  left = Attribute()
  top = Attribute()
  right = Attribute()
  bottom = Attribute()
  rect = Attribute()
  underMouse = Attribute()

  def __init__(self, *args, **kwargs) -> None:
    WorkToyClass.__init__(self, *args, **kwargs)
    parent = self.maybeType(QWidget, *args)
    QWidget.__init__(self, parent)
    self.setMouseTracking(True)

  def resizeEvent(self, event: QResizeEvent) -> None:
    """Implementation"""

  @rect.GET
  def getRect(self) -> QRect:
    """GET RECT!"""
    return getattr(self, '__mouse_region__', )

  @rect.SET
  def setRect(self, mouseRegion: QRect) -> None:
    """Setter-function for mouse area"""
    setattr(self, '__mouse_region__', mouseRegion)

  def mouseLeaveHandle(self, mousePoint: QPointF) -> None:
    """Triggered when the mouse cursor leaves the mouse region. (Since the
    mouse region may be smaller than the painter viewport, this method is
    different generally than the leave event."""

  def mouseEnterHandle(self, mousePoint: QPointF):
    """See above"""

  def mouseMoveEvent(self, event: QMouseEvent) -> None:
    """Handle for mouse move event."""
    mousePoint = event.button()
    if self.underMouse and (mousePoint in self):
      pass
