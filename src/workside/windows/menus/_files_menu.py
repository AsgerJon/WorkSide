"""WorkSide - Windows - Menus - DebugMenu
Menu implementation for the 'files' menu."""
#  MIT Licence
#  Copyright (c) 2023 Asger Jon Vistisen
from __future__ import annotations

from PySide6.QtCore import Signal

from workside.windows.menus import AbstractMenu
from workside.windows.actions import NewAction, OpenAction
from workside.windows.actions import SaveAsAction, SaveAction


class FilesMenu(AbstractMenu):
  """WorkSide - Windows - Menus - DebugMenu
  Test menu"""

  newSignal = Signal()
  openSignal = Signal()
  saveSignal = Signal()
  saveAsSignal = Signal()

  def __init__(self, *args, **kwargs) -> None:
    AbstractMenu.__init__(self, *args, **kwargs)
    self.setTitle('Files')
    self.setToolTipsVisible(True)
    newAction = NewAction(self.parent())
    openAction = OpenAction(self.parent())
    saveAction = SaveAction(self.parent())
    saveAsAction = SaveAsAction(self.parent())
    #  Adding actions
    self.addAction(newAction)
    self.addAction(openAction)
    self.addSeparator()
    self.addAction(saveAction)
    self.addAction(saveAsAction)
    #  Connecting signals
    newAction.triggered.connect(self.newSignal.emit)
    openAction.triggered.connect(self.openSignal.emit)
    saveAction.triggered.connect(self.saveSignal.emit)
    saveAsAction.triggered.connect(self.saveAsSignal.emit)
