"""The button decorates the CoreWidget with a mouse button"""
#  Copyright (c) 2023 Asger Jon Vistisen
#  MIT Licence
from __future__ import annotations

from typing import NoReturn

from PySide6.QtCore import Qt
from icecream import ic
from worktoy.typetools import CallMeMaybe

ic.configureOutput(includeContext=True)


def buttonFactory(button: Qt.MouseButton) -> CallMeMaybe:
  """The button decorates the CoreWidget with a mouse button
  #  Copyright (c) 2023 Asger Jon Vistisen
  #  MIT Licence"""

  def decorator(cls: type) -> type:
    """The actual decorator returned by the factory"""
    ButtonName = ('%s' % button).split('.')[-1]
    buttonName = '%s%s' % (ButtonName[0].lower(), ButtonName[1:])
    getButtonName = '_get%s'

    init = getattr(cls, '__init__', None)
    if init is None:
      raise KeyError('__init__')

    def _postInit(self, ) -> NoReturn:
      """Extra __init__"""
      setattr(self, buttonName, None)

    def newInit(self, *args, **kwargs) -> NoReturn:
      """New init function"""
      init(self, *args, **kwargs)
      _postInit(self)

    setattr(cls, '__init__', newInit)

    def _createButton(self, ) -> NoReturn:
      """Creator-function for the button instance"""
      setattr(self, )
