"""WorkSide - Core - AbstractMouseRegion
Code writing assistant"""
#  Copyright (c) 2023 Asger Jon Vistisen
#  MIT Licence
from __future__ import annotations

from abc import abstractmethod
from typing import cast

from PySide6.QtCore import QEvent, QPointF, QRectF
from PySide6.QtGui import QMouseEvent
from PySide6.QtWidgets import QWidget
from icecream import ic
from worktoy.descriptors import Attribute

from workside.settings import NoBtn
from workside.settings import MouseRelease, MouseMove
from workside.settings import SinglePress, DoublePress, Leave, Enter
from workside.widgets import AbstractButtonTimer

ic.configureOutput(includeContext=True)
