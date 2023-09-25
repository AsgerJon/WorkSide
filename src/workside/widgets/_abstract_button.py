"""WorkToy - Core - AbstractButton
Code writing assistant"""
#  Copyright (c) 2023 Asger Jon Vistisen
#  MIT Licence
from __future__ import annotations

from abc import abstractmethod
from typing import cast

from PySide6.QtCore import QEvent, QPointF, QRectF
from PySide6.QtGui import QMouseEvent
from PySide6.QtWidgets import QWidget
from icecream import ic
from worktoy.descriptors import Attribute

from workside.settings import NoBtn
from workside.settings import MouseRelease, MouseMove
from workside.settings import SinglePress, DoublePress, Leave, Enter
from workside.widgets import AbstractButtonTimer

ic.configureOutput(includeContext=True)


class AbstractButton(AbstractButtonTimer):
  """Abstract baseclass for mouse sensitive widgets"""

  underMouse = Attribute(False)
  mousePoint = Attribute(QPointF(0, 0))
  mouseX = Attribute(0.)
  mouseY = Attribute(0.)
  mouseVX = Attribute(0.)
  mouseVY = Attribute(0.)
  mouseAX = Attribute(0.)
  mouseAY = Attribute(0.)
  mouseState = Attribute(NoBtn)
  mouseArea = Attribute(QRectF())
  mouseLeft = Attribute()
  mouseTop = Attribute()
  mouseRight = Attribute()
  mouseBottom = Attribute()

  def __init__(self, *args, **kwargs) -> None:
    AbstractButtonTimer.__init__(self, *args, **kwargs)
    self.setMouseTracking(True)

  @mouseArea.GET
  @abstractmethod
  def getMouseArea(self, ) -> str:
    """Getter-function for the mouse area. Subclass must implement this
    method to define which part of the widget are to be considered by the
    mouse events."""

  def event(self, widgetEvent: QEvent) -> bool:
    """Implementation of event handling"""
    handleResults = [
      self.handleMousePress(widgetEvent),
      self.handleMouseRelease(widgetEvent),
      self.handleEnter(widgetEvent),
      self.handleLeave(widgetEvent),
      self.handleMove(widgetEvent),
    ]
    if any(handleResults):
      return True
    return QWidget.event(self, widgetEvent)

  def handleMousePress(self, event: QEvent) -> bool:
    """Catches mouse press events and double click events"""
    if not event.type() in [SinglePress, DoublePress]:
      return False
    self.activeButton = event.button()
    oldButton, newButton = self.activeButton, None
    if isinstance(event, QMouseEvent):
      newButton = event.button()
    if newButton is None:
      raise TypeError
    if oldButton == NoBtn:
      self.activeButton = newButton
    elif oldButton != newButton:
      self.activeButton = NoBtn
      self.resetTimers()
      return True
    self.getActiveTimer()
    if self._waitForSingleClick:
      self.resetTimers()
      self._waitForSingleRelease.start()
      return True
    if self._waitForDoubleClick:
      self.resetTimers()
      self._waitForDoubleRelease.start()
      return True
    if self._waitForTripleClick:
      self.resetTimers()
      self.emitTripleClick()
      # self._waitForTripleRelease.start()
      return True
    self.resetTimers()
    self._waitForSingleRelease.start()
    return True

  def handleMouseRelease(self, event: QEvent) -> bool:
    """Catches mouse press events"""
    if not event.type() in [MouseRelease]:
      return False
    # self.getActiveTimer()
    if self._waitForSingleRelease:
      self.resetTimers()
      self._waitForDoubleClick.start()
      return True
    if self._waitForDoubleRelease:
      self.resetTimers()
      self._waitForTripleClick.start()
      return True
    if self._waitForTripleRelease:
      self.resetTimers()
      self._waitForTripleRelease.start()
      return True
    return True

  def handleEnter(self, event: QEvent) -> bool:
    """Handles mouse enter events"""
    if not event.type() in [Enter]:
      return False
    self.resetTimers()
    self.mouseX, self.mouseY = event.position().x(), event.position().y()
    self.mouseVX, self.mouseVY, self.mouseAX, self.mouseAY = 0, 0, 0, 0
    self.underMouse = True
    self.update()
    return True

  def handleLeave(self, event: QEvent) -> bool:
    """Handles mouse enter events"""
    if not event.type() in [Leave]:
      return False
    self.underMouse = False
    self.activeButton = NoBtn
    if self._waitForDoubleClick:
      print('leave emit single')
      self.resetTimers()
      self.emitSingleClick()
    if self._waitForTripleClick:
      print('leave emit double')
      self.resetTimers()
      self.emitDoubleClick()
    self.update()
    return True

  def __contains__(self, mousePoint: QPointF) -> bool:
    """Instances of QPointF that are inside the mouse area rectangle are
    considered to be 'in' this instance."""

  def handleMove(self, event: QEvent) -> bool:
    """Handles mouse move events"""
    if not event.type() in [MouseMove]:
      return False
    event = cast(QMouseEvent, event)
    mousePosition = event.position()
    if mousePosition in self and isinstance(mousePosition, QPointF):
      self.updateCursorPosition(mousePosition)

  def updateCursorPosition(self, mousePoint: QPointF) -> None:
    """This method updates cursor location information."""
    px, py = self.mouseX, self.mouseY
    vx, vy = self.mouseVX, self.mouseVY
    p = mousePoint
    self.mouseX, self.mouseY, self.mousePoint = p.x(), p.y(), p
    dt = 2 ** 32 - 1
    if self._mouseMove:
      dt = max(1, 1000 - self._mouseMove.remainingTime())
    self.mouseVX = (self.mouseX - px) / dt
    self.mouseVY = (self.mouseY - py) / dt
    self.mouseAX = (self.mouseVX - vx) / dt
    self.mouseAY = (self.mouseVY - vy) / dt
    self._mouseMove.start()
    self.update()

  def __str__(self) -> str:
    return '%s: %s' % (self.__class__.__qualname__, self.currentText)

  def __repr__(self, ) -> str:
    """Code Representation"""
    return '%s(%s)' % (self.__class__.__qualname__, self.currentText)
