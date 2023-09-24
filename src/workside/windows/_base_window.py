"""WorkSide - Windows - BaseWindow
Base window inheriting from QMainWindow setting the menus and actions."""
#  MIT Licence
#  Copyright (c) 2023 Asger Jon Vistisen
from __future__ import annotations

from PySide6.QtCore import Signal
from PySide6.QtGui import QAction
from PySide6.QtWidgets import QMainWindow, QWidget, QApplication, QStatusBar

from workside.windows.dialogs import AboutWorkSide
from workside.windows.menus import MainMenuBar, StatusBar
from worktoy.worktoyclass import WorkToyClass


class BaseWindow(QMainWindow, WorkToyClass):
  """WorkSide - Windows - BaseWindow
  Base window inheriting from QMainWindow setting the menus and actions."""

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

  def __init__(self, *args, **kwargs) -> None:
    WorkToyClass.__init__(self, *args, **kwargs)
    parent = self.maybeType(QWidget, *args)
    QMainWindow.__init__(self, parent)
    mainMenuBar = MainMenuBar(self)
    statusBar = StatusBar()
    self.setStatusBar(statusBar)
    self.setMenuBar(mainMenuBar)
    self.aboutWorkSideDialog = AboutWorkSide()

    mainMenuBar.newSignal.connect(self.newProject)
    mainMenuBar.openSignal.connect(self.openFile)
    mainMenuBar.saveSignal.connect(self.saveFile)
    mainMenuBar.saveAsSignal.connect(self.saveAsFile)
    mainMenuBar.cutSignal.connect(self.cutFunction)
    mainMenuBar.copySignal.connect(self.copyFunction)
    mainMenuBar.pasteSignal.connect(self.pasteFunction)
    mainMenuBar.preferencesSignal.connect(self.preferencesFunction)
    mainMenuBar.aboutWorkSideSignal.connect(self.aboutWorkSideDialog.show)
    mainMenuBar.aboutQtSignal.connect(QApplication.aboutQt)
    mainMenuBar.hoverSignal.connect(self.hoverActionFunc)
    mainMenuBar.debugSignal01.connect(self.debugFunc01)
    mainMenuBar.debugSignal02.connect(self.debugFunc02)
    mainMenuBar.debugSignal03.connect(self.debugFunc03)
    mainMenuBar.debugSignal04.connect(self.debugFunc04)
    mainMenuBar.debugSignal05.connect(self.debugFunc05)
    mainMenuBar.debugSignal06.connect(self.debugFunc06)
    mainMenuBar.debugSignal07.connect(self.debugFunc07)
    mainMenuBar.debugSignal08.connect(self.debugFunc08)
    mainMenuBar.debugSignal09.connect(self.debugFunc09)
    mainMenuBar.debugSignal10.connect(self.debugFunc10)
    mainMenuBar.debugSignal11.connect(self.debugFunc11)
    mainMenuBar.debugSignal12.connect(self.debugFunc12)

  debugFunc01 = lambda self: None
  debugFunc02 = lambda self: None
  debugFunc03 = lambda self: None
  debugFunc04 = lambda self: None
  debugFunc05 = lambda self: None
  debugFunc06 = lambda self: None
  debugFunc07 = lambda self: None
  debugFunc08 = lambda self: None
  debugFunc09 = lambda self: None
  debugFunc10 = lambda self: None
  debugFunc11 = lambda self: None
  debugFunc12 = lambda self: None

  def hoverActionFunc(self, action: QAction) -> None:
    """Hovers the action"""

    self.statusBar().showMessage(action.text(), -1)

  def show(self) -> None:
    """Reimplementation"""
    QMainWindow.show(self)
    self.update()

  def newProject(self, ) -> None:
    """New project function"""
    print('New project')

  def openFile(self, ) -> None:
    """Open project function"""
    print('Open')

  def saveFile(self, ) -> None:
    """Save project function"""
    print('Save')

  def saveAsFile(self, ) -> None:
    """Save as function"""
    print('Save as')

  def cutFunction(self, ) -> None:
    """Implementation of cutting"""
    print('Cut function')

  def copyFunction(self, ) -> None:
    """Implementation of cutting"""
    print('Copy function')

  def pasteFunction(self, ) -> None:
    """Implementation of cutting"""
    print('Paste function')

  def preferencesFunction(self, ) -> None:
    """Implementation of cutting"""
    print('Preferences function')
