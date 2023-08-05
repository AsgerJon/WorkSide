"""DebugButton is a subclass of AbstractButton allowing implementation of
various functionality for use in more specific subclasses"""
#  Copyright (c) 2023 Asger Jon Vistisen
#  MIT Licence
from __future__ import annotations

from typing import NoReturn

from PySide6.QtCore import Qt
from PySide6.QtGui import QPaintEvent, QPainter
from icecream import ic

from workside.styles import darkSquareStyle, labelStyle, \
  outlineStyle
from workside.widgets import CoreWidget, AbstractButton

ic.configureOutput(includeContext=True)


class DebugButton(AbstractButton):
  """DebugButton is a subclass of AbstractButton allowing implementation of
  various functionality for use in more specific subclasses
  #  Copyright (c) 2023 Asger Jon Vistisen
  #  MIT Licence"""

  def __init__(self, *args, **kwargs) -> None:
    self._text = None
    AbstractButton.__init__(self, *args, **kwargs)
    self.leftPressHold.connect(lambda: print(
      'AbstractButton: Left PressHold!'))
    self.leftClick.connect(lambda: print(
      'AbstractButton: Left SingleClick!'))
    self.leftDoubleClick.connect(lambda: print(
      'AbstractButton: Left DoubleClick!'))

    self.rightPressHold.connect(lambda: print(
      'AbstractButton: Right PressHold!'))
    self.rightClick.connect(lambda: print(
      'AbstractButton: Right SingleClick!'))
    self.rightDoubleClick.connect(lambda: print(
      'AbstractButton: Right DoubleClick!'))

    self.middlePressHold.connect(lambda: print(
      'AbstractButton: Middle PressHold!'))
    self.middleClick.connect(lambda: print(
      'AbstractButton: Middle SingleClick!'))
    self.middleDoubleClick.connect(lambda: print(
      'AbstractButton: Middle DoubleClick!'))

    self.backPressHold.connect(lambda: print(
      'AbstractButton: Back PressHold!'))
    self.backClick.connect(lambda: print(
      'AbstractButton: Back SingleClick!'))
    self.backDoubleClick.connect(lambda: print(
      'AbstractButton: Back DoubleClick!'))

    self.forwardPressHold.connect(lambda: print(
      'AbstractButton: Forward PressHold!'))
    self.forwardClick.connect(lambda: print(
      'AbstractButton: Forward SingleClick!'))
    self.forwardDoubleClick.connect(lambda: print(
      'AbstractButton: Forward DoubleClick!'))

  def _createText(self, ) -> NoReturn:
    """Creator-function for the text"""
    self._text = 'Hello there, I\'m the debug button!'

  def _getText(self, ) -> str:
    """Getter-function for the text"""
    if self._text is None:
      self._createText()
      return self._getText()
    if isinstance(self._text, str):
      return self._text
    msg = """Expected text to be of type %s, but received: %s!"""
    raise TypeError(msg % (str, type(self._text)))

  def update(self, ) -> NoReturn:
    """Brings a resize before the parent update"""
    boundingRect = self.getStyle().getBoundingRect(self._getText())
    self.setMinimumSize(boundingRect.size().toSize())
    return CoreWidget.update(self)

  def paintEvent(self, event: QPaintEvent) -> NoReturn:
    """Implementation of paint event"""
    painter = QPainter()
    painter.begin(self)
    style = darkSquareStyle if self.hover else outlineStyle
    style @ painter
    viewRect = painter.viewport()
    painter.drawRect(viewRect)
    labelStyle @ painter
    painter.drawText(viewRect, Qt.AlignmentFlag.AlignCenter, self._getText())
    painter.end()
