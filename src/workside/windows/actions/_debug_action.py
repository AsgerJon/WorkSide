"""WorkToy - Core - DebugAction
Code writing assistant"""
#  MIT Licence
#  Copyright (c) 2023 Asger Jon Vistisen
from __future__ import annotations

from PySide6.QtCore import Qt

from workside.windows.actions import AbstractAction


class DebugAction(AbstractAction):
  """WorkToy - Core - DebugAction
  Debugging action"""

  def __init__(self, *args, **kwargs) -> None:
    AbstractAction.__init__(self, *args, **kwargs)
    icon = self.iconFactory('risitas')
    debugNum = self.maybeType(int, *args)
    debugNum = self.maybe(debugNum, 1)
    text = 'DEBUG %02d' % debugNum
    tip = self.monoSpace('DEBUG %02d' % debugNum)
    self.setText(text)
    self.setIcon(icon)
    self.setShortcutVisibleInContextMenu(True)
    self.setStatusTip(tip)
    self.setToolTip(tip)
    key = self.keyFactory('F%d' % debugNum)
    sequence = self.keySequenceFactory(key, )
    self.setShortcut(sequence)
    self.setShortcutContext(Qt.ShortcutContext.ApplicationShortcut)
