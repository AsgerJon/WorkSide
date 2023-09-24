"""WorkSide - Settings - LinePen
Reimplementation of QPen supporting  Color"""
#  MIT Licence
#  Copyright (c) 2023 Asger Jon Vistisen
from __future__ import annotations

from PySide6.QtGui import QPen, QColor

from workside.settings import PenStyle, Color
from worktoy.worktoyclass import WorkToyClass


class LinePen(QPen, WorkToyClass):
  """WorkSide - Settings - LinePen
  Reimplementation of QPen supporting  Color"""
 