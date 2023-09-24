"""WorkSide - Painters - Actions - AbstractAction
Baseclass for custom actions."""
#  MIT Licence
#  Copyright (c) 2023 Asger Jon Vistisen
from __future__ import annotations

import os
from typing import Union

from PySide6.QtCore import Qt, QKeyCombination
from PySide6.QtGui import QIcon, QPixmap, QAction, QKeySequence
from PySide6.QtWidgets import QWidget

from workside.settings import KeyMod, NoMod
from worktoy.worktoyclass import WorkToyClass


class AbstractAction(QAction, WorkToyClass):
  """WorkSide - Painters - Actions - AbstractAction
  Baseclass for custom actions."""

  def __init__(self, *args, **kwargs) -> None:
    WorkToyClass.__init__(self, *args, **kwargs)
    parent = self.maybeType(QWidget, *args)
    QAction.__init__(self, parent)
    strArgs = self.maybeTypes(str, *args)
    name, tip = None, None
    keyMod = self.maybeType(KeyMod, *args)
    key = self.maybeType(Qt.Key, *args)
    if strArgs:
      name = strArgs.pop(0)
    if strArgs:
      tip = strArgs.pop(0)
    if strArgs and key is None:
      key = self.keyFactory(strArgs.pop(0))
    if isinstance(name, str):
      icon = self.iconFactory(name)
      text = name.capitalize()
      self.setIcon(icon)
      self.setIconVisibleInMenu(True)
      self.setText(text)
    if isinstance(tip, str):
      self.setStatusTip(tip)
      self.setToolTip(tip)
    if isinstance(key, (Qt.Key, str)) and isinstance(keyMod, KeyMod):
      sequence = self.keySequenceFactory(key, keyMod, )
      self.setShortcut(sequence)
      self.setShortcutContext(Qt.ShortcutContext.ApplicationShortcut)

  def pixFactory(self, pixName: str) -> QPixmap:
    """Creates instance of QPixmap matching name."""
    here = os.path.dirname(__file__)
    there = '../icons'
    fileName = '%s.png' % pixName
    filePath = os.path.join(here, there, fileName)
    return QPixmap(filePath)

  def iconFactory(self, iconName: str) -> QIcon:
    """Creates instance of icon matching name. """
    return QIcon(self.pixFactory(iconName))

  def keyFactory(self, keyChar: str) -> Qt.Key:
    """Getter-function for keyboard key matching given character"""
    keyName = 'Key_%s' % (keyChar.upper())
    for item in Qt.Key:
      if keyName == item.name:
        return item

  def keySequenceFactory(self,
                         key: Union[Qt.Key, str],
                         keyMod: KeyMod = None, **kwargs) -> QKeySequence:
    """Creates instance of QKeySequence"""
    keyMod = self.maybe(keyMod, NoMod)
    if isinstance(key, KeyMod) and isinstance(keyMod, (Qt.Key, str)):
      return self.keySequenceFactory(keyMod, key, **kwargs)
    if isinstance(key, Qt.Key):
      combination = QKeyCombination(keyMod, key)
      return QKeySequence(combination)
    if kwargs.get('_recursion', False):
      raise RecursionError
    return self.keySequenceFactory(
      self.keyFactory(key), keyMod, _recursion=True)
