"""WorkSide - Settings - Pen and Brush
This module provides shortcuts to the Qt namespace related to QPen and
QBrush."""
#  MIT Licence
#  Copyright (c) 2023 Asger Jon Vistisen
from __future__ import annotations

from typing import TYPE_CHECKING

from PySide6.QtCore import Qt
from PySide6.QtGui import QPen, QColor
from icecream import ic

from worktoy.worktoyclass import WorkToyClass

ic.configureOutput(includeContext=True)

if TYPE_CHECKING:
  from workside.settings import Color, Black

PenStyle = Qt.PenStyle
Line = Qt.PenStyle.SolidLine
NoLine = Qt.PenStyle.NoPen
Dash = Qt.PenStyle.DashLine
DashDot = Qt.PenStyle.DashDotLine
DashDotDot = Qt.PenStyle.DashDotDotLine
blankPen = QPen(NoLine)


def getBasePen(color: Color = None,
               width: int = None,
               style: PenStyle = None) -> QPen:
  """Creator function for instances of QPen."""
  pen = QPen()
  color = WorkToyClass().maybe(color, QColor(0, 0, 0, 255))
  width = WorkToyClass().maybe(width, 1)
  style = WorkToyClass().maybe(style, Line)
  if isinstance(color, QColor):
    pen.setColor(color)
  else:
    pen.setColor(color.Q)
  pen.setWidth(width)
  pen.setStyle(style)
  return pen
