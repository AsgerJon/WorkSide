"""WorkSide - Core - AbstractMouseRegion
Code writing assistant"""
#  Copyright (c) 2023 Asger Jon Vistisen
#  MIT Licence
from __future__ import annotations

from abc import abstractmethod
from typing import cast, Never

from PySide6.QtCore import QEvent, QPointF, QRectF
from PySide6.QtGui import QMouseEvent
from PySide6.QtWidgets import QWidget
from icecream import ic
from worktoy.descriptors import Attribute

from moreworktoy import Field
from workside.settings import NoBtn, Mouse
from workside.settings import MouseRelease, MouseMove
from workside.settings import SinglePress, DoublePress, Leave, Enter
from workside.widgets import AbstractButtonTimer, AbstractWidget

ic.configureOutput(includeContext=True)


class AbstractMouseRegion(AbstractWidget, metaclass=type):
  """Documentation"""
  mousePoint = Field()
  underMouse = Field()
  mousePX = Field()
  mousePY = Field()
  mouseVX = Field()
  mouseVY = Field()
  mouseAX = Field()
  mouseAY = Field()
  mouseState = Field()
  mouseRegion = Field()
  mouseLeft = Field()
  mouseTop = Field()
  mouseRight = Field()
  mouseBottom = Field()

  #          || _____________________________________________ ||          #
  #          || mousePoint                                    ||          #
  #          || ¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨ ||          #
  @mousePoint.GET
  def _getMousePoint(self, **kwargs) -> str:
    """Getter function for mousePoint"""
    if self.__mouse_point__ is None:
      if kwargs.get('_recursion', False):
        from worktoy.waitaminute import RecursiveCreateGetError
        creator = self._createMousePoint
        argType = str
        argName = '__mouse_point__'
        raise RecursiveCreateGetError(creator, argType, argName)
      self._createMousePoint()
      return self._getMousePoint(_recursion=True)
    return getattr(self, '__mouse_point__', )

  @mousePoint.SET
  def setMousePoint(self, newValue: str) -> None:
    """Setter-function for mousePoint"""
    setattr(str, '__mouse_point__', newValue)

  @mousePoint.DEL
  def delMousePoint(self, *_) -> Never:
    """Illegal deleter-function for mousePoint"""
    from worktoy.waitaminute import ProtectedAttributeError
    attName = 'mousePoint'
    insName = str(self)
    clsName = self.__class__
    raise ProtectedAttributeError(attName, insName, clsName)

  @mousePoint.CREATE
  def _createMousePoint(self, ) -> None:
    """Creator-function for mousePoint"""
    newInstance = str()
    setattr(str, '__mouse_point__', newInstance)

  #          || _____________________________________________ ||          #
  #          || underMouse                                    ||          #
  #          || ¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨ ||          #
  @underMouse.GET
  def _getUnderMouse(self, **kwargs) -> str:
    """Getter function for underMouse"""
    if self.__under_mouse__ is None:
      if kwargs.get('_recursion', False):
        from worktoy.waitaminute import RecursiveCreateGetError
        creator = self._createUnderMouse
        argType = str
        argName = '__under_mouse__'
        raise RecursiveCreateGetError(creator, argType, argName)
      self._createUnderMouse()
      return self._getUnderMouse(_recursion=True)
    return getattr(self, '__under_mouse__', )

  @underMouse.SET
  def setUnderMouse(self, newValue: str) -> None:
    """Setter-function for underMouse"""
    setattr(str, '__under_mouse__', newValue)

  @underMouse.DEL
  def delUnderMouse(self, *_) -> Never:
    """Illegal deleter-function for underMouse"""
    from worktoy.waitaminute import ProtectedAttributeError
    attName = 'underMouse'
    insName = str(self)
    clsName = self.__class__
    raise ProtectedAttributeError(attName, insName, clsName)

  @underMouse.CREATE
  def _createUnderMouse(self, ) -> None:
    """Creator-function for underMouse"""
    newInstance = str()
    setattr(str, '__under_mouse__', newInstance)

  #          || _____________________________________________ ||          #
  #          || mousePX                                       ||          #
  #          || ¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨ ||          #
  @mousePX.GET
  def _getMousePX(self, **kwargs) -> type:
    """Getter function for mousePX"""
    if self.__mouse_p_x__ is None:
      if kwargs.get('_recursion', False):
        from worktoy.waitaminute import RecursiveCreateGetError
        creator = self._createMousePX
        argType = type
        argName = '__mouse_p_x__'
        raise RecursiveCreateGetError(creator, argType, argName)
      self._createMousePX()
      return self._getMousePX(_recursion=True)
    return getattr(self, '__mouse_p_x__', )

  @mousePX.SET
  def setMousePX(self, newValue: type) -> None:
    """Setter-function for mousePX"""
    setattr(type, '__mouse_p_x__', newValue)

  @mousePX.DEL
  def delMousePX(self, *_) -> Never:
    """Illegal deleter-function for mousePX"""
    from worktoy.waitaminute import ProtectedAttributeError
    attName = 'mousePX'
    insName = str(self)
    clsName = self.__class__
    raise ProtectedAttributeError(attName, insName, clsName)

  @mousePX.CREATE
  def _createMousePX(self, ) -> None:
    """Creator-function for mousePX"""
    newInstance = type()
    setattr(type, '__mouse_p_x__', newInstance)

  #          || _____________________________________________ ||          #
  #          || mousePY                                       ||          #
  #          || ¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨ ||          #
  @mousePY.GET
  def _getMousePY(self, **kwargs) -> type:
    """Getter function for mousePY"""
    if self.__mouse_p_y__ is None:
      if kwargs.get('_recursion', False):
        from worktoy.waitaminute import RecursiveCreateGetError
        creator = self._createMousePY
        argType = type
        argName = '__mouse_p_y__'
        raise RecursiveCreateGetError(creator, argType, argName)
      self._createMousePY()
      return self._getMousePY(_recursion=True)
    return getattr(self, '__mouse_p_y__', )

  @mousePY.SET
  def setMousePY(self, newValue: type) -> None:
    """Setter-function for mousePY"""
    setattr(type, '__mouse_p_y__', newValue)

  @mousePY.DEL
  def delMousePY(self, *_) -> Never:
    """Illegal deleter-function for mousePY"""
    from worktoy.waitaminute import ProtectedAttributeError
    attName = 'mousePY'
    insName = str(self)
    clsName = self.__class__
    raise ProtectedAttributeError(attName, insName, clsName)

  @mousePY.CREATE
  def _createMousePY(self, ) -> None:
    """Creator-function for mousePY"""
    newInstance = type()
    setattr(type, '__mouse_p_y__', newInstance)

  #          || _____________________________________________ ||          #
  #          || mouseVX                                       ||          #
  #          || ¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨ ||          #
  @mouseVX.GET
  def _getMouseVX(self, **kwargs) -> type:
    """Getter function for mouseVX"""
    if self.__mouse_v_x__ is None:
      if kwargs.get('_recursion', False):
        from worktoy.waitaminute import RecursiveCreateGetError
        creator = self._createMouseVX
        argType = type
        argName = '__mouse_v_x__'
        raise RecursiveCreateGetError(creator, argType, argName)
      self._createMouseVX()
      return self._getMouseVX(_recursion=True)
    return getattr(self, '__mouse_v_x__', )

  @mouseVX.SET
  def setMouseVX(self, newValue: type) -> None:
    """Setter-function for mouseVX"""
    setattr(type, '__mouse_v_x__', newValue)

  @mouseVX.DEL
  def delMouseVX(self, *_) -> Never:
    """Illegal deleter-function for mouseVX"""
    from worktoy.waitaminute import ProtectedAttributeError
    attName = 'mouseVX'
    insName = str(self)
    clsName = self.__class__
    raise ProtectedAttributeError(attName, insName, clsName)

  @mouseVX.CREATE
  def _createMouseVX(self, ) -> None:
    """Creator-function for mouseVX"""
    newInstance = type()
    setattr(type, '__mouse_v_x__', newInstance)

  #          || _____________________________________________ ||          #
  #          || mouseVY                                       ||          #
  #          || ¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨ ||          #
  @mouseVY.GET
  def _getMouseVY(self, **kwargs) -> type:
    """Getter function for mouseVY"""
    if self.__mouse_v_y__ is None:
      if kwargs.get('_recursion', False):
        from worktoy.waitaminute import RecursiveCreateGetError
        creator = self._createMouseVY
        argType = type
        argName = '__mouse_v_y__'
        raise RecursiveCreateGetError(creator, argType, argName)
      self._createMouseVY()
      return self._getMouseVY(_recursion=True)
    return getattr(self, '__mouse_v_y__', )

  @mouseVY.SET
  def setMouseVY(self, newValue: type) -> None:
    """Setter-function for mouseVY"""
    setattr(type, '__mouse_v_y__', newValue)

  @mouseVY.DEL
  def delMouseVY(self, *_) -> Never:
    """Illegal deleter-function for mouseVY"""
    from worktoy.waitaminute import ProtectedAttributeError
    attName = 'mouseVY'
    insName = str(self)
    clsName = self.__class__
    raise ProtectedAttributeError(attName, insName, clsName)

  @mouseVY.CREATE
  def _createMouseVY(self, ) -> None:
    """Creator-function for mouseVY"""
    newInstance = type()
    setattr(type, '__mouse_v_y__', newInstance)

  #          || _____________________________________________ ||          #
  #          || mouseAX                                       ||          #
  #          || ¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨ ||          #
  @mouseAX.GET
  def _getMouseAX(self, **kwargs) -> type:
    """Getter function for mouseAX"""
    if self.__mouse_a_x__ is None:
      if kwargs.get('_recursion', False):
        from worktoy.waitaminute import RecursiveCreateGetError
        creator = self._createMouseAX
        argType = type
        argName = '__mouse_a_x__'
        raise RecursiveCreateGetError(creator, argType, argName)
      self._createMouseAX()
      return self._getMouseAX(_recursion=True)
    return getattr(self, '__mouse_a_x__', )

  @mouseAX.SET
  def setMouseAX(self, newValue: type) -> None:
    """Setter-function for mouseAX"""
    setattr(type, '__mouse_a_x__', newValue)

  @mouseAX.DEL
  def delMouseAX(self, *_) -> Never:
    """Illegal deleter-function for mouseAX"""
    from worktoy.waitaminute import ProtectedAttributeError
    attName = 'mouseAX'
    insName = str(self)
    clsName = self.__class__
    raise ProtectedAttributeError(attName, insName, clsName)

  @mouseAX.CREATE
  def _createMouseAX(self, ) -> None:
    """Creator-function for mouseAX"""
    newInstance = type()
    setattr(type, '__mouse_a_x__', newInstance)

  #          || _____________________________________________ ||          #
  #          || mouseAY                                       ||          #
  #          || ¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨ ||          #
  @mouseAY.GET
  def _getMouseAY(self, **kwargs) -> type:
    """Getter function for mouseAY"""
    if self.__mouse_a_y__ is None:
      if kwargs.get('_recursion', False):
        from worktoy.waitaminute import RecursiveCreateGetError
        creator = self._createMouseAY
        argType = type
        argName = '__mouse_a_y__'
        raise RecursiveCreateGetError(creator, argType, argName)
      self._createMouseAY()
      return self._getMouseAY(_recursion=True)
    return getattr(self, '__mouse_a_y__', )

  @mouseAY.SET
  def setMouseAY(self, newValue: type) -> None:
    """Setter-function for mouseAY"""
    setattr(type, '__mouse_a_y__', newValue)

  @mouseAY.DEL
  def delMouseAY(self, *_) -> Never:
    """Illegal deleter-function for mouseAY"""
    from worktoy.waitaminute import ProtectedAttributeError
    attName = 'mouseAY'
    insName = str(self)
    clsName = self.__class__
    raise ProtectedAttributeError(attName, insName, clsName)

  @mouseAY.CREATE
  def _createMouseAY(self, ) -> None:
    """Creator-function for mouseAY"""
    newInstance = type()
    setattr(type, '__mouse_a_y__', newInstance)

  #          || _____________________________________________ ||          #
  #          || mouseState                                    ||          #
  #          || ¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨ ||          #
  @mouseState.GET
  def _getMouseState(self, **kwargs) -> str:
    """Getter function for mouseState"""
    if self.__mouse_state__ is None:
      if kwargs.get('_recursion', False):
        from worktoy.waitaminute import RecursiveCreateGetError
        creator = self._createMouseState
        argType = str
        argName = '__mouse_state__'
        raise RecursiveCreateGetError(creator, argType, argName)
      self._createMouseState()
      return self._getMouseState(_recursion=True)
    return getattr(self, '__mouse_state__', )

  @mouseState.SET
  def setMouseState(self, newValue: str) -> None:
    """Setter-function for mouseState"""
    setattr(str, '__mouse_state__', newValue)

  @mouseState.DEL
  def delMouseState(self, *_) -> Never:
    """Illegal deleter-function for mouseState"""
    from worktoy.waitaminute import ProtectedAttributeError
    attName = 'mouseState'
    insName = str(self)
    clsName = self.__class__
    raise ProtectedAttributeError(attName, insName, clsName)

  @mouseState.CREATE
  def _createMouseState(self, ) -> None:
    """Creator-function for mouseState"""
    newInstance = str()
    setattr(str, '__mouse_state__', newInstance)

  #          || _____________________________________________ ||          #
  #          || mouseRegion                                   ||          #
  #          || ¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨ ||          #
  @mouseRegion.GET
  def _getMouseRegion(self, **kwargs) -> str:
    """Getter function for mouseRegion"""
    if self.__mouse_region__ is None:
      if kwargs.get('_recursion', False):
        from worktoy.waitaminute import RecursiveCreateGetError
        creator = self._createMouseRegion
        argType = str
        argName = '__mouse_region__'
        raise RecursiveCreateGetError(creator, argType, argName)
      self._createMouseRegion()
      return self._getMouseRegion(_recursion=True)
    return getattr(self, '__mouse_region__', )

  @mouseRegion.SET
  def setMouseRegion(self, newValue: str) -> None:
    """Setter-function for mouseRegion"""
    setattr(str, '__mouse_region__', newValue)

  @mouseRegion.DEL
  def delMouseRegion(self, *_) -> Never:
    """Illegal deleter-function for mouseRegion"""
    from worktoy.waitaminute import ProtectedAttributeError
    attName = 'mouseRegion'
    insName = str(self)
    clsName = self.__class__
    raise ProtectedAttributeError(attName, insName, clsName)

  @mouseRegion.CREATE
  def _createMouseRegion(self, ) -> None:
    """Creator-function for mouseRegion"""
    newInstance = str()
    setattr(str, '__mouse_region__', newInstance)

  #          || _____________________________________________ ||          #
  #          || mouseLeft                                     ||          #
  #          || ¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨ ||          #
  @mouseLeft.GET
  def _getMouseLeft(self, **kwargs) -> int:
    """Getter function for mouseLeft"""
    if self.__mouse_left__ is None:
      if kwargs.get('_recursion', False):
        from worktoy.waitaminute import RecursiveCreateGetError
        creator = self._createMouseLeft
        argType = int
        argName = '__mouse_left__'
        raise RecursiveCreateGetError(creator, argType, argName)
      self._createMouseLeft()
      return self._getMouseLeft(_recursion=True)
    return getattr(self, '__mouse_left__', )

  @mouseLeft.SET
  def setMouseLeft(self, newValue: int) -> None:
    """Setter-function for mouseLeft"""
    setattr(int, '__mouse_left__', newValue)

  @mouseLeft.DEL
  def delMouseLeft(self, *_) -> Never:
    """Illegal deleter-function for mouseLeft"""
    from worktoy.waitaminute import ProtectedAttributeError
    attName = 'mouseLeft'
    insName = str(self)
    clsName = self.__class__
    raise ProtectedAttributeError(attName, insName, clsName)

  @mouseLeft.CREATE
  def _createMouseLeft(self, ) -> None:
    """Creator-function for mouseLeft"""
    newInstance = int()
    setattr(int, '__mouse_left__', newInstance)

  #          || _____________________________________________ ||          #
  #          || mouseTop                                      ||          #
  #          || ¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨ ||          #
  @mouseTop.GET
  def _getMouseTop(self, **kwargs) -> int:
    """Getter function for mouseTop"""
    if self.__mouse_top__ is None:
      if kwargs.get('_recursion', False):
        from worktoy.waitaminute import RecursiveCreateGetError
        creator = self._createMouseTop
        argType = int
        argName = '__mouse_top__'
        raise RecursiveCreateGetError(creator, argType, argName)
      self._createMouseTop()
      return self._getMouseTop(_recursion=True)
    return getattr(self, '__mouse_top__', )

  @mouseTop.SET
  def setMouseTop(self, newValue: int) -> None:
    """Setter-function for mouseTop"""
    setattr(int, '__mouse_top__', newValue)

  @mouseTop.DEL
  def delMouseTop(self, *_) -> Never:
    """Illegal deleter-function for mouseTop"""
    from worktoy.waitaminute import ProtectedAttributeError
    attName = 'mouseTop'
    insName = str(self)
    clsName = self.__class__
    raise ProtectedAttributeError(attName, insName, clsName)

  @mouseTop.CREATE
  def _createMouseTop(self, ) -> None:
    """Creator-function for mouseTop"""
    newInstance = int()
    setattr(int, '__mouse_top__', newInstance)

  #          || _____________________________________________ ||          #
  #          || mouseRight                                    ||          #
  #          || ¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨ ||          #
  @mouseRight.GET
  def _getMouseRight(self, **kwargs) -> int:
    """Getter function for mouseRight"""
    if self.__mouse_right__ is None:
      if kwargs.get('_recursion', False):
        from worktoy.waitaminute import RecursiveCreateGetError
        creator = self._createMouseRight
        argType = int
        argName = '__mouse_right__'
        raise RecursiveCreateGetError(creator, argType, argName)
      self._createMouseRight()
      return self._getMouseRight(_recursion=True)
    return getattr(self, '__mouse_right__', )

  @mouseRight.SET
  def setMouseRight(self, newValue: int) -> None:
    """Setter-function for mouseRight"""
    setattr(int, '__mouse_right__', newValue)

  @mouseRight.DEL
  def delMouseRight(self, *_) -> Never:
    """Illegal deleter-function for mouseRight"""
    from worktoy.waitaminute import ProtectedAttributeError
    attName = 'mouseRight'
    insName = str(self)
    clsName = self.__class__
    raise ProtectedAttributeError(attName, insName, clsName)

  @mouseRight.CREATE
  def _createMouseRight(self, ) -> None:
    """Creator-function for mouseRight"""
    newInstance = int()
    setattr(int, '__mouse_right__', newInstance)

  #          || _____________________________________________ ||          #
  #          || mouseBottom                                   ||          #
  #          || ¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨ ||          #
  @mouseBottom.GET
  def _getMouseBottom(self, **kwargs) -> int:
    """Getter function for mouseBottom"""
    if self.__mouse_bottom__ is None:
      if kwargs.get('_recursion', False):
        from worktoy.waitaminute import RecursiveCreateGetError
        creator = self._createMouseBottom
        argType = int
        argName = '__mouse_bottom__'
        raise RecursiveCreateGetError(creator, argType, argName)
      self._createMouseBottom()
      return self._getMouseBottom(_recursion=True)
    return getattr(self, '__mouse_bottom__', )

  @mouseBottom.SET
  def setMouseBottom(self, newValue: int) -> None:
    """Setter-function for mouseBottom"""
    setattr(int, '__mouse_bottom__', newValue)

  @mouseBottom.DEL
  def delMouseBottom(self, *_) -> Never:
    """Illegal deleter-function for mouseBottom"""
    from worktoy.waitaminute import ProtectedAttributeError
    attName = 'mouseBottom'
    insName = str(self)
    clsName = self.__class__
    raise ProtectedAttributeError(attName, insName, clsName)

  @mouseBottom.CREATE
  def _createMouseBottom(self, ) -> None:
    """Creator-function for mouseBottom"""
    newInstance = int()
    setattr(int, '__mouse_bottom__', newInstance)

  def __init__(self, *args, **kwargs) -> None:
    AbstractWidget.__init__(self, *args, **kwargs)
    self.__mouse_point__ = QPointF()
    self.__under_mouse__ = False
    self.__mouse_p_x__ = float
    self.__mouse_p_y__ = float
    self.__mouse_v_x__ = float
    self.__mouse_v_y__ = float
    self.__mouse_a_x__ = float
    self.__mouse_a_y__ = float
    self.__mouse_state__ = NoBtn
    self.__mouse_region__ = QRectF()
    self.__mouse_left__ = 0
    self.__mouse_top__ = 0
    self.__mouse_right__ = 0
    self.__mouse_bottom__ = 0
