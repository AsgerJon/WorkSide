"""WorkSide - Settings - Event
This module provides shortcuts to the Qt namespace related to """
#  MIT Licence
#  Copyright (c) 2023 Asger Jon Vistisen
from __future__ import annotations

from PySide6.QtCore import QEvent

EvType = QEvent.Type

MouseSingle = QEvent.Type.MouseButtonPress
MouseRelease = QEvent.Type.MouseButtonRelease
MouseDouble = QEvent.Type.MouseButtonDblClick
