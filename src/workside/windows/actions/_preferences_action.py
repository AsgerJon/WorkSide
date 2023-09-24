"""WorkSide - Windows - Actions - PreferencesAction
Action opening the preferences."""
#  MIT Licence
#  Copyright (c) 2023 Asger Jon Vistisen
from __future__ import annotations

from PySide6.QtCore import Qt

from workside.settings import NoMod
from workside.windows.actions import AbstractAction


class PreferencesAction(AbstractAction):
  """WorkSide - Windows - Actions - PreferencesAction
  Action activating pasting from clipboard."""

  def __init__(self, *args, **kwargs) -> None:
    AbstractAction.__init__(self, *args, **kwargs)
    icon = self.iconFactory('preferences')
    tip = self.monoSpace("""Open Application Preferences""")
    text = 'Preferences'
    self.setText(text)
    self.setIcon(icon)
    self.setShortcutVisibleInContextMenu(True)
    self.setStatusTip(tip)
    self.setToolTip(tip)
    key = self.keyFactory('F12')
    sequence = self.keySequenceFactory(key, NoMod)
    self.setShortcut(sequence)
    self.setShortcutContext(Qt.ShortcutContext.ApplicationShortcut)
