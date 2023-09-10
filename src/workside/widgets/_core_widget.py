"""WorkSide - Widgets - CoreWidget
The core widget is the abstract baseclass shared by the widgets in the
WorkSide framework."""
#  Copyright (c) 2023 Asger Jon Vistisen
#  MIT Licence
from __future__ import annotations

from PySide6.QtWidgets import QWidget
from worktoy.worktoyclass import WorkToyClass


class CoreWidget(QWidget, WorkToyClass, ):
  """WorkSide - Widgets - CoreWidget
  The core widget is the abstract baseclass shared by the widgets in the
  WorkSide framework."""

  def __init__(self, *args, **kwargs) -> None:
    self._events = {}
    WorkToyClass.__init__(self, *args, **kwargs)
    parent = self.maybe(QWidget, *args)
    QWidget.__init__(self, parent)
    self.setMouseTracking(True)
