"""WorkToy - Core - DebugMenu
Debug menu"""
#  MIT Licence
#  Copyright (c) 2023 Asger Jon Vistisen
from __future__ import annotations

from PySide6.QtCore import Signal

from workside.windows.actions import DebugAction
from workside.windows.menus import AbstractMenu


class DebugMenu(AbstractMenu):
  """WorkToy - Core - DebugMenu
  Debug menu"""

  debugSignal01 = Signal()
  debugSignal02 = Signal()
  debugSignal03 = Signal()
  debugSignal04 = Signal()
  debugSignal05 = Signal()
  debugSignal06 = Signal()
  debugSignal07 = Signal()
  debugSignal08 = Signal()
  debugSignal09 = Signal()
  debugSignal10 = Signal()
  debugSignal11 = Signal()
  debugSignal12 = Signal()

  def __init__(self, *args, **kwargs) -> None:
    AbstractMenu.__init__(self, *args, **kwargs)
    self.setTitle('Edit')
    self.setToolTipsVisible(True)
    debugAction01 = DebugAction(self.parent(), 1)
    debugAction02 = DebugAction(self.parent(), 2)
    debugAction03 = DebugAction(self.parent(), 3)
    debugAction04 = DebugAction(self.parent(), 4)
    debugAction05 = DebugAction(self.parent(), 5)
    debugAction06 = DebugAction(self.parent(), 6)
    debugAction07 = DebugAction(self.parent(), 7)
    debugAction08 = DebugAction(self.parent(), 8)
    debugAction09 = DebugAction(self.parent(), 9)
    debugAction10 = DebugAction(self.parent(), 10)
    debugAction11 = DebugAction(self.parent(), 11)
    debugAction12 = DebugAction(self.parent(), 12)
    debugAction01.triggered.connect(self.debugSignal01.emit)
    debugAction02.triggered.connect(self.debugSignal02.emit)
    debugAction03.triggered.connect(self.debugSignal03.emit)
    debugAction04.triggered.connect(self.debugSignal04.emit)
    debugAction05.triggered.connect(self.debugSignal05.emit)
    debugAction06.triggered.connect(self.debugSignal06.emit)
    debugAction07.triggered.connect(self.debugSignal07.emit)
    debugAction08.triggered.connect(self.debugSignal08.emit)
    debugAction09.triggered.connect(self.debugSignal09.emit)
    debugAction10.triggered.connect(self.debugSignal10.emit)
    debugAction11.triggered.connect(self.debugSignal11.emit)
    debugAction12.triggered.connect(self.debugSignal12.emit)
    self.addAction(debugAction01)
    self.addAction(debugAction02)
    self.addAction(debugAction03)
    self.addAction(debugAction04)
    self.addAction(debugAction05)
    self.addAction(debugAction06)
    self.addAction(debugAction07)
    self.addAction(debugAction08)
    self.addAction(debugAction09)
    self.addAction(debugAction10)
    self.addAction(debugAction11)
    self.addAction(debugAction12)
