"""WorkSide - Widgets - TextWidget
Implementing text labels on the paint event."""
#  Copyright (c) 2023 Asger Jon Vistisen
#  MIT Licence
from __future__ import annotations

from PySide6.QtGui import QPaintEvent

from workside.widgets import CoreWidget


class TextWidget(CoreWidget):
  """WorkSide - Widgets - TextWidget
  Implementing text labels on the paint event."""

  def __init__(self, text: str, *args, **kwargs) -> None:
    CoreWidget.__init__(self, *args, **kwargs)

  def getAlignmentFlags(self) -> int:
    """Getter-function for the alignment flag."""

  def paintEvent(self, event: QPaintEvent) -> None:
    """Implementation through the WorkPainter class."""
