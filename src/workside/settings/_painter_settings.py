"""WorkToy - Core - PainterSettings
Provides names of painter settings"""
#  MIT Licence
#  Copyright (c) 2023 Asger Jon Vistisen
from __future__ import annotations

from PySide6.QtGui import QPainter

RenderHint = QPainter.RenderHint
Antialiasing = QPainter.RenderHint.Antialiasing
RenderText = RenderHint.TextAntialiasing
