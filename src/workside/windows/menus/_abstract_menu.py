"""WorkSide - Windows - Menus - AbstractMenu
Baseclass for the custom menus"""
#  MIT Licence
#  Copyright (c) 2023 Asger Jon Vistisen
from __future__ import annotations

import os
from typing import Union

from PySide6.QtCore import Qt, QKeyCombination
from PySide6.QtGui import QIcon, QPixmap, QKeySequence, QAction
from PySide6.QtWidgets import QMenu, QWidget

from workside.settings import KeyMod, getIcon, getKey
from worktoy.worktoyclass import WorkToyClass


class AbstractMenu(QMenu, WorkToyClass):
  """WorkSide - Windows - Menus - AbstractMenu
  Baseclass for the custom menus"""

  @staticmethod
  def actionFactory(name: str,
                    parent: AbstractMenu = None,
                    statusTip: str = None,
                    keyMod: KeyMod = None,
                    key: Union[Qt.Key, str] = None, ) -> QAction:
    """Creates a factory with given name"""
    icon = getIcon(name)
    text = name.capitalize()
    action = QAction(icon, text, parent)
    statusTip = WorkToyClass().maybe(statusTip, text)
    action.setStatusTip(statusTip)
    action.setToolTip(statusTip)
    if isinstance(keyMod, KeyMod):
      if isinstance(key, str):
        key = getKey(key)
      if isinstance(key, Qt.Key):
        shortCut = QKeyCombination(keyMod, key)
        action.setShortcut(shortCut)
    return action

  def __init__(self, *args, **kwargs) -> None:
    WorkToyClass.__init__(self, *args, **kwargs)
    parent = self.maybeType(QWidget, *args)
    QMenu.__init__(self, parent)
    self.hovered.connect(self.handleHover)
    self.triggered.connect(self.handleTrigger)

  def handleHover(self, action: QAction) -> None:
    """Handles the hovered action"""
    action.showStatusText()

  def handleTrigger(self, action: QAction) -> None:
    """Handles the hovered action"""
    action.showStatusText()
