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

from workside.paint import FontStyle
from workside.widgets import CoreWidget


class LabelWidget(CoreWidget):
  """WorkSide - Widgets - LabelWidget
  This widget provides label functionality."""

  fontStyle = Field()
  text = Field()

  def __init__(self, *args, **kwargs) -> None:
    CoreWidget.__init__(self, *args, **kwargs)
    self._text = 'LMAO'
    self._fontStyle = FontStyle.getBaseSpec()

  @text.GET
  def getText(self) -> str:
    """Getter-function for the underlying text"""
    return self._text

  @text.SET
  def setText(self, text: str) -> None:
    """Setter-function for the underlying text"""
    self._text = text

  @fontStyle.GET
  def getFontStyle(self, ) -> FontStyle:
    """Getter-function for FontStyle"""
    return self._fontStyle

  @fontStyle.SET
  def setFontStyle(self, fontStyle: FontStyle) -> None:
    """Setter-function for FontStyle"""
    self._fontStyle = fontStyle

  def paintEvent(self, event: QPaintEvent) -> None:
    """Implementation of paint event."""
    painter = QPainter()
    painter.begin(self)
    self.fontStyle.apply(painter)
    painter.end()
