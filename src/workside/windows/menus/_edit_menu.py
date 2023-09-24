"""WorkSide - Windows - Menus - EditMenu
Menu implementation for the 'edit' menu."""
#  MIT Licence
#  Copyright (c) 2023 Asger Jon Vistisen
from __future__ import annotations

from PySide6.QtCore import Signal

from workside.windows.actions import CutAction, CopyAction, PasteAction, \
  PreferencesAction
from workside.windows.menus import AbstractMenu


class EditMenu(AbstractMenu):
  """WorkSide - Windows - Menus - DebugMenu
  Test menu"""

  cutSignal = Signal()
  copySignal = Signal()
  pasteSignal = Signal()
  preferencesSignal = Signal()

  def __init__(self, *args, **kwargs) -> None:
    AbstractMenu.__init__(self, *args, **kwargs)
    self.setTitle('Edit')
    self.setToolTipsVisible(True)
    cutAction = CutAction(self.parent())
    copyAction = CopyAction(self.parent())
    pasteAction = PasteAction(self.parent())
    preferencesAction = PreferencesAction(self.parent())
    #  Adding actions
    self.addAction(cutAction)
    self.addAction(copyAction)
    self.addAction(pasteAction)
    self.addSeparator()
    self.addAction(preferencesAction)
    #  Connecting signals
    cutAction.triggered.connect(self.cutSignal.emit)
    copyAction.triggered.connect(self.copySignal.emit)
    pasteAction.triggered.connect(self.pasteSignal.emit)
    preferencesAction.triggered.connect(self.preferencesSignal.emit)
