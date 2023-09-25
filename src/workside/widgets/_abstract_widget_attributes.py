"""WorkSide - Widgets - AbstractWidgetAttributes
Class containing attributes on the AbstractWidgetClass"""
#  Copyright (c) 2023 Asger Jon Vistisen
#  MIT Licence
from __future__ import annotations

from typing import Never

from PySide6.QtCore import QObject
from PySide6.QtGui import QPaintEvent
from PySide6.QtWidgets import QWidget
from icecream import ic

from worktoy.descriptors import Attribute
from worktoy.worktoyclass import WorkToyClass


class AbstractWidgetAttributes(QWidget, WorkToyClass):
  """ This class provides independent geometric attributes of the widgets
in the WorkSide framework. The outer left and outer top values define
the top left corner of the widget. The width and height of the inner
rectangle define the size required by the widget to show its content.
The remaining values refer to the box model. These combined with the
size defined on the inner rectangle and position on the outer rectangle
define exactly the geometric properties of the widget. These attributes
have getters and setters, but not deleter functions. """
  outerLeft = Attribute(1)
  outerTop = Attribute(1)
  innerWidth = Attribute(1)
  innerHeight = Attribute(1)
  paddingLeft = Attribute(1)
  paddingTop = Attribute(1)
  paddingRight = Attribute(1)
  paddingBottom = Attribute(1)
  borderLeft = Attribute(1)
  borderTop = Attribute(1)
  borderRight = Attribute(1)
  borderBottom = Attribute(1)
  marginLeft = Attribute(1)
  marginTop = Attribute(1)
  marginRight = Attribute(1)
  marginBottom = Attribute(1)

  # | _________________________________________________________________ | #
  # | <<<<<<<<<<<<<<<<<<<<<<<<<<  outerLeft  >>>>>>>>>>>>>>>>>>>>>>>>>> | #
  # | ¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨ | #
  @outerLeft.GET
  def getOuterLeft(self, ) -> int:
    """Getter-function for outerLeft"""
    return self.__outer_left__

  @outerLeft.SET
  def setOuterLeft(self, newValue: int) -> None:
    """Setter-function for outerLeft"""
    self.__outer_left__ = newValue

  @outerLeft.DEL
  def delOuterLeft(self, *_) -> Never:
    """Illegal deleter-function for outerLeft"""
    from worktoy.waitaminute import ProtectedAttributeError
    attName = 'outerLeft'
    insName = str(self)
    clsName = self.__class__
    raise ProtectedAttributeError(attName, insName, clsName)

  # | _________________________________________________________________ | #
  # | <<<<<<<<<<<<<<<<<<<<<<<<<<<  outerTop  >>>>>>>>>>>>>>>>>>>>>>>>>> | #
  # | ¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨ | #
  @outerTop.GET
  def getOuterTop(self, ) -> int:
    """Getter-function for outerTop"""
    return self.__outer_top__

  @outerTop.SET
  def setOuterTop(self, newValue: int) -> None:
    """Setter-function for outerTop"""
    self.__outer_top__ = newValue

  @outerTop.DEL
  def delOuterTop(self, *_) -> Never:
    """Illegal deleter-function for outerTop"""
    from worktoy.waitaminute import ProtectedAttributeError
    attName = 'outerTop'
    insName = str(self)
    clsName = self.__class__
    raise ProtectedAttributeError(attName, insName, clsName)

  # | _________________________________________________________________ | #
  # | <<<<<<<<<<<<<<<<<<<<<<<<<<  innerWidth  >>>>>>>>>>>>>>>>>>>>>>>>> | #
  # | ¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨ | #
  @innerWidth.GET
  def getInnerWidth(self, ) -> int:
    """Getter-function for innerWidth"""
    return self.__inner_width__

  @innerWidth.SET
  def setInnerWidth(self, newValue: int) -> None:
    """Setter-function for innerWidth"""
    self.__inner_width__ = newValue

  @innerWidth.DEL
  def delInnerWidth(self, *_) -> Never:
    """Illegal deleter-function for innerWidth"""
    from worktoy.waitaminute import ProtectedAttributeError
    attName = 'innerWidth'
    insName = str(self)
    clsName = self.__class__
    raise ProtectedAttributeError(attName, insName, clsName)

  # | _________________________________________________________________ | #
  # | <<<<<<<<<<<<<<<<<<<<<<<<<  innerHeight  >>>>>>>>>>>>>>>>>>>>>>>>> | #
  # | ¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨ | #
  @innerHeight.GET
  def getInnerHeight(self, ) -> int:
    """Getter-function for innerHeight"""
    return self.__inner_height__

  @innerHeight.SET
  def setInnerHeight(self, newValue: int) -> None:
    """Setter-function for innerHeight"""
    self.__inner_height__ = newValue

  @innerHeight.DEL
  def delInnerHeight(self, *_) -> Never:
    """Illegal deleter-function for innerHeight"""
    from worktoy.waitaminute import ProtectedAttributeError
    attName = 'innerHeight'
    insName = str(self)
    clsName = self.__class__
    raise ProtectedAttributeError(attName, insName, clsName)

  # | _________________________________________________________________ | #
  # | <<<<<<<<<<<<<<<<<<<<<<<<<  paddingLeft  >>>>>>>>>>>>>>>>>>>>>>>>> | #
  # | ¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨ | #
  @paddingLeft.GET
  def getPaddingLeft(self, ) -> int:
    """Getter-function for paddingLeft"""
    return self.__padding_left__

  @paddingLeft.SET
  def setPaddingLeft(self, newValue: int) -> None:
    """Setter-function for paddingLeft"""
    self.__padding_left__ = newValue

  @paddingLeft.DEL
  def delPaddingLeft(self, *_) -> Never:
    """Illegal deleter-function for paddingLeft"""
    from worktoy.waitaminute import ProtectedAttributeError
    attName = 'paddingLeft'
    insName = str(self)
    clsName = self.__class__
    raise ProtectedAttributeError(attName, insName, clsName)

  # | _________________________________________________________________ | #
  # | <<<<<<<<<<<<<<<<<<<<<<<<<<  paddingTop  >>>>>>>>>>>>>>>>>>>>>>>>> | #
  # | ¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨ | #
  @paddingTop.GET
  def getPaddingTop(self, ) -> int:
    """Getter-function for paddingTop"""
    return self.__padding_top__

  @paddingTop.SET
  def setPaddingTop(self, newValue: int) -> None:
    """Setter-function for paddingTop"""
    self.__padding_top__ = newValue

  @paddingTop.DEL
  def delPaddingTop(self, *_) -> Never:
    """Illegal deleter-function for paddingTop"""
    from worktoy.waitaminute import ProtectedAttributeError
    attName = 'paddingTop'
    insName = str(self)
    clsName = self.__class__
    raise ProtectedAttributeError(attName, insName, clsName)

  # | _________________________________________________________________ | #
  # | <<<<<<<<<<<<<<<<<<<<<<<<<  paddingRight  >>>>>>>>>>>>>>>>>>>>>>>> | #
  # | ¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨ | #
  @paddingRight.GET
  def getPaddingRight(self, ) -> int:
    """Getter-function for paddingRight"""
    return self.__padding_right__

  @paddingRight.SET
  def setPaddingRight(self, newValue: int) -> None:
    """Setter-function for paddingRight"""
    self.__padding_right__ = newValue

  @paddingRight.DEL
  def delPaddingRight(self, *_) -> Never:
    """Illegal deleter-function for paddingRight"""
    from worktoy.waitaminute import ProtectedAttributeError
    attName = 'paddingRight'
    insName = str(self)
    clsName = self.__class__
    raise ProtectedAttributeError(attName, insName, clsName)

  # | _________________________________________________________________ | #
  # | <<<<<<<<<<<<<<<<<<<<<<<<  paddingBottom  >>>>>>>>>>>>>>>>>>>>>>>> | #
  # | ¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨ | #
  @paddingBottom.GET
  def getPaddingBottom(self, ) -> int:
    """Getter-function for paddingBottom"""
    return self.__padding_bottom__

  @paddingBottom.SET
  def setPaddingBottom(self, newValue: int) -> None:
    """Setter-function for paddingBottom"""
    self.__padding_bottom__ = newValue

  @paddingBottom.DEL
  def delPaddingBottom(self, *_) -> Never:
    """Illegal deleter-function for paddingBottom"""
    from worktoy.waitaminute import ProtectedAttributeError
    attName = 'paddingBottom'
    insName = str(self)
    clsName = self.__class__
    raise ProtectedAttributeError(attName, insName, clsName)

  # | _________________________________________________________________ | #
  # | <<<<<<<<<<<<<<<<<<<<<<<<<<  borderLeft  >>>>>>>>>>>>>>>>>>>>>>>>> | #
  # | ¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨ | #
  @borderLeft.GET
  def getBorderLeft(self, ) -> int:
    """Getter-function for borderLeft"""
    return self.__border_left__

  @borderLeft.SET
  def setBorderLeft(self, newValue: int) -> None:
    """Setter-function for borderLeft"""
    self.__border_left__ = newValue

  @borderLeft.DEL
  def delBorderLeft(self, *_) -> Never:
    """Illegal deleter-function for borderLeft"""
    from worktoy.waitaminute import ProtectedAttributeError
    attName = 'borderLeft'
    insName = str(self)
    clsName = self.__class__
    raise ProtectedAttributeError(attName, insName, clsName)

  # | _________________________________________________________________ | #
  # | <<<<<<<<<<<<<<<<<<<<<<<<<<  borderTop  >>>>>>>>>>>>>>>>>>>>>>>>>> | #
  # | ¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨ | #
  @borderTop.GET
  def getBorderTop(self, ) -> int:
    """Getter-function for borderTop"""
    return self.__border_top__

  @borderTop.SET
  def setBorderTop(self, newValue: int) -> None:
    """Setter-function for borderTop"""
    self.__border_top__ = newValue

  @borderTop.DEL
  def delBorderTop(self, *_) -> Never:
    """Illegal deleter-function for borderTop"""
    from worktoy.waitaminute import ProtectedAttributeError
    attName = 'borderTop'
    insName = str(self)
    clsName = self.__class__
    raise ProtectedAttributeError(attName, insName, clsName)

  # | _________________________________________________________________ | #
  # | <<<<<<<<<<<<<<<<<<<<<<<<<  borderRight  >>>>>>>>>>>>>>>>>>>>>>>>> | #
  # | ¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨ | #
  @borderRight.GET
  def getBorderRight(self, ) -> int:
    """Getter-function for borderRight"""
    return self.__border_right__

  @borderRight.SET
  def setBorderRight(self, newValue: int) -> None:
    """Setter-function for borderRight"""
    self.__border_right__ = newValue

  @borderRight.DEL
  def delBorderRight(self, *_) -> Never:
    """Illegal deleter-function for borderRight"""
    from worktoy.waitaminute import ProtectedAttributeError
    attName = 'borderRight'
    insName = str(self)
    clsName = self.__class__
    raise ProtectedAttributeError(attName, insName, clsName)

  # | _________________________________________________________________ | #
  # | <<<<<<<<<<<<<<<<<<<<<<<<<  borderBottom  >>>>>>>>>>>>>>>>>>>>>>>> | #
  # | ¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨ | #
  @borderBottom.GET
  def getBorderBottom(self, ) -> int:
    """Getter-function for borderBottom"""
    return self.__border_bottom__

  @borderBottom.SET
  def setBorderBottom(self, newValue: int) -> None:
    """Setter-function for borderBottom"""
    self.__border_bottom__ = newValue

  @borderBottom.DEL
  def delBorderBottom(self, *_) -> Never:
    """Illegal deleter-function for borderBottom"""
    from worktoy.waitaminute import ProtectedAttributeError
    attName = 'borderBottom'
    insName = str(self)
    clsName = self.__class__
    raise ProtectedAttributeError(attName, insName, clsName)

  # | _________________________________________________________________ | #
  # | <<<<<<<<<<<<<<<<<<<<<<<<<<  marginLeft  >>>>>>>>>>>>>>>>>>>>>>>>> | #
  # | ¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨ | #
  @marginLeft.GET
  def getMarginLeft(self, ) -> int:
    """Getter-function for marginLeft"""
    return self.__margin_left__

  @marginLeft.SET
  def setMarginLeft(self, newValue: int) -> None:
    """Setter-function for marginLeft"""
    self.__margin_left__ = newValue

  @marginLeft.DEL
  def delMarginLeft(self, *_) -> Never:
    """Illegal deleter-function for marginLeft"""
    from worktoy.waitaminute import ProtectedAttributeError
    attName = 'marginLeft'
    insName = str(self)
    clsName = self.__class__
    raise ProtectedAttributeError(attName, insName, clsName)

  # | _________________________________________________________________ | #
  # | <<<<<<<<<<<<<<<<<<<<<<<<<<  marginTop  >>>>>>>>>>>>>>>>>>>>>>>>>> | #
  # | ¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨ | #
  @marginTop.GET
  def getMarginTop(self, ) -> int:
    """Getter-function for marginTop"""
    return self.__margin_top__

  @marginTop.SET
  def setMarginTop(self, newValue: int) -> None:
    """Setter-function for marginTop"""
    self.__margin_top__ = newValue

  @marginTop.DEL
  def delMarginTop(self, *_) -> Never:
    """Illegal deleter-function for marginTop"""
    from worktoy.waitaminute import ProtectedAttributeError
    attName = 'marginTop'
    insName = str(self)
    clsName = self.__class__
    raise ProtectedAttributeError(attName, insName, clsName)

  # | _________________________________________________________________ | #
  # | <<<<<<<<<<<<<<<<<<<<<<<<<  marginRight  >>>>>>>>>>>>>>>>>>>>>>>>> | #
  # | ¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨ | #
  @marginRight.GET
  def getMarginRight(self, ) -> int:
    """Getter-function for marginRight"""
    return self.__margin_right__

  @marginRight.SET
  def setMarginRight(self, newValue: int) -> None:
    """Setter-function for marginRight"""
    self.__margin_right__ = newValue

  @marginRight.DEL
  def delMarginRight(self, *_) -> Never:
    """Illegal deleter-function for marginRight"""
    from worktoy.waitaminute import ProtectedAttributeError
    attName = 'marginRight'
    insName = str(self)
    clsName = self.__class__
    raise ProtectedAttributeError(attName, insName, clsName)

  # | _________________________________________________________________ | #
  # | <<<<<<<<<<<<<<<<<<<<<<<<<  marginBottom  >>>>>>>>>>>>>>>>>>>>>>>> | #
  # | ¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨ | #
  @marginBottom.GET
  def getMarginBottom(self, ) -> int:
    """Getter-function for marginBottom"""
    return self.__margin_bottom__

  @marginBottom.SET
  def setMarginBottom(self, newValue: int) -> None:
    """Setter-function for marginBottom"""
    self.__margin_bottom__ = newValue

  @marginBottom.DEL
  def delMarginBottom(self, *_) -> Never:
    """Illegal deleter-function for marginBottom"""
    from worktoy.waitaminute import ProtectedAttributeError
    attName = 'marginBottom'
    insName = str(self)
    clsName = self.__class__
    raise ProtectedAttributeError(attName, insName, clsName)

  # | _________________________________________________________________ | #
  def __init__(self, *args, **kwargs) -> None:
    WorkToyClass.__init__(self, *args, **kwargs)
    self.__outer_left__ = 0
    self.__outer_top__ = 0
    self.__inner_width__ = 0
    self.__inner_height__ = 0
    self.__padding_left__ = 0
    self.__padding_top__ = 0
    self.__padding_right__ = 0
    self.__padding_bottom__ = 0
    self.__border_left__ = 0
    self.__border_top__ = 0
    self.__border_right__ = 0
    self.__border_bottom__ = 0
    self.__margin_left__ = 0
    self.__margin_top__ = 0
    self.__margin_right__ = 0
    self.__margin_bottom__ = 0
    parent = self.maybeType(QWidget, *args)
    QWidget.__init__(self, parent)
    self.setMouseTracking(True)
    ic(isinstance(self, QObject))

  def paintEvent(self, event: QPaintEvent) -> None:
    """Adds state dependent fill to the inner rectangle."""
    QWidget.paintEvent(self, event)
