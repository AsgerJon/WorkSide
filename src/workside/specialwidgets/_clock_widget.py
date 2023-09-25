"""WorkToy - Core - ClockWidget 
Code writing assistant"""
#  Copyright (c) 2023 Asger Jon Vistisen
#  MIT Licence
from __future__ import annotations

from time import ctime

from PySide6.QtCore import QTimer
from PySide6.QtGui import QPaintEvent
from icecream import ic
from worktoy.settings import AlignBottom, AlignHCenter

from workside.settings import Coarse, Precise
from workside.widgets import TextWidget


class ClockWidget(TextWidget):
  """Subclass of TextWidget showing the current time"""

  def __init__(self, *args, **kwargs) -> None:
    TextWidget.__init__(self, *args, **kwargs)
    self.setMouseTracking(True)
    self.fontFamily = 'Courier'
    self.fontSize = 9
    self.paddingLeft = 3
    self.paddingRight = 3
    self.paddingTop = 1
    self.alignment = AlignHCenter | AlignBottom
    self._clockTimer = None
    self.currentText = ctime()
    self.lineLength = len(ctime()) + 2
    self.getClockTimer().start()

  def createClockTimer(self) -> None:
    """Creator function for clock timer"""
    self._clockTimer = QTimer()
    self._clockTimer.setTimerType(Precise)
    self._clockTimer.setInterval(250)
    # self._clockTimer.setSingleShot(True)
    self._clockTimer.timeout.connect(self.refresh)

  def getClockTimer(self, **kwargs) -> QTimer:
    """Getter-function for clock timer"""
    if self._clockTimer is None:
      if kwargs.get('_recursion', False):
        from worktoy.waitaminute import RecursiveCreateGetError
        creator = self.createClockTimer
        varType = QTimer
        varName = 'leftTimer'
        raise RecursiveCreateGetError(creator, varType, varName)
      self.createClockTimer()
      return self.getClockTimer(_recursion=True)
    return self._clockTimer

  def refresh(self) -> None:
    """Refresh"""
    self.currentText = ctime()
    self.update()

  def paintEvent(self, event: QPaintEvent) -> None:
    """LMAO"""
    TextWidget.paintEvent(self, event)
