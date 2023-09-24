"""WorkSide - Painters - AbstractPainter
Base class for the custom painters"""
#  MIT Licence
#  Copyright (c) 2023 Asger Jon Vistisen
from __future__ import annotations

from abc import abstractmethod

from PySide6.QtCore import Qt
from PySide6.QtGui import QPainter, QBrush, QPen, QFont
from icecream import ic

from workside.painters import AbstractPainterProperties
from workside.widgets import AbstractWidget
from worktoy.descriptors import Attribute

ic.configureOutput(includeContext=True)


class AbstractPainter(QPainter, AbstractPainterProperties):
  """WorkSide - Painters - AbstractPainter
  Base class for the custom painters"""

  def _parseStyles(self, *args) -> tuple:
    """Parses arguments to QFont, QBrush, QPen in the indicated order"""
    font, brush, pen = None, None, None
    for arg in args:
      if isinstance(arg, QFont) and font is None:
        font = arg
      if isinstance(arg, QBrush) and brush is None:
        brush = arg
      if isinstance(arg, QPen) and pen is None:
        pen = arg
    return font, brush, pen

  def __init__(self, *args, **kwargs) -> None:
    AbstractPainterProperties.__init__(self, *args, **kwargs)
    QPainter.__init__(self)
    self.baseFont = self.maybeType(QFont, *args)
    self.baseBrush = self.maybeType(QBrush, *args)
    self.basePen = self.maybeType(QPen, *args)
    widget = self.maybeType(AbstractWidget, *args)
    if isinstance(widget, AbstractWidget):
      self.setRenderHint(QPainter.RenderHint.Antialiasing)
      self.preparePainting(widget, *args)

  def preparePainting(self,
                      widget: AbstractWidget,
                      *args) -> AbstractWidget:
    """Prepares the painter by setting styles if defined"""
    self.begin(widget)
    for arg in args:
      if isinstance(arg, QBrush):
        self.setBrush(arg)
      if isinstance(arg, QPen):
        self.setPen(arg)
      if isinstance(arg, QFont):
        self.setFont(arg)
    self.setRenderHint(QPainter.RenderHint.Antialiasing)
    widget = self.paintMeLike(widget)
    self.end()
    return widget

  @abstractmethod
  def paintMeLike(self, widget: AbstractWidget, *args, ) -> AbstractWidget:
    """This abstract method should define the paint operation assigned to
    the particular subclass. """
