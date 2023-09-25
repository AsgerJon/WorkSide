"""WorkToy - Core - PushButton 
Code writing assistant"""
#  MIT Licence
#  Copyright (c) 2023 Asger Jon Vistisen
from __future__ import annotations

from PySide6.QtGui import QPaintEvent, QColor
from icecream import ic

from workside.painters import OutlineBackground
from workside.settings import Pink, getBaseBrush, getBasePen
from workside.widgets import AbstractButton

ic.configureOutput(includeContext=True)


class PushButton(AbstractButton):
  """Implementation of push button"""

  def __init__(self, *args, **kwargs) -> None:
    AbstractButton.__init__(self, *args, **kwargs)
    btnTextKeys = self.stringList("""text, title, label""")
    btnTextKwarg = self.searchKey(*btnTextKeys, **kwargs)
    btnTextArg = self.maybeType(str, *args)
    btnTextDefault = 'fuck you!'
    self.lineLength = 40
    self.currentText = self.maybe(btnTextKwarg, btnTextArg, btnTextDefault)
    self.textAlign = 'center'

  def paintEvent(self, event: QPaintEvent) -> None:
    """LMAO"""
    AbstractButton.paintEvent(self, event)
    if self.underMouse:
      OutlineBackground(self, getBasePen(Pink, 3))
