"""WorkSide - Windows - Actions - AboutWorkSideAction
Action opening the workside information dialog AboutWorkSideAction."""
#  MIT Licence
#  Copyright (c) 2023 Asger Jon Vistisen
from __future__ import annotations

from PySide6.QtCore import Qt

from workside.settings import NoMod
from workside.windows.actions import AbstractAction


class AboutWorkSideAction(AbstractAction):
  """WorkSide - Windows - Actions - AboutWorkSideAction
  Action opening the workside information dialog AboutWorkSideAction."""

  def __init__(self, *args, **kwargs) -> None:
    AbstractAction.__init__(self, *args, **kwargs)
    icon = self.iconFactory('workside')
    tip = self.monoSpace("""About WorkSide""")
    text = 'About WorkSide'
    self.setText(text)
    self.setIcon(icon)
    self.setShortcutVisibleInContextMenu(True)
    self.setStatusTip(tip)
    self.setToolTip(tip)
    key = self.keyFactory('F10')
    sequence = self.keySequenceFactory(key, NoMod, )
    self.setShortcut(sequence)
    self.setShortcutContext(Qt.ShortcutContext.ApplicationShortcut)
    self.triggered.connect(lambda: print('about workside'))
