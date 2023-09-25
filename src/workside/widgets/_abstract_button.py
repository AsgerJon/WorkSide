"""WorkToy - Core - AbstractButton
Code writing assistant"""
#  Copyright (c) 2023 Asger Jon Vistisen
#  MIT Licence
from __future__ import annotations

from abc import abstractmethod
from typing import cast

from PySide6.QtCore import QEvent, QPointF, QRectF
from PySide6.QtGui import QMouseEvent, QPaintEvent
from PySide6.QtWidgets import QWidget
from icecream import ic
from worktoy.descriptors import Attribute

from workside.painters import HoverPainter
from workside.settings import NoBtn
from workside.settings import MouseRelease, MouseMove
from workside.settings import SinglePress, DoublePress, Leave, Enter
from workside.widgets import AbstractMouseRegion

ic.configureOutput(includeContext=True)


class AbstractButton(AbstractMouseRegion):
  """Abstract baseclass for mouse sensitive widgets"""

  def __init__(self, *args, **kwargs) -> None:
    AbstractMouseRegion.__init__(self, *args, **kwargs)
    self.setMouseTracking(True)
    ic(self.__ready__)

  def event(self, widgetEvent: QEvent) -> bool:
    """Implementation of event handling"""
    if self.__ready__:
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
    return True

  def handleEnter(self, mousePoint: QPointF = None) -> bool:
    """Handles mouse enter events"""
    self.underMouse = True
    self.resetTimers()
    self.update()
    return True

  def handleLeave(self, mousePoint: QPointF = None) -> bool:
    """Handles mouse enter events"""
    self.underMouse = False
    if self._waitForDoubleClick:
      self.resetTimers()
      self.emitSingleClick()
    if self._waitForTripleClick:
      self.resetTimers()
      self.emitDoubleClick()
    self.update()
    return True

  def handleMove(self, event: QEvent) -> bool:
    """Handles mouse move events"""
    if not event.type() in [MouseMove]:
      return False
    event = cast(QMouseEvent, event)
    mousePoint = event.position()
    if self.underMouse and mousePoint not in self:
      self.handleLeave()
    if not self.underMouse and mousePoint in self:
      self.handleEnter()
    if mousePoint in self:
      self.updateCursorPosition(mousePoint)

  def __str__(self) -> str:
    return '%s: %s' % (self.__class__.__qualname__, self.currentText)

  def __repr__(self, ) -> str:
    """Code Representation"""
    return '%s(%s)' % (self.__class__.__qualname__, self.currentText)

  def paintEvent(self, event: QPaintEvent) -> None:
    """Adds state dependent fill to the inner rectangle."""
    ic()
    if self.underMouse:
      HoverPainter(self)
    AbstractMouseRegion.paintEvent(self, event)
