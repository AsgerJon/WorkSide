"""WorkSide - Windows - Menus - MainMenuBar
Subclass implementing the menubar in the main application window."""
#  MIT Licence
#  Copyright (c) 2023 Asger Jon Vistisen
from __future__ import annotations

from PySide6.QtCore import Signal
from PySide6.QtGui import QAction
from icecream import ic

from workside.windows.menus import FilesMenu, AbstractMenuBar, EditMenu, \
  HelpMenu, DebugMenu

ic.configureOutput(includeContext=True)


class MainMenuBar(AbstractMenuBar):
  """WorkSide - Windows - Menus - MainMenu
  Subclass implementing the menubar in the main application window."""

  newSignal = Signal()
  openSignal = Signal()
  saveSignal = Signal()
  saveAsSignal = Signal()
  cutSignal = Signal()
  copySignal = Signal()
  pasteSignal = Signal()
  preferencesSignal = Signal()
  aboutWorkSideSignal = Signal()
  aboutQtSignal = Signal()
  hoverSignal = Signal(QAction)
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
    AbstractMenuBar.__init__(self, *args, **kwargs)
    filesMenu = FilesMenu(self.parent())
    editMenu = EditMenu(self.parent())
    helpMenu = HelpMenu(self.parent())
    debugMenu = DebugMenu(self.parent())
    self.hovered.connect(self.hoverHandle)
    self.addMenu(filesMenu)
    self.addMenu(editMenu)
    self.addMenu(helpMenu)
    self.addMenu(debugMenu)
    #  Connecting signals
    #  - Files
    filesMenu.newSignal.connect(self.newSignal.emit)
    filesMenu.openSignal.connect(self.openSignal.emit)
    filesMenu.saveSignal.connect(self.saveSignal.emit)
    filesMenu.saveAsSignal.connect(self.saveAsSignal.emit)
    #  - Edit
    editMenu.cutSignal.connect(self.cutSignal.emit)
    editMenu.copySignal.connect(self.copySignal.emit)
    editMenu.pasteSignal.connect(self.pasteSignal.emit)
    editMenu.preferencesSignal.connect(self.preferencesSignal.emit)
    #  - Help
    helpMenu.aboutQtSignal.connect(self.aboutQtSignal.emit)
    helpMenu.aboutWorkSideSignal.connect(self.aboutWorkSideSignal.emit)
    #  - Debug
    debugMenu.debugSignal01.connect(self.debugSignal01.emit)
    debugMenu.debugSignal02.connect(self.debugSignal02.emit)
    debugMenu.debugSignal03.connect(self.debugSignal03.emit)
    debugMenu.debugSignal04.connect(self.debugSignal04.emit)
    debugMenu.debugSignal05.connect(self.debugSignal05.emit)
    debugMenu.debugSignal06.connect(self.debugSignal06.emit)
    debugMenu.debugSignal07.connect(self.debugSignal07.emit)
    debugMenu.debugSignal08.connect(self.debugSignal08.emit)
    debugMenu.debugSignal09.connect(self.debugSignal09.emit)
    debugMenu.debugSignal10.connect(self.debugSignal10.emit)
    debugMenu.debugSignal11.connect(self.debugSignal11.emit)
    debugMenu.debugSignal12.connect(self.debugSignal12.emit)

  def hoverHandle(self, action: QAction) -> None:
    """Handles hover signal"""
    self.hoverSignal.emit(action)
