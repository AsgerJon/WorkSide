"""WorkSide - Settings - Brush
This module provides shortcuts to the Qt namespace related to QBrush."""
#  MIT Licence
#  Copyright (c) 2023 Asger Jon Vistisen
from __future__ import annotations

from typing import TYPE_CHECKING
from PySide6.QtCore import Qt
from PySide6.QtGui import QBrush, QColor
from icecream import ic

ic.configureOutput(includeContext=True)
if TYPE_CHECKING:
  from workside.settings import Color

BrushStyle = Qt.BrushStyle
Fill = Qt.BrushStyle.SolidPattern
NoFill = Qt.BrushStyle.NoBrush
blankBrush = QBrush(NoFill)


def getBaseBrush(color: Color) -> QBrush:
  """Creator function for the colored QBrush"""
  brush = QBrush()
  brush.setStyle(Fill)
  if isinstance(color, QColor):
    brush.setColor(color)
  else:
    brush.setColor(color.Q)
  return brush
