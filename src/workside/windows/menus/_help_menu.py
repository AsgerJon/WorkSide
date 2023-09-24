"""WorkSide - Windows - Menus - HelpMenu
Menu implementation for the 'help' menu."""
#  MIT Licence
#  Copyright (c) 2023 Asger Jon Vistisen
from __future__ import annotations

from PySide6.QtCore import Signal

from workside.windows.actions import AboutQtAction, AboutWorkSideAction
from workside.windows.menus import AbstractMenu


class HelpMenu(AbstractMenu):
  """WorkSide - Windows - Menus - HelpMenu
  Menu implementation for the 'help' menu."""

  aboutQtSignal = Signal()
  aboutWorkSideSignal = Signal()

  def __init__(self, *args, **kwargs) -> None:
    AbstractMenu.__init__(self, *args, **kwargs)
    self.setTitle('Help')
    self.setToolTipsVisible(True)
    aboutQtAction = AboutQtAction(self.parent())
    aboutWorkSideAction = AboutWorkSideAction(self.parent())
    #  Adding actions
    self.addAction(aboutQtAction)
    self.addAction(aboutWorkSideAction)
    #  Connecting signals
    aboutQtAction.triggered.connect(self.aboutQtSignal.emit)
    aboutWorkSideAction.triggered.connect(self.aboutWorkSideSignal.emit)
