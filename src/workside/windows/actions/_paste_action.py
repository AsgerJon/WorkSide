"""WorkSide - Windows - Actions - PasteAction
Action activating pasting from clipboard."""
#  MIT Licence
#  Copyright (c) 2023 Asger Jon Vistisen
from __future__ import annotations

from PySide6.QtCore import Qt
from workside.settings import CTRL
from workside.windows.actions import AbstractAction


class PasteAction(AbstractAction):
  """WorkSide - Windows - Actions - PasteAction
  Action activating pasting from clipboard."""

  def __init__(self, *args, **kwargs) -> None:
    AbstractAction.__init__(self, *args, **kwargs)
    icon = self.iconFactory('paste')
    tip = self.monoSpace("""Pasting from Clipboard""")
    text = 'Paste'
    self.setText(text)
    self.setIcon(icon)
    self.setShortcutVisibleInContextMenu(True)
    self.setStatusTip(tip)
    self.setToolTip(tip)
    key = self.keyFactory('V')
    sequence = self.keySequenceFactory(key, CTRL, )
    self.setShortcut(sequence)
    self.setShortcutContext(Qt.ShortcutContext.ApplicationShortcut)
