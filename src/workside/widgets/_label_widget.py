"""WorkSide - Widgets - LabelWidget
This widget provides label functionality. By default, it shows the text it
holds in a private variable accessed through the 'text' field. This text
is styled according to the data in a private variable 'fontSpec'. These
are static in the default implementation, but subclasses can implement
state sensitive styles and dynamic text."""
#  Copyright (c) 2023 Asger Jon Vistisen
#  MIT Licence
from __future__ import annotations

from PySide6.QtGui import QPaintEvent, QPainter
from worktoy.descriptors import Field

from workside.widgets import CoreWidget


class LabelWidget(CoreWidget):
  """WorkSide - Widgets - LabelWidget
  This widget provides label functionality."""
