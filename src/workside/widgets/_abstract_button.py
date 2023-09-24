"""WorkToy - Core - AbstractButton
Code writing assistant"""
#  MIT Licence
#  Copyright (c) 2023 Asger Jon Vistisen
from __future__ import annotations

from PySide6.QtCore import QEvent, Signal, QPointF
from PySide6.QtCore import QObject
from PySide6.QtGui import QPaintEvent, QMouseEvent
from PySide6.QtWidgets import QWidget
from icecream import ic

from workside.painters import OutlineBackground, PrintTextWidget
from workside.settings import WaitForSingleReleaseLimit, Pink
from workside.settings import getBasePen
from workside.settings import NoBtn, Mouse
from workside.settings import WaitForDoubleCLickLimit
from workside.settings import WaitForSingleHoldLimit
from workside.settings import WaitForDoubleReleaseLimit
from workside.settings import WaitForDoubleHoldLimit
from workside.settings import WaitForTripleReleaseLimit
from workside.settings import WaitForTripleClickLimit
from workside.settings import MouseRelease, MouseMove
from workside.settings import SinglePress, DoublePress, Leave, Enter
from workside.timer import Timer
from workside.widgets import TextWidget
from worktoy.descriptors import Attribute

ic.configureOutput(includeContext=True)


class AbstractButton(TextWidget):
  """Abstract baseclass for mouse sensitive widgets"""

  singleClick = Signal(Mouse)
  doubleClick = Signal(Mouse)
  tripleClick = Signal(Mouse)
  singlePressHold = Signal(Mouse)
  doublePressHold = Signal(Mouse)

  underMouse = Attribute(False)
  activeButton = Attribute(NoBtn)
  mousePoint = Attribute(QPointF(0, 0))
  mouseX = Attribute(0.)
  mouseY = Attribute(0.)
  mouseVX = Attribute(0.)
  mouseVY = Attribute(0.)
  mouseAX = Attribute(0.)
  mouseAY = Attribute(0.)
  mouseState = Attribute()

  def __init__(self, *args, **kwargs) -> None:
    TextWidget.__init__(self, *args, **kwargs)
    self.setMouseTracking(True)
    if isinstance(self, QObject):
      self._waitForSingleClick = Timer(  # Fake timer
        self, -1, 'Wait for Single Click')
      self._waitForSingleRelease = Timer(
        self, WaitForSingleReleaseLimit, 'Wait for Single Release')
      self._waitForDoubleClick = Timer(
        self, WaitForDoubleCLickLimit, 'Wait for Double Click')
      self._waitForSingleHold = Timer(
        self, WaitForSingleHoldLimit, 'Wait for Single Hold')
      self._waitForDoubleRelease = Timer(
        self, WaitForDoubleReleaseLimit, 'Wait for Double Release')
      self._waitForDoubleHold = Timer(
        self, WaitForDoubleHoldLimit, 'Wait for Double Hold')
      self._waitForTripleClick = Timer(
        self, WaitForTripleClickLimit, 'Wait for Triple Click')
      self._waitForTripleRelease = Timer(
        self, WaitForTripleReleaseLimit, 'Wait for Triple Release')
      self._mouseMove = Timer(self, 1000)
    else:
      raise TypeError
    label = self.maybeType(str, *args)
    self.currentText = label
    self._waitForDoubleClick.timeout.connect(self.emitSingleClick)
    self._waitForTripleClick.timeout.connect(self.emitDoubleClick)
    self._waitForSingleRelease.timeout.connect(self._waitForSingleHold.start)
    self._waitForDoubleRelease.timeout.connect(self._waitForDoubleHold.start)
    self._waitForSingleHold.timeout.connect(self.emitSinglePressHold)
    self._waitForDoubleHold.timeout.connect(self.emitDoublePressHold)

    self.getActiveTimer()

  def emitSinglePressHold(self, ) -> None:
    """Emits the single press-hold"""
    self.resetTimers()
    self.singlePressHold.emit(self.activeButton)

  def emitDoublePressHold(self, ) -> None:
    """Emits the double press-hold"""
    self.resetTimers()
    self.doublePressHold.emit(self.activeButton)

  def emitSingleClick(self, ) -> None:
    """Emits the single click"""
    self.resetTimers()
    self.singleClick.emit(self.activeButton)

  def emitDoubleClick(self, ) -> None:
    """Emits the double click"""
    self.resetTimers()
    self.doubleClick.emit(self.activeButton)

  def emitTripleClick(self, ) -> None:
    """Emits the triple click"""
    self.resetTimers()
    self.tripleClick.emit(self.activeButton)

  def getTimers(self) -> list[Timer]:
    """Getter-function for all timers"""
    return [
      self._waitForSingleClick,
      self._waitForSingleRelease,
      self._waitForDoubleClick,
      self._waitForSingleHold,
      self._waitForDoubleRelease,
      self._waitForDoubleHold,
      self._waitForTripleClick,
      self._waitForTripleRelease,
    ]

  def resetTimers(self) -> bool:
    """Stops all timers."""
    for timer in self.getTimers():
      timer.stop()
    return True

  def getActiveTimer(self, **kwargs) -> Timer:
    """Getter function for first active timer"""
    for timer in self.getTimers():
      if timer.isActive():
        return timer
    if kwargs.get('_recursion', False):
      raise RecursionError
    self._waitForSingleClick.start()
    return self.getActiveTimer()

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

  def handleMove(self, event: QEvent) -> bool:
    """Handles mouse move events"""
    if not event.type() in [MouseMove]:
      return False
    p = event.position()
    px, py = self.mouseX, self.mouseY
    vx, vy = self.mouseVX, self.mouseVY
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
    return True

  def paintEvent(self, event: QPaintEvent) -> None:
    """Reimplementation"""
    x, y = self.mouseVX, self.mouseVY
    self.currentText = 'V: %.3f | %.3f' % (x, y)
    PrintTextWidget(self)

    if self.underMouse:
      OutlineBackground(self, getBasePen(Pink))

  def __str__(self) -> str:
    return '%s: %s' % (self.__class__.__qualname__, self.currentText)

  def __repr__(self, ) -> str:
    """Code Representation"""
    return '%s(%s)' % (self.__class__.__qualname__, self.currentText)
