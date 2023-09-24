"""WorkSide - Widgets - TextWidget
Base class for text showing widgets"""
#  MIT Licence
#  Copyright (c) 2023 Asger Jon Vistisen
from __future__ import annotations

from PySide6.QtCore import QMargins
from PySide6.QtGui import QPaintEvent, QPainter, QBrush, QColor
from PySide6.QtWidgets import QSizePolicy
from icecream import ic

from workside.painters import (PrintTextWidget, PaintRect,
                               OutlineBackground, \
  FillBackground)
from workside.settings import Fill, getBaseBrush, getBasePen, Black
from workside.widgets import TextWidgetVirtuals, AbstractWidget
from worktoy.settings import AlignCenter, AlignLeft, AlignVCenter, AlignTop

ic.configureOutput(includeContext=True)


class TextWidget(TextWidgetVirtuals, ):
  """WorkSide - Widgets - TextWidget
  Base class for text showing widgets"""

  def getInnerHeight(self) -> int:
    """Getter-function for the inner height"""
    try:
      return (self.boundRect + self.paintMargins).height()
    except AttributeError:
      return AbstractWidget.getInnerHeight(self)

  def getInnerWidth(self) -> int:
    """Getter-function for the inner height"""
    try:
      return (self.boundRect + self.paintMargins).width()
    except AttributeError:
      return AbstractWidget.getInnerWidth(self)

  def __init__(self, *args, **kwargs) -> None:
    TextWidgetVirtuals.__init__(self, *args, **kwargs)
    self.setSizePolicy(QSizePolicy.Policy.Maximum,
                       QSizePolicy.Policy.Maximum, )
    self.alignment = AlignCenter

  def paintEvent(self, event: QPaintEvent) -> None:
    """Implementation"""
    brush = getBaseBrush(QColor(191, 191, 191, 255))
    FillBackground(self, brush)
    OutlineBackground(self, getBasePen(Black, 1))
    PrintTextWidget(self)
