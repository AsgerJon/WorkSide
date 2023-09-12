"""WorkSide - Widgets - CoreWidget
This is the baseclass for the widgets."""
#  Copyright (c) 2023 Asger Jon Vistisen
#  MIT Licence
from __future__ import annotations

from PySide6.QtWidgets import QWidget
from worktoy.worktoyclass import WorkToyClass


class CoreWidget(QWidget, WorkToyClass):
  """WorkSide - Widgets - CoreWidget
  This is the baseclass for the widgets."""

  def __init__(self, *args, **kwargs) -> None:
    WorkToyClass.__init__(self, *args, **kwargs)
    parent = self.maybeType(QWidget, *args)
    QWidget.__init__(self, parent)
