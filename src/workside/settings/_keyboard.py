"""WorkSide - Settings - Keyboard
Names and settings related to keyboard and key modifiers."""
#  MIT Licence
#  Copyright (c) 2023 Asger Jon Vistisen
from __future__ import annotations

import os

from PySide6.QtCore import Qt, QKeyCombination
from PySide6.QtGui import QIcon, QPixmap, QKeySequence

KEY = Qt.Key

KeyMod = Qt.KeyboardModifier
CTRL = KeyMod.ControlModifier
SHIFT = KeyMod.ShiftModifier
ALT = KeyMod.AltModifier
KeyPad = KeyMod.KeypadModifier
NoMod = KeyMod.NoModifier


def getNamedKey(name: str) -> KEY:
  """Getter-function for named key. This function attempts to find a
  member of the enum matching the input given. """

  for key in KEY:
    if name.lower() in key.lower():
      return key
  raise KeyError


def getIcon(icon: str) -> QIcon:
  """Getter-function for named icon"""
  here = os.path.dirname(__file__)
  there = '../icons'
  fileName = '%s.png' % icon
  filePath = os.path.join(here, there, fileName)
  pix = QPixmap(filePath)
  return QIcon(pix)


def getKey(keyChar: str) -> Qt.Key:
  """Getter-function for keyboard key matching given character"""
  keyName = 'Key_%s' % (keyChar.upper())
  for item in Qt.Key:
    if keyName == item.name:
      return item


def getShortCut(keyChar: str, modifier: KeyMod) -> QKeySequence:
  """Getter-function for shortcut key sequence"""
  key = getKey(keyChar)
  combination = QKeyCombination(modifier, key)
  return QKeySequence(combination)
