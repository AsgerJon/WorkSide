"""WorkSide - Windows - Actions - OpenAction
Action opening existing project."""
#  MIT Licence
#  Copyright (c) 2023 Asger Jon Vistisen
from __future__ import annotations

from PySide6.QtCore import Qt
from workside.settings import CTRL
from workside.windows.actions import AbstractAction


class OpenAction(AbstractAction):
  """WorkSide - Windows - Actions - NewAction
  Action creating new project."""

  def __init__(self, *args, **kwargs) -> None:
    AbstractAction.__init__(self, *args, **kwargs)
    icon = self.iconFactory('open')
    tip = self.monoSpace("""Open an Existing Project""")
    text = 'Open Existing'
    self.setText(text)
    self.setIcon(icon)
    self.setShortcutVisibleInContextMenu(True)
    self.setStatusTip(tip)
    self.setToolTip(tip)
    key = self.keyFactory('O')
    sequence = self.keySequenceFactory(key, CTRL, )
    self.setShortcut(sequence)
    self.setShortcutContext(Qt.ShortcutContext.ApplicationShortcut)
