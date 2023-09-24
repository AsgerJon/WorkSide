"""WorkSide - Widgets - Spacer widgets
Invisible spacer widgets expanding in horizontal, vertical or both
directions."""
#  MIT Licence
#  Copyright (c) 2023 Asger Jon Vistisen
from __future__ import annotations

from PySide6.QtCore import QSize
from PySide6.QtGui import QPaintEvent, QResizeEvent
from PySide6.QtWidgets import QSizePolicy

from workside.painters import OutlineBackground
from workside.settings import getBasePen, Black, Dash
from workside.widgets import AbstractWidget
from worktoy.settings import getPolicy


class VerticalSpacer(AbstractWidget):
  """WorkSide - Widgets - VerticalSpacer
  Invisible spacer item expanding vertically"""

  def __init__(self, *args, **kwargs) -> None:
    AbstractWidget.__init__(self, *args, **kwargs)
    self.innerWidth = 8
    self.setSizePolicy(QSizePolicy.Policy.Maximum,
                       QSizePolicy.Policy.MinimumExpanding, )

  def paintEvent(self, event: QPaintEvent) -> None:
    """Draws a dashed outline"""
    pen = getBasePen(Black, 1, Dash)
    OutlineBackground(self, pen)

  def resizeEvent(self, event: QResizeEvent) -> None:
    """Implementation"""
    self.update()
    return AbstractWidget.resizeEvent(self, event)


class HorizontalSpacer(AbstractWidget):
  """WorkSide - Widgets - HorizontalSpacer
  Invisible spacer item expanding horizontally"""

  def __init__(self, *args, **kwargs) -> None:
    AbstractWidget.__init__(self, *args, **kwargs)
    self.innerHeight = 8
    self.setSizePolicy(QSizePolicy.Policy.MinimumExpanding,
                       QSizePolicy.Policy.Maximum, )

  def paintEvent(self, event: QPaintEvent) -> None:
    """Draws a dashed outline"""
    pen = getBasePen(Black, 1, Dash)
    OutlineBackground(self, pen)

  def resizeEvent(self, event: QResizeEvent) -> None:
    """Implementation"""
    self.update()
    return AbstractWidget.resizeEvent(self, event)


class DoubleSpacer(AbstractWidget):
  """WorkSide - Widgets - VerticalSpacer
  Invisible spacer item expanding in both direction"""

  def __init__(self, *args, **kwargs) -> None:
    AbstractWidget.__init__(self, *args, **kwargs)
    self.setSizePolicy(QSizePolicy.Policy.MinimumExpanding,
                       QSizePolicy.Policy.MinimumExpanding, )

  def paintEvent(self, event: QPaintEvent) -> None:
    """Draws a dashed outline"""
    pen = getBasePen(Black, 1, Dash)
    OutlineBackground(self, pen)

  def resizeEvent(self, event: QResizeEvent) -> None:
    """Implementation"""
    self.update()
    return AbstractWidget.resizeEvent(self, event)
