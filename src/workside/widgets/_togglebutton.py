"""ToggleButton implements toggling between two states"""
#  Copyright (c) 2023 Asger Jon Vistisen
#  MIT Licence
from __future__ import annotations

from typing import NoReturn

from PySide6.QtCore import Qt, QEvent
from PySide6.QtGui import QPaintEvent, QPainter, QEnterEvent, QMouseEvent
from icecream import ic

from workside.settings import flag, timer, Settings
from workside.styles import lightSquareStyle, darkSquareStyle, labelStyle, \
  outlineStyle
from workside.widgets import CoreWidget, buttonFactory

ic.configureOutput(includeContext=True)


@buttonFactory('left')
@buttonFactory('right')
@buttonFactory('middle')
@buttonFactory('back')
@buttonFactory('forward')
@timer('movingDelay', Settings.movingDelayTime, 'deactivateMoving')
@flag('moving')
@flag('hover', )
@flag('active', )
class ToggleButton(CoreWidget):
  """ToggleButton implements toggling between two states
  #  Copyright (c) 2023 Asger Jon Vistisen
  #  MIT Licence"""

  def __init__(self, *args, **kwargs) -> None:
    CoreWidget.__init__(self, *args, **kwargs)

  def enterEvent(self, event: QEnterEvent) -> NoReturn:
    """Implementation of enter event"""
    self.setStyle(lightSquareStyle)
    self.activateMoving()
    self.activateHover()
    self.repaint()
    CoreWidget.enterEvent(self, event)

  def leaveEvent(self, event: QEvent) -> NoReturn:
    """Implementation of leave event"""
    self.setStyle(darkSquareStyle)
    self.deactivateMoving()
    self.deactivateHover()
    self.update()
    CoreWidget.leaveEvent(self, event)

  def mouseMoveEvent(self, event: QMouseEvent) -> NoReturn:
    """Implementation of mouse move event"""
    if not self._getHover:
      self.activateHover()
    self.activateMoving()
    self.getMovingDelayTimer().stop()
    self.getMovingDelayTimer().start()
    self.update()
    CoreWidget.mouseMoveEvent(self, event)

  def paintEvent(self, event: QPaintEvent) -> NoReturn:
    """Implementation of paint event"""
    painter = QPainter()
    painter.begin(self)
    style = darkSquareStyle if self.hover else outlineStyle
    style @ painter
    viewRect = painter.viewport()
    painter.drawRect(viewRect)
    labelStyle @ painter
    painter.drawText(viewRect, Qt.AlignmentFlag.AlignCenter, 'Toggle')
    painter.end()
