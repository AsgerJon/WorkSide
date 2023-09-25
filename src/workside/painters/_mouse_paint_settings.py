"""WorkSide - Painters - MousePaintSettings
Code writing assistant"""
#  Copyright (c) 2023 Asger Jon Vistisen
#  MIT Licence
from __future__ import annotations

from workside.settings import Color, getBaseBrush, getBasePen, Black, Line

MouseBaseFill = getBaseBrush(Color(191, 191, 191, 255))
MouseHoverFill = getBaseBrush(Color(143, 143, 143, 255))
MouseCheckedFill = getBaseBrush(Color(169, 169, 169, 255))
MouseCheckedHoverFill = getBaseBrush(Color(127, 127, 127, 255))

MouseBaseLine = getBasePen(Black, 1, Line)
MouseHoverLine = getBasePen(Black, 3, Line)
MouseCheckedLine = getBasePen(Black, 1, Line)
MouseCheckedHoverLine = getBasePen(Black, 3, Line)
