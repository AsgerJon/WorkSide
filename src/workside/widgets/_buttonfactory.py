"""The button decorates the CoreWidget with a mouse button"""
#  Copyright (c) 2023 Asger Jon Vistisen
#  MIT Licence
from __future__ import annotations

from typing import NoReturn

from PySide6.QtCore import Qt, Signal, QCoreApplication
from PySide6.QtGui import QMouseEvent
from icecream import ic
from worktoy.typetools import CallMeMaybe

from workside.widgets import MouseButton

ic.configureOutput(includeContext=True)

buttonDict = dict(
  left=Qt.MouseButton.LeftButton,
  right=Qt.MouseButton.RightButton,
  middle=Qt.MouseButton.MiddleButton,
  back=Qt.MouseButton.BackButton,
  forward=Qt.MouseButton.ForwardButton,
)


def buttonFactory(button: Qt.MouseButton | str) -> CallMeMaybe:
  """The button decorates the CoreWidget with a mouse button
  #  Copyright (c) 2023 Asger Jon Vistisen
  #  MIT Licence"""

  if isinstance(button, str):
    try:
      return buttonFactory(buttonDict.get(button))
    except KeyError as e:
      print('Could not recognize %s as name of mouse button!' % button)
      raise e

  if not isinstance(button, Qt.MouseButton):
    msg = """Expected button to be of type %s, but received %s!"""
    raise TypeError(msg % (Qt.MouseButton, type(button)))

  def decorator(cls: type) -> type:
    """The actual decorator returned by the factory"""
    ButtonName = ('%s' % button).split('.')[-1]
    buttonName = '%s%s' % (ButtonName[0].lower(), ButtonName[1:])
    _buttonName = '_%s' % buttonName
    getButtonName = '_get%s' % ButtonName
    createButtonName = '_create%s' % ButtonName
    shortName = buttonName.replace('Button', '')
    pressHoldName = '%sPressHold' % shortName
    singleClickName = '%sClick' % shortName
    doubleClickName = '%sDoubleClick' % shortName

    setattr(cls, pressHoldName, Signal())
    setattr(cls, singleClickName, Signal())
    setattr(cls, doubleClickName, Signal())

    def _createButton(self, ) -> NoReturn:
      """Creator-function for the button instance"""
      mouseButton = MouseButton(self, button)
      button.pressHold.connect(getattr(self, pressHoldName, ))
      button.singleClick.connect(getattr(self, singleClickName, ))
      button.doubleClick.connect(getattr(self, doubleClickName, ))
      setattr(self, _buttonName, mouseButton)

    setattr(cls, createButtonName, _createButton)

    def _getButton(self, ) -> MouseButton:
      """Getter-function for button"""
      if getattr(self, _buttonName, ):
        _create = getattr(self, createButtonName)
        _create()
        getter = getattr(self, '_getButton')
        return getter()
      finalButton = getattr(self, _buttonName)
      if isinstance(finalButton, MouseButton):
        return finalButton
      msg = """Expected button to be of type MouseButton, but received %s"""
      raise TypeError(msg % (type(self)))

    setattr(cls, getButtonName, _getButton)

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

    oldPress = getattr(cls, 'mousePressEvent')
    oldRelease = getattr(cls, 'mouseReleaseEvent')
    oldDoubleClick = getattr(cls, 'mouseDoubleClickEvent')

    def newPressEvent(self, event: QMouseEvent) -> NoReturn:
      """New mouse press event"""
      getattr(self, _buttonName).mousePressEvent(event)
      oldPress(event)
      return

    def newReleaseEvent(self, event: QMouseEvent) -> NoReturn:
      """New mouse press event"""
      ic(self)
      ic(_buttonName)
      ic(getattr(self, _buttonName))
      if getattr(self, _buttonName) is not None:
        ic(self, _buttonName)
      else:

        QCoreApplication.quit()
      getattr(self, _buttonName).mouseReleaseEvent(event)
      oldRelease(event)
      return

    def newDoubleClick(self, event: QMouseEvent) -> NoReturn:
      """New mouse press event"""
      getattr(self, _buttonName).mouseDoubleClickEvent(event)
      oldDoubleClick(event)
      return

    setattr(cls, 'mousePressEvent', newPressEvent)
    setattr(cls, 'mouseReleaseEvent', newReleaseEvent)
    setattr(cls, 'mouseDoubleClickEvent', newDoubleClick)

    return cls

  return decorator
