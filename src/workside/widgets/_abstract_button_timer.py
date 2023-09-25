"""WorkToy - Core - AbstractButtonTimers
Class providing the timers for use by the buttons"""
#  Copyright (c) 2023 Asger Jon Vistisen
#  MIT Licence
from __future__ import annotations

from PySide6.QtCore import Signal
from PySide6.QtGui import QPaintEvent
from icecream import ic
from worktoy.descriptors import Attribute

from workside.painters import FillBackground
from workside.settings import WaitForSingleReleaseLimit
from workside.settings import NoBtn, Mouse
from workside.settings import WaitForDoubleCLickLimit
from workside.settings import WaitForSingleHoldLimit
from workside.settings import WaitForDoubleReleaseLimit
from workside.settings import WaitForDoubleHoldLimit
from workside.settings import WaitForTripleClickLimit
from workside.timer import Timer
from workside.widgets import TextWidget

ic.configureOutput(includeContext=True)


class AbstractButtonTimer(TextWidget):
  """Class providing the timers for use by the buttons."""

  activeButton = Attribute(NoBtn)

  singleClick = Signal(Mouse)
  doubleClick = Signal(Mouse)
  tripleClick = Signal(Mouse)
  singlePressHold = Signal(Mouse)
  doublePressHold = Signal(Mouse)

  def __init__(self, *args, **kwargs) -> None:
    self.__ready__ = False
    TextWidget.__init__(self, *args, **kwargs)
    self.setMouseTracking(True)
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
    self._mouseMove = Timer(self, 1000)
    label = self.maybeType(str, *args)
    self.currentText = label
    self._waitForDoubleClick.timeout.connect(self.emitSingleClick)
    self._waitForTripleClick.timeout.connect(self.emitDoubleClick)
    self._waitForSingleRelease.timeout.connect(self._waitForSingleHold.start)
    self._waitForDoubleRelease.timeout.connect(self._waitForDoubleHold.start)
    self._waitForSingleHold.timeout.connect(self.emitSinglePressHold)
    self._waitForDoubleHold.timeout.connect(self.emitDoublePressHold)

    self.getActiveTimer()
    self.__ready__ = True

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

  def paintEvent(self, event: QPaintEvent) -> None:
    """Adds state dependent fill to the inner rectangle."""
    TextWidget.paintEvent(self, event)
