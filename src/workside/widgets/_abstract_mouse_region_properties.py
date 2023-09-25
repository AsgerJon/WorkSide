"""WorkSide - Core - AbstractMouseRegionProperties
Code writing assistant"""
#  Copyright (c) 2023 Asger Jon Vistisen
#  MIT Licence
from __future__ import annotations

from typing import Never

from PySide6.QtCore import QPointF, QRectF
from PySide6.QtGui import QPaintEvent
from icecream import ic
from worktoy.descriptors import Attribute

from workside.settings import Mouse, NoBtn
from workside.widgets import AbstractButtonTimer

ic.configureOutput(includeContext=True)


class AbstractMouseRegionProperties(AbstractButtonTimer):
  """Defines the area of the widget considered by the mouse"""
  mousePoint = Attribute()
  underMouse = Attribute()
  mousePX = Attribute()
  mousePY = Attribute()
  mouseVX = Attribute()
  mouseVY = Attribute()
  mouseAX = Attribute()
  mouseAY = Attribute()
  mouseState = Attribute()
  mouseRegion = Attribute()
  mouseLeft = Attribute()
  mouseTop = Attribute()
  mouseRight = Attribute()
  mouseBottom = Attribute()

  # | _________________________________________________________________ | #
  # | <<<<<<<<<<<<<<<<<<<<<<<<<<  mousePoint  >>>>>>>>>>>>>>>>>>>>>>>>> | #
  # | ¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨ | #
  @mousePoint.GET
  def getMousePoint(self, ) -> QPointF():
    """Getter-function for mousePoint"""
    return self.__mouse_point__

  @mousePoint.SET
  def setMousePoint(self, newValue: QPointF()) -> None:
    """Setter-function for mousePoint"""
    self.__mouse_point__ = newValue

  @mousePoint.DEL
  def delMousePoint(self, *_) -> Never:
    """Illegal deleter-function for mousePoint"""
    from worktoy.waitaminute import ProtectedAttributeError
    attName = 'mousePoint'
    insName = str(self)
    clsName = self.__class__
    raise ProtectedAttributeError(attName, insName, clsName)

  # | _________________________________________________________________ | #
  # | <<<<<<<<<<<<<<<<<<<<<<<<<<  underMouse  >>>>>>>>>>>>>>>>>>>>>>>>> | #
  # | ¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨ | #
  @underMouse.GET
  def getUnderMouse(self, ) -> bool:
    """Getter-function for underMouse"""
    return self.__under_mouse__

  @underMouse.SET
  def setUnderMouse(self, newValue: bool) -> None:
    """Setter-function for underMouse"""
    self.__under_mouse__ = newValue

  @underMouse.DEL
  def delUnderMouse(self, *_) -> Never:
    """Illegal deleter-function for underMouse"""
    from worktoy.waitaminute import ProtectedAttributeError
    attName = 'underMouse'
    insName = str(self)
    clsName = self.__class__
    raise ProtectedAttributeError(attName, insName, clsName)

  # | _________________________________________________________________ | #
  # | <<<<<<<<<<<<<<<<<<<<<<<<<<<  mousePX  >>>>>>>>>>>>>>>>>>>>>>>>>>> | #
  # | ¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨ | #
  @mousePX.GET
  def getMousePX(self, ) -> float:
    """Getter-function for mousePX"""
    return self.__mouse_p_x__

  @mousePX.SET
  def setMousePX(self, newValue: float) -> None:
    """Setter-function for mousePX"""
    self.__mouse_p_x__ = newValue

  @mousePX.DEL
  def delMousePX(self, *_) -> Never:
    """Illegal deleter-function for mousePX"""
    from worktoy.waitaminute import ProtectedAttributeError
    attName = 'mousePX'
    insName = str(self)
    clsName = self.__class__
    raise ProtectedAttributeError(attName, insName, clsName)

  # | _________________________________________________________________ | #
  # | <<<<<<<<<<<<<<<<<<<<<<<<<<<  mousePY  >>>>>>>>>>>>>>>>>>>>>>>>>>> | #
  # | ¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨ | #
  @mousePY.GET
  def getMousePY(self, ) -> float:
    """Getter-function for mousePY"""
    return self.__mouse_p_y__

  @mousePY.SET
  def setMousePY(self, newValue: float) -> None:
    """Setter-function for mousePY"""
    self.__mouse_p_y__ = newValue

  @mousePY.DEL
  def delMousePY(self, *_) -> Never:
    """Illegal deleter-function for mousePY"""
    from worktoy.waitaminute import ProtectedAttributeError
    attName = 'mousePY'
    insName = str(self)
    clsName = self.__class__
    raise ProtectedAttributeError(attName, insName, clsName)

  # | _________________________________________________________________ | #
  # | <<<<<<<<<<<<<<<<<<<<<<<<<<<  mouseVX  >>>>>>>>>>>>>>>>>>>>>>>>>>> | #
  # | ¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨ | #
  @mouseVX.GET
  def getMouseVX(self, ) -> float:
    """Getter-function for mouseVX"""
    return self.__mouse_v_x__

  @mouseVX.SET
  def setMouseVX(self, newValue: float) -> None:
    """Setter-function for mouseVX"""
    self.__mouse_v_x__ = newValue

  @mouseVX.DEL
  def delMouseVX(self, *_) -> Never:
    """Illegal deleter-function for mouseVX"""
    from worktoy.waitaminute import ProtectedAttributeError
    attName = 'mouseVX'
    insName = str(self)
    clsName = self.__class__
    raise ProtectedAttributeError(attName, insName, clsName)

  # | _________________________________________________________________ | #
  # | <<<<<<<<<<<<<<<<<<<<<<<<<<<  mouseVY  >>>>>>>>>>>>>>>>>>>>>>>>>>> | #
  # | ¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨ | #
  @mouseVY.GET
  def getMouseVY(self, ) -> float:
    """Getter-function for mouseVY"""
    return self.__mouse_v_y__

  @mouseVY.SET
  def setMouseVY(self, newValue: float) -> None:
    """Setter-function for mouseVY"""
    self.__mouse_v_y__ = newValue

  @mouseVY.DEL
  def delMouseVY(self, *_) -> Never:
    """Illegal deleter-function for mouseVY"""
    from worktoy.waitaminute import ProtectedAttributeError
    attName = 'mouseVY'
    insName = str(self)
    clsName = self.__class__
    raise ProtectedAttributeError(attName, insName, clsName)

  # | _________________________________________________________________ | #
  # | <<<<<<<<<<<<<<<<<<<<<<<<<<<  mouseAX  >>>>>>>>>>>>>>>>>>>>>>>>>>> | #
  # | ¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨ | #
  @mouseAX.GET
  def getMouseAX(self, ) -> float:
    """Getter-function for mouseAX"""
    return self.__mouse_a_x__

  @mouseAX.SET
  def setMouseAX(self, newValue: float) -> None:
    """Setter-function for mouseAX"""
    self.__mouse_a_x__ = newValue

  @mouseAX.DEL
  def delMouseAX(self, *_) -> Never:
    """Illegal deleter-function for mouseAX"""
    from worktoy.waitaminute import ProtectedAttributeError
    attName = 'mouseAX'
    insName = str(self)
    clsName = self.__class__
    raise ProtectedAttributeError(attName, insName, clsName)

  # | _________________________________________________________________ | #
  # | <<<<<<<<<<<<<<<<<<<<<<<<<<<  mouseAY  >>>>>>>>>>>>>>>>>>>>>>>>>>> | #
  # | ¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨ | #
  @mouseAY.GET
  def getMouseAY(self, ) -> float:
    """Getter-function for mouseAY"""
    return self.__mouse_a_y__

  @mouseAY.SET
  def setMouseAY(self, newValue: float) -> None:
    """Setter-function for mouseAY"""
    self.__mouse_a_y__ = newValue

  @mouseAY.DEL
  def delMouseAY(self, *_) -> Never:
    """Illegal deleter-function for mouseAY"""
    from worktoy.waitaminute import ProtectedAttributeError
    attName = 'mouseAY'
    insName = str(self)
    clsName = self.__class__
    raise ProtectedAttributeError(attName, insName, clsName)

  # | _________________________________________________________________ | #
  # | <<<<<<<<<<<<<<<<<<<<<<<<<<  mouseState  >>>>>>>>>>>>>>>>>>>>>>>>> | #
  # | ¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨ | #
  @mouseState.GET
  def getMouseState(self, ) -> Mouse:
    """Getter-function for mouseState"""
    return self.__mouse_state__

  @mouseState.SET
  def setMouseState(self, newValue: Mouse) -> None:
    """Setter-function for mouseState"""
    self.__mouse_state__ = newValue

  @mouseState.DEL
  def delMouseState(self, *_) -> Never:
    """Illegal deleter-function for mouseState"""
    from worktoy.waitaminute import ProtectedAttributeError
    attName = 'mouseState'
    insName = str(self)
    clsName = self.__class__
    raise ProtectedAttributeError(attName, insName, clsName)

  # | _________________________________________________________________ | #
  # | <<<<<<<<<<<<<<<<<<<<<<<<<  mouseRegion  >>>>>>>>>>>>>>>>>>>>>>>>> | #
  # | ¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨ | #
  @mouseRegion.GET
  def getMouseRegion(self, ) -> QRectF:
    """Getter-function for mouseRegion"""
    return self.__mouse_region__

  @mouseRegion.SET
  def setMouseRegion(self, newValue: QRectF) -> None:
    """Setter-function for mouseRegion"""
    self.__mouse_region__ = newValue

  @mouseRegion.DEL
  def delMouseRegion(self, *_) -> Never:
    """Illegal deleter-function for mouseRegion"""
    from worktoy.waitaminute import ProtectedAttributeError
    attName = 'mouseRegion'
    insName = str(self)
    clsName = self.__class__
    raise ProtectedAttributeError(attName, insName, clsName)

  # | _________________________________________________________________ | #
  # | <<<<<<<<<<<<<<<<<<<<<<<<<<  mouseLeft  >>>>>>>>>>>>>>>>>>>>>>>>>> | #
  # | ¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨ | #
  @mouseLeft.GET
  def getMouseLeft(self, ) -> float:
    """Getter-function for mouseLeft"""
    return self.__mouse_left__

  @mouseLeft.SET
  def setMouseLeft(self, newValue: float) -> None:
    """Setter-function for mouseLeft"""
    self.__mouse_left__ = newValue

  @mouseLeft.DEL
  def delMouseLeft(self, *_) -> Never:
    """Illegal deleter-function for mouseLeft"""
    from worktoy.waitaminute import ProtectedAttributeError
    attName = 'mouseLeft'
    insName = str(self)
    clsName = self.__class__
    raise ProtectedAttributeError(attName, insName, clsName)

  # | _________________________________________________________________ | #
  # | <<<<<<<<<<<<<<<<<<<<<<<<<<<  mouseTop  >>>>>>>>>>>>>>>>>>>>>>>>>> | #
  # | ¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨ | #
  @mouseTop.GET
  def getMouseTop(self, ) -> float:
    """Getter-function for mouseTop"""
    return self.__mouse_top__

  @mouseTop.SET
  def setMouseTop(self, newValue: float) -> None:
    """Setter-function for mouseTop"""
    self.__mouse_top__ = newValue

  @mouseTop.DEL
  def delMouseTop(self, *_) -> Never:
    """Illegal deleter-function for mouseTop"""
    from worktoy.waitaminute import ProtectedAttributeError
    attName = 'mouseTop'
    insName = str(self)
    clsName = self.__class__
    raise ProtectedAttributeError(attName, insName, clsName)

  # | _________________________________________________________________ | #
  # | <<<<<<<<<<<<<<<<<<<<<<<<<<  mouseRight  >>>>>>>>>>>>>>>>>>>>>>>>> | #
  # | ¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨ | #
  @mouseRight.GET
  def getMouseRight(self, ) -> float:
    """Getter-function for mouseRight"""
    return self.__mouse_right__

  @mouseRight.SET
  def setMouseRight(self, newValue: float) -> None:
    """Setter-function for mouseRight"""
    self.__mouse_right__ = newValue

  @mouseRight.DEL
  def delMouseRight(self, *_) -> Never:
    """Illegal deleter-function for mouseRight"""
    from worktoy.waitaminute import ProtectedAttributeError
    attName = 'mouseRight'
    insName = str(self)
    clsName = self.__class__
    raise ProtectedAttributeError(attName, insName, clsName)

  # | _________________________________________________________________ | #
  # | <<<<<<<<<<<<<<<<<<<<<<<<<  mouseBottom  >>>>>>>>>>>>>>>>>>>>>>>>> | #
  # | ¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨ | #
  @mouseBottom.GET
  def getMouseBottom(self, ) -> float:
    """Getter-function for mouseBottom"""
    return self.__mouse_bottom__

  @mouseBottom.SET
  def setMouseBottom(self, newValue: float) -> None:
    """Setter-function for mouseBottom"""
    self.__mouse_bottom__ = newValue

  @mouseBottom.DEL
  def delMouseBottom(self, *_) -> Never:
    """Illegal deleter-function for mouseBottom"""
    from worktoy.waitaminute import ProtectedAttributeError
    attName = 'mouseBottom'
    insName = str(self)
    clsName = self.__class__
    raise ProtectedAttributeError(attName, insName, clsName)

  # | _________________________________________________________________ | #
  def __init__(self, *args, **kwargs) -> None:
    AbstractButtonTimer.__init__(self, *args, **kwargs)
    self.setMouseTracking(True)
    self.__mouse_point__ = QPointF(0, 0)
    self.__under_mouse__ = False
    self.__mouse_p_x__ = 0.0
    self.__mouse_p_y__ = 0.0
    self.__mouse_v_x__ = 0.0
    self.__mouse_v_y__ = 0.0
    self.__mouse_a_x__ = 0.0
    self.__mouse_a_y__ = 0.0
    self.__mouse_state__ = NoBtn
    self.__mouse_region__ = QRectF()
    self.__mouse_left__ = 0
    self.__mouse_top__ = 0
    self.__mouse_right__ = 0
    self.__mouse_bottom__ = 0
    ic()
