"""WorkSide - Windows - Actions - SaveAction
Action updating file on disk with current state."""
#  MIT Licence
#  Copyright (c) 2023 Asger Jon Vistisen
from __future__ import annotations

from PySide6.QtCore import Qt
from workside.settings import CTRL
from workside.windows.actions import AbstractAction


class SaveAction(AbstractAction):
  """WorkSide - Windows - Actions - SaveAction
  Action updating file on disk with current state."""

  def __init__(self, *args, **kwargs) -> None:
    AbstractAction.__init__(self, *args, **kwargs)
    icon = self.iconFactory('save')
    tip = self.monoSpace("""Save Changes""")
    text = 'Save'
    self.setText(text)
    self.setIcon(icon)
    self.setShortcutVisibleInContextMenu(True)
    self.setStatusTip(tip)
    self.setToolTip(tip)
    key = self.keyFactory('S')
    sequence = self.keySequenceFactory(key, CTRL, )
    self.setShortcut(sequence)
    self.setShortcutContext(Qt.ShortcutContext.ApplicationShortcut)
