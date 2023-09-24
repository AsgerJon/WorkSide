"""WorkSide - Windows - Actions - SaveAsAction
Action creating a new file on disk and saves current progress to it."""
#  MIT Licence
#  Copyright (c) 2023 Asger Jon Vistisen
from __future__ import annotations

from PySide6.QtCore import Qt
from workside.settings import CTRL, SHIFT
from workside.windows.actions import AbstractAction


class SaveAsAction(AbstractAction):
  """WorkSide - Windows - Actions - SaveAction
  Action updating file on disk with current state."""

  def __init__(self, *args, **kwargs) -> None:
    AbstractAction.__init__(self, *args, **kwargs)
    icon = self.iconFactory('save_as')
    tip = self.monoSpace("""Save to New Filename""")
    text = 'Save As'
    self.setText(text)
    self.setIcon(icon)
    self.setShortcutVisibleInContextMenu(True)
    self.setStatusTip(tip)
    self.setToolTip(tip)
    key = self.keyFactory('S')
    sequence = self.keySequenceFactory(key, CTRL | SHIFT, )
    self.setShortcut(sequence)
    self.setShortcutContext(Qt.ShortcutContext.ApplicationShortcut)
