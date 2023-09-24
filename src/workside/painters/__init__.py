"""WorkSide - Painters
Collection of specialized subclasses of QPainter"""
#  MIT Licence
#  Copyright (c) 2023 Asger Jon Vistisen
from __future__ import annotations

from ._abstract_painter_attributes import AbstractPainterProperties
from ._abstract_painter import AbstractPainter
from ._fill_background import FillBackground
from ._outline_background import OutlineBackground
from ._paint_rect import PaintRect
from ._print_text_widget import PrintTextWidget
from ._print_rect_text import PrintRectText
