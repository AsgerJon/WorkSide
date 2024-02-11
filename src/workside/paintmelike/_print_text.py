"""WorkSide - PaintMeLike - PrintText
Prints text on the target widget"""
#  Copyright (c) 2023 Asger Jon Vistisen
#  MIT Licence
from __future__ import annotations

from typing import TYPE_CHECKING

from PySide6.QtGui import QPainter, QFont

from workside.settings import getBasePen, blankPen, getBaseFont


class PrintText(QPainter):
  """WorkSide - PaintMeLike - PrintText
  Prints text on the target widget"""
