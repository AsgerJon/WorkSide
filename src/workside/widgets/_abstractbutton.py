"""AbstractButton is a class providing fundamental functionality"""
#  Copyright (c) 2023 Asger Jon Vistisen
#  MIT Licence
from __future__ import annotations

from typing import NoReturn

from PySide6.QtCore import Signal, QEvent, Qt, QTimer
from PySide6.QtGui import QEnterEvent, QMouseEvent, QPaintEvent, QPainter
from PySide6.QtWidgets import QSizePolicy
from icecream import ic

from workside.settings import flag, Settings
from workside.styles import lightSquareStyle, darkSquareStyle, labelStyle
from workside.widgets import CoreWidget, MouseButton, buttonFactory

ic.configureOutput(includeContext=True)


@buttonFactory(Qt.MouseButton.LeftButton)
@buttonFactory(Qt.MouseButton.RightButton)
@buttonFactory(Qt.MouseButton.MiddleButton)
@buttonFactory(Qt.MouseButton.BackButton)
@buttonFactory(Qt.MouseButton.ForwardButton)
@flag('hover')
@flag('moving')
class AbstractButton(CoreWidget):
  """AbstractButton is a class providing fundamental functionality
  #  Copyright (c) 2023 Asger Jon Vistisen
  #  MIT Licence"""

  hoverEnter = Signal()
  hoverLeave = Signal()
  leftPressHold = Signal()
  leftClick = Signal()
  leftDoubleClick = Signal()
  rightPressHold = Signal()
  rightClick = Signal()
  rightDoubleClick = Signal()

  def __init__(self, *args, **kwargs) -> None:
    CoreWidget.__init__(self, *args, **kwargs)
    self.setMouseTracking(True)
    _policy = self.createSizePolicy(
      vertical=QSizePolicy.Policy.Maximum,
      horizontal=QSizePolicy.Policy.Maximum,
    )
    self.setSizePolicy(_policy)
    self._movingDelayTimer = None
    # self._leftButton = None
    # self._rightButton = None
    # self._middleButton = None
    # self._forwardButton = None
    # self._backButton = None
    self.leftPressHold.connect(lambda: print('left press hold'))
    self.leftClick.connect(lambda: print('left single click'))
    self.leftDoubleClick.connect(lambda: print('left double click'))
    self.rightPressHold.connect(lambda: print('right press hold'))
    self.rightClick.connect(lambda: print('right single click'))
    self.rightDoubleClick.connect(lambda: print('right double click'))

  #
  # def _createLeftButton(self) -> NoReturn:
  #   """Creator function for left button"""
  #   self._leftButton = MouseButton(self, btn=Qt.MouseButton.LeftButton)
  #   self._leftButton.pressHold.connect(self.leftPressHold.emit)
  #   self._leftButton.singleClick.connect(self.leftClick.emit)
  #   self._leftButton.doubleClick.connect(self.leftDoubleClick.emit)
  #
  # def _getLeftButton(self) -> MouseButton:
  #   """Getter-function for the left mouse button"""
  #   if self._leftButton is None:
  #     self._createLeftButton()
  #     return self._getLeftButton()
  #   if isinstance(self._leftButton, MouseButton):
  #     return self._leftButton
  #   raise TypeError
  #
  # def _createRightButton(self) -> NoReturn:
  #   """Creator function for right mouse button"""
  #   self._rightButton = MouseButton(self, btn=Qt.MouseButton.RightButton)
  #   self._rightButton.pressHold.connect(self.rightPressHold.emit)
  #   self._rightButton.singleClick.connect(self.rightClick.emit)
  #   self._rightButton.doubleClick.connect(self.rightDoubleClick.emit)
  #
  # def _getRightButton(self) -> MouseButton:
  #   """Getter-function for the right mouse button"""
  #   if self._rightButton is None:
  #     self._createRightButton()
  #     return self._getRightButton()
  #   if isinstance(self._rightButton, MouseButton):
  #     return self._rightButton
  #   raise TypeError

  def _createMovingDelayTimer(self) -> NoReturn:
    """Creator function for the moving delay. """
    self._movingDelayTimer = QTimer()
    self._movingDelayTimer.setTimerType(Qt.TimerType.PreciseTimer)
    self._movingDelayTimer.setInterval(Settings.movingDelayTime)
    self._movingDelayTimer.setSingleShot(True)
    self._movingDelayTimer.timeout.connect(self.deactivateMoving)

  def getMovingDelayTimer(self) -> QTimer:
    """Getter-function for the moving delay timer"""
    if self._movingDelayTimer is None:
      self._createMovingDelayTimer()
      return self.getMovingDelayTimer()
    if isinstance(self._movingDelayTimer, QTimer):
      return self._movingDelayTimer
    raise TypeError

  def enterEvent(self, event: QEnterEvent) -> NoReturn:
    """Implementation of enter event"""
    self.setStyle(lightSquareStyle)
    self.activateMoving()
    self.activateHover()
    self.hoverEnter.emit()
    self.repaint()
    CoreWidget.enterEvent(self, event)

  def leaveEvent(self, event: QEvent) -> NoReturn:
    """Implementation of leave event"""
    self.setStyle(darkSquareStyle)
    self.deactivateMoving()
    self.deactivateHover()
    self.hoverLeave.emit()
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

  def mousePressEvent(self, event: QMouseEvent) -> NoReturn:
    """Implementation of mouse press event"""
    self._getLeftButton().mousePressEvent(event)
    self._getRightButton().mousePressEvent(event)
    CoreWidget.mousePressEvent(self, event)

  def mouseReleaseEvent(self, event: QMouseEvent) -> NoReturn:
    """Implementation of mouse release event"""
    self._getLeftButton().mouseReleaseEvent(event)
    self._getRightButton().mouseReleaseEvent(event)
    CoreWidget.mouseReleaseEvent(self, event)

  def mouseDoubleClickEvent(self, event: QMouseEvent) -> NoReturn:
    """Implementation of double click event"""
    self._getLeftButton().mouseDoubleClickEvent(event)
    self._getRightButton().mouseDoubleClickEvent(event)
    CoreWidget.mouseDoubleClickEvent(self, event)

  def paintEvent(self, event: QPaintEvent) -> NoReturn:
    """Implementation of paint event"""
    painter = QPainter()
    painter.begin(self)
    style = lightSquareStyle if self.hover else darkSquareStyle
    style @ painter
    viewRect = painter.viewport()
    painter.drawRect(viewRect)
    labelStyle @ painter
    painter.drawText(viewRect, Qt.AlignmentFlag.AlignCenter, 'LOL')
    painter.end()
