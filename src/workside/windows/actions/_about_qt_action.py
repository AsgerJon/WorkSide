"""WorkSide - Windows - Actions - AboutQtAction
Action opening the Qt information dialog."""
#  MIT Licence
#  Copyright (c) 2023 Asger Jon Vistisen
from __future__ import annotations

from PySide6.QtCore import Qt

from workside.settings import NoMod
from workside.windows.actions import AbstractAction


class AboutQtAction(AbstractAction):
  """WorkSide - Windows - Actions - AboutQtAction
  Action opening the Qt information dialog."""

  def __init__(self, *args, **kwargs) -> None:
    AbstractAction.__init__(self, *args, **kwargs)
    icon = self.iconFactory('qt')
    tip = self.monoSpace("""About Qt""")
    text = 'About Qt'
    self.setText(text)
    self.setIcon(icon)
    self.setShortcutVisibleInContextMenu(True)
    self.setStatusTip(tip)
    self.setToolTip(tip)
    key = self.keyFactory('F11')
    sequence = self.keySequenceFactory(key, NoMod)
    self.setShortcut(sequence)
    self.setShortcutContext(Qt.ShortcutContext.ApplicationShortcut)
