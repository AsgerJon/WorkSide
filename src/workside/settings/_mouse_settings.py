"""WorkSide - Settings - Mouse settings
This module provides shortcuts to the Qt namespace related to QPen."""
#  MIT Licence
#  Copyright (c) 2023 Asger Jon Vistisen
from __future__ import annotations

from PySide6.QtCore import Qt, QEvent

Mouse = Qt.MouseButton

NoBtn = Mouse.NoButton
Left = Mouse.LeftButton
Middle = Mouse.MiddleButton
Right = Mouse.RightButton
Back = Mouse.BackButton
Forward = Mouse.ForwardButton

SinglePress = QEvent.MouseButtonPress
MouseRelease = QEvent.MouseButtonRelease
DoublePress = QEvent.MouseButtonDblClick
MouseMove = QEvent.MouseMove
Enter = QEvent.Enter
Leave = QEvent.Leave
