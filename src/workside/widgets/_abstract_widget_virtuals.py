"""WorkSide - Widgets - AbstractWidgetVirtuals
Class containing virtual attributes on the AbstractWidgetClass.

A virtual attribute refers to a function value on more than one 'real'
attribute.
"""
#  MIT Licence
#  Copyright (c) 2023 Asger Jon Vistisen
from __future__ import annotations

from typing import Never

from PySide6.QtCore import QPoint, QSize, QRect
from workside.widgets import AbstractWidgetAttributes
from worktoy.descriptors import Attribute


class AbstractWidgetVirtuals(AbstractWidgetAttributes):
  """ Class containing virtual attributes on the AbstractWidgetClass. A
virtual attribute refers to a function value on more than one 'real'
attribute. """
  outerRight = Attribute()
  outerBottom = Attribute()
  outerWidth = Attribute()
  outerHeight = Attribute()
  outerTopLeft = Attribute()
  outerTopRight = Attribute()
  outerBottomRight = Attribute()
  outerBottomLeft = Attribute()
  outerArea = Attribute()
  outerSize = Attribute()
  outerRect = Attribute()
  borderedLeft = Attribute()
  borderedTop = Attribute()
  borderedRight = Attribute()
  borderedBottom = Attribute()
  borderedWidth = Attribute()
  borderedHeight = Attribute()
  borderedArea = Attribute()
  borderedSize = Attribute()
  borderedRect = Attribute()
  borderedTopLeft = Attribute()
  borderedTopRight = Attribute()
  borderedBottomRight = Attribute()
  borderedBottomLeft = Attribute()
  paddedLeft = Attribute()
  paddedTop = Attribute()
  paddedRight = Attribute()
  paddedBottom = Attribute()
  paddedWidth = Attribute()
  paddedHeight = Attribute()
  paddedArea = Attribute()
  paddedSize = Attribute()
  paddedRect = Attribute()
  paddedTopLeft = Attribute()
  paddedTopRight = Attribute()
  paddedBottomRight = Attribute()
  paddedBottomLeft = Attribute()
  innerLeft = Attribute()
  innerTop = Attribute()
  innerRight = Attribute()
  innerBottom = Attribute()
  innerArea = Attribute()
  innerTopLeft = Attribute()
  innerTopRight = Attribute()
  innerBottomRight = Attribute()
  innerBottomLeft = Attribute()
  innerSize = Attribute()
  innerRect = Attribute()

  # | _________________________________________________________________ | #
  # | <<<<<<<<<<<<<<<<<<<<<<<<<<  outerRight  >>>>>>>>>>>>>>>>>>>>>>>>> | #
  # | ¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨ | #
  @outerRight.GET
  def getOuterRight(self, ) -> int:
    """Getter-function for outerRight"""
    return self.outerLeft + self.outerWidth

  @outerRight.SET
  def setOuterRight(self, *_) -> Never:
    """Illegal setter-function for outerRight"""
    from worktoy.waitaminute import ReadOnlyException
    attName = 'outerRight'
    insName = str(self)
    clsName = self.__class__
    raise ReadOnlyException(attName, insName, clsName)

  @outerRight.DEL
  def delOuterRight(self, *_) -> Never:
    """Illegal deleter-function for outerRight"""
    from worktoy.waitaminute import ProtectedAttributeError
    attName = 'outerRight'
    insName = str(self)
    clsName = self.__class__
    raise ProtectedAttributeError(attName, insName, clsName)

  # | _________________________________________________________________ | #
  # | <<<<<<<<<<<<<<<<<<<<<<<<<  outerBottom  >>>>>>>>>>>>>>>>>>>>>>>>> | #
  # | ¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨ | #
  @outerBottom.GET
  def getOuterBottom(self, ) -> int:
    """Getter-function for outerBottom"""
    return self.outerTop + self.outerHeight

  @outerBottom.SET
  def setOuterBottom(self, *_) -> Never:
    """Illegal setter-function for outerBottom"""
    from worktoy.waitaminute import ReadOnlyException
    attName = 'outerBottom'
    insName = str(self)
    clsName = self.__class__
    raise ReadOnlyException(attName, insName, clsName)

  @outerBottom.DEL
  def delOuterBottom(self, *_) -> Never:
    """Illegal deleter-function for outerBottom"""
    from worktoy.waitaminute import ProtectedAttributeError
    attName = 'outerBottom'
    insName = str(self)
    clsName = self.__class__
    raise ProtectedAttributeError(attName, insName, clsName)

  # | _________________________________________________________________ | #
  # | <<<<<<<<<<<<<<<<<<<<<<<<<<  outerWidth  >>>>>>>>>>>>>>>>>>>>>>>>> | #
  # | ¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨ | #
  @outerWidth.GET
  def getOuterWidth(self, ) -> int:
    """Getter-function for outerWidth"""
    return self.borderedWidth + self.marginLeft + self.marginRight

  @outerWidth.SET
  def setOuterWidth(self, *_) -> Never:
    """Illegal setter-function for outerWidth"""
    from worktoy.waitaminute import ReadOnlyException
    attName = 'outerWidth'
    insName = str(self)
    clsName = self.__class__
    raise ReadOnlyException(attName, insName, clsName)

  @outerWidth.DEL
  def delOuterWidth(self, *_) -> Never:
    """Illegal deleter-function for outerWidth"""
    from worktoy.waitaminute import ProtectedAttributeError
    attName = 'outerWidth'
    insName = str(self)
    clsName = self.__class__
    raise ProtectedAttributeError(attName, insName, clsName)

  # | _________________________________________________________________ | #
  # | <<<<<<<<<<<<<<<<<<<<<<<<<  outerHeight  >>>>>>>>>>>>>>>>>>>>>>>>> | #
  # | ¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨ | #
  @outerHeight.GET
  def getOuterHeight(self, ) -> int:
    """Getter-function for outerHeight"""
    return self.borderedHeight + self.marginTop + self.marginBottom

  @outerHeight.SET
  def setOuterHeight(self, *_) -> Never:
    """Illegal setter-function for outerHeight"""
    from worktoy.waitaminute import ReadOnlyException
    attName = 'outerHeight'
    insName = str(self)
    clsName = self.__class__
    raise ReadOnlyException(attName, insName, clsName)

  @outerHeight.DEL
  def delOuterHeight(self, *_) -> Never:
    """Illegal deleter-function for outerHeight"""
    from worktoy.waitaminute import ProtectedAttributeError
    attName = 'outerHeight'
    insName = str(self)
    clsName = self.__class__
    raise ProtectedAttributeError(attName, insName, clsName)

  # | _________________________________________________________________ | #
  # | <<<<<<<<<<<<<<<<<<<<<<<<<  outerTopLeft  >>>>>>>>>>>>>>>>>>>>>>>> | #
  # | ¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨ | #
  @outerTopLeft.GET
  def getOuterTopLeft(self, ) -> QPoint:
    """Getter-function for outerTopLeft"""
    return QPoint(self.outerLeft, self.outerTop)

  @outerTopLeft.SET
  def setOuterTopLeft(self, *_) -> Never:
    """Illegal setter-function for outerTopLeft"""
    from worktoy.waitaminute import ReadOnlyException
    attName = 'outerTopLeft'
    insName = str(self)
    clsName = self.__class__
    raise ReadOnlyException(attName, insName, clsName)

  @outerTopLeft.DEL
  def delOuterTopLeft(self, *_) -> Never:
    """Illegal deleter-function for outerTopLeft"""
    from worktoy.waitaminute import ProtectedAttributeError
    attName = 'outerTopLeft'
    insName = str(self)
    clsName = self.__class__
    raise ProtectedAttributeError(attName, insName, clsName)

  # | _________________________________________________________________ | #
  # | <<<<<<<<<<<<<<<<<<<<<<<<  outerTopRight  >>>>>>>>>>>>>>>>>>>>>>>> | #
  # | ¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨ | #
  @outerTopRight.GET
  def getOuterTopRight(self, ) -> QPoint:
    """Getter-function for outerTopRight"""
    return QPoint(self.outerRight, self.outerTop)

  @outerTopRight.SET
  def setOuterTopRight(self, *_) -> Never:
    """Illegal setter-function for outerTopRight"""
    from worktoy.waitaminute import ReadOnlyException
    attName = 'outerTopRight'
    insName = str(self)
    clsName = self.__class__
    raise ReadOnlyException(attName, insName, clsName)

  @outerTopRight.DEL
  def delOuterTopRight(self, *_) -> Never:
    """Illegal deleter-function for outerTopRight"""
    from worktoy.waitaminute import ProtectedAttributeError
    attName = 'outerTopRight'
    insName = str(self)
    clsName = self.__class__
    raise ProtectedAttributeError(attName, insName, clsName)

  # | _________________________________________________________________ | #
  # | <<<<<<<<<<<<<<<<<<<<<<<  outerBottomRight  >>>>>>>>>>>>>>>>>>>>>> | #
  # | ¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨ | #
  @outerBottomRight.GET
  def getOuterBottomRight(self, ) -> QPoint:
    """Getter-function for outerBottomRight"""
    return QPoint(self.outerRight, self.outerBottom)

  @outerBottomRight.SET
  def setOuterBottomRight(self, *_) -> Never:
    """Illegal setter-function for outerBottomRight"""
    from worktoy.waitaminute import ReadOnlyException
    attName = 'outerBottomRight'
    insName = str(self)
    clsName = self.__class__
    raise ReadOnlyException(attName, insName, clsName)

  @outerBottomRight.DEL
  def delOuterBottomRight(self, *_) -> Never:
    """Illegal deleter-function for outerBottomRight"""
    from worktoy.waitaminute import ProtectedAttributeError
    attName = 'outerBottomRight'
    insName = str(self)
    clsName = self.__class__
    raise ProtectedAttributeError(attName, insName, clsName)

  # | _________________________________________________________________ | #
  # | <<<<<<<<<<<<<<<<<<<<<<<  outerBottomLeft  >>>>>>>>>>>>>>>>>>>>>>> | #
  # | ¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨ | #
  @outerBottomLeft.GET
  def getOuterBottomLeft(self, ) -> QPoint:
    """Getter-function for outerBottomLeft"""
    return QPoint(self.outerLeft, self.outerBottom)

  @outerBottomLeft.SET
  def setOuterBottomLeft(self, *_) -> Never:
    """Illegal setter-function for outerBottomLeft"""
    from worktoy.waitaminute import ReadOnlyException
    attName = 'outerBottomLeft'
    insName = str(self)
    clsName = self.__class__
    raise ReadOnlyException(attName, insName, clsName)

  @outerBottomLeft.DEL
  def delOuterBottomLeft(self, *_) -> Never:
    """Illegal deleter-function for outerBottomLeft"""
    from worktoy.waitaminute import ProtectedAttributeError
    attName = 'outerBottomLeft'
    insName = str(self)
    clsName = self.__class__
    raise ProtectedAttributeError(attName, insName, clsName)

  # | _________________________________________________________________ | #
  # | <<<<<<<<<<<<<<<<<<<<<<<<<<  outerArea  >>>>>>>>>>>>>>>>>>>>>>>>>> | #
  # | ¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨ | #
  @outerArea.GET
  def getOuterArea(self, ) -> int:
    """Getter-function for outerArea"""
    return self.outerWidth * self.outerHeight

  @outerArea.SET
  def setOuterArea(self, *_) -> Never:
    """Illegal setter-function for outerArea"""
    from worktoy.waitaminute import ReadOnlyException
    attName = 'outerArea'
    insName = str(self)
    clsName = self.__class__
    raise ReadOnlyException(attName, insName, clsName)

  @outerArea.DEL
  def delOuterArea(self, *_) -> Never:
    """Illegal deleter-function for outerArea"""
    from worktoy.waitaminute import ProtectedAttributeError
    attName = 'outerArea'
    insName = str(self)
    clsName = self.__class__
    raise ProtectedAttributeError(attName, insName, clsName)

  # | _________________________________________________________________ | #
  # | <<<<<<<<<<<<<<<<<<<<<<<<<<  outerSize  >>>>>>>>>>>>>>>>>>>>>>>>>> | #
  # | ¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨ | #
  @outerSize.GET
  def getOuterSize(self, ) -> QSize:
    """Getter-function for outerSize"""
    return QSize(self.outerWidth, self.outerHeight)

  @outerSize.SET
  def setOuterSize(self, *_) -> Never:
    """Illegal setter-function for outerSize"""
    from worktoy.waitaminute import ReadOnlyException
    attName = 'outerSize'
    insName = str(self)
    clsName = self.__class__
    raise ReadOnlyException(attName, insName, clsName)

  @outerSize.DEL
  def delOuterSize(self, *_) -> Never:
    """Illegal deleter-function for outerSize"""
    from worktoy.waitaminute import ProtectedAttributeError
    attName = 'outerSize'
    insName = str(self)
    clsName = self.__class__
    raise ProtectedAttributeError(attName, insName, clsName)

  # | _________________________________________________________________ | #
  # | <<<<<<<<<<<<<<<<<<<<<<<<<<  outerRect  >>>>>>>>>>>>>>>>>>>>>>>>>> | #
  # | ¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨ | #
  @outerRect.GET
  def getOuterRect(self, ) -> QRect:
    """Getter-function for outerRect"""
    return QRect(self.outerTopLeft, self.outerBottomRight)

  @outerRect.SET
  def setOuterRect(self, *_) -> Never:
    """Illegal setter-function for outerRect"""
    from worktoy.waitaminute import ReadOnlyException
    attName = 'outerRect'
    insName = str(self)
    clsName = self.__class__
    raise ReadOnlyException(attName, insName, clsName)

  @outerRect.DEL
  def delOuterRect(self, *_) -> Never:
    """Illegal deleter-function for outerRect"""
    from worktoy.waitaminute import ProtectedAttributeError
    attName = 'outerRect'
    insName = str(self)
    clsName = self.__class__
    raise ProtectedAttributeError(attName, insName, clsName)

  # | _________________________________________________________________ | #
  # | <<<<<<<<<<<<<<<<<<<<<<<<<  borderedLeft  >>>>>>>>>>>>>>>>>>>>>>>> | #
  # | ¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨ | #
  @borderedLeft.GET
  def getBorderedLeft(self, ) -> int:
    """Getter-function for borderedLeft"""
    return self.outerLeft + self.marginLeft

  @borderedLeft.SET
  def setBorderedLeft(self, *_) -> Never:
    """Illegal setter-function for borderedLeft"""
    from worktoy.waitaminute import ReadOnlyException
    attName = 'borderedLeft'
    insName = str(self)
    clsName = self.__class__
    raise ReadOnlyException(attName, insName, clsName)

  @borderedLeft.DEL
  def delBorderedLeft(self, *_) -> Never:
    """Illegal deleter-function for borderedLeft"""
    from worktoy.waitaminute import ProtectedAttributeError
    attName = 'borderedLeft'
    insName = str(self)
    clsName = self.__class__
    raise ProtectedAttributeError(attName, insName, clsName)

  # | _________________________________________________________________ | #
  # | <<<<<<<<<<<<<<<<<<<<<<<<<  borderedTop  >>>>>>>>>>>>>>>>>>>>>>>>> | #
  # | ¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨ | #
  @borderedTop.GET
  def getBorderedTop(self, ) -> int:
    """Getter-function for borderedTop"""
    return self.outerTop + self.marginTop

  @borderedTop.SET
  def setBorderedTop(self, *_) -> Never:
    """Illegal setter-function for borderedTop"""
    from worktoy.waitaminute import ReadOnlyException
    attName = 'borderedTop'
    insName = str(self)
    clsName = self.__class__
    raise ReadOnlyException(attName, insName, clsName)

  @borderedTop.DEL
  def delBorderedTop(self, *_) -> Never:
    """Illegal deleter-function for borderedTop"""
    from worktoy.waitaminute import ProtectedAttributeError
    attName = 'borderedTop'
    insName = str(self)
    clsName = self.__class__
    raise ProtectedAttributeError(attName, insName, clsName)

  # | _________________________________________________________________ | #
  # | <<<<<<<<<<<<<<<<<<<<<<<<  borderedRight  >>>>>>>>>>>>>>>>>>>>>>>> | #
  # | ¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨ | #
  @borderedRight.GET
  def getBorderedRight(self, ) -> int:
    """Getter-function for borderedRight"""
    return self.paddedRight + self.borderRight

  @borderedRight.SET
  def setBorderedRight(self, *_) -> Never:
    """Illegal setter-function for borderedRight"""
    from worktoy.waitaminute import ReadOnlyException
    attName = 'borderedRight'
    insName = str(self)
    clsName = self.__class__
    raise ReadOnlyException(attName, insName, clsName)

  @borderedRight.DEL
  def delBorderedRight(self, *_) -> Never:
    """Illegal deleter-function for borderedRight"""
    from worktoy.waitaminute import ProtectedAttributeError
    attName = 'borderedRight'
    insName = str(self)
    clsName = self.__class__
    raise ProtectedAttributeError(attName, insName, clsName)

  # | _________________________________________________________________ | #
  # | <<<<<<<<<<<<<<<<<<<<<<<<  borderedBottom  >>>>>>>>>>>>>>>>>>>>>>> | #
  # | ¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨ | #
  @borderedBottom.GET
  def getBorderedBottom(self, ) -> int:
    """Getter-function for borderedBottom"""
    return self.paddedBottom + self.borderBottom

  @borderedBottom.SET
  def setBorderedBottom(self, *_) -> Never:
    """Illegal setter-function for borderedBottom"""
    from worktoy.waitaminute import ReadOnlyException
    attName = 'borderedBottom'
    insName = str(self)
    clsName = self.__class__
    raise ReadOnlyException(attName, insName, clsName)

  @borderedBottom.DEL
  def delBorderedBottom(self, *_) -> Never:
    """Illegal deleter-function for borderedBottom"""
    from worktoy.waitaminute import ProtectedAttributeError
    attName = 'borderedBottom'
    insName = str(self)
    clsName = self.__class__
    raise ProtectedAttributeError(attName, insName, clsName)

  # | _________________________________________________________________ | #
  # | <<<<<<<<<<<<<<<<<<<<<<<<  borderedWidth  >>>>>>>>>>>>>>>>>>>>>>>> | #
  # | ¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨ | #
  @borderedWidth.GET
  def getBorderedWidth(self, ) -> int:
    """Getter-function for borderedWidth"""
    return self.paddedWidth + self.borderLeft + self.borderRight

  @borderedWidth.SET
  def setBorderedWidth(self, *_) -> Never:
    """Illegal setter-function for borderedWidth"""
    from worktoy.waitaminute import ReadOnlyException
    attName = 'borderedWidth'
    insName = str(self)
    clsName = self.__class__
    raise ReadOnlyException(attName, insName, clsName)

  @borderedWidth.DEL
  def delBorderedWidth(self, *_) -> Never:
    """Illegal deleter-function for borderedWidth"""
    from worktoy.waitaminute import ProtectedAttributeError
    attName = 'borderedWidth'
    insName = str(self)
    clsName = self.__class__
    raise ProtectedAttributeError(attName, insName, clsName)

  # | _________________________________________________________________ | #
  # | <<<<<<<<<<<<<<<<<<<<<<<<  borderedHeight  >>>>>>>>>>>>>>>>>>>>>>> | #
  # | ¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨ | #
  @borderedHeight.GET
  def getBorderedHeight(self, ) -> int:
    """Getter-function for borderedHeight"""
    return self.paddedHeight + self.borderTop + self.borderBottom

  @borderedHeight.SET
  def setBorderedHeight(self, *_) -> Never:
    """Illegal setter-function for borderedHeight"""
    from worktoy.waitaminute import ReadOnlyException
    attName = 'borderedHeight'
    insName = str(self)
    clsName = self.__class__
    raise ReadOnlyException(attName, insName, clsName)

  @borderedHeight.DEL
  def delBorderedHeight(self, *_) -> Never:
    """Illegal deleter-function for borderedHeight"""
    from worktoy.waitaminute import ProtectedAttributeError
    attName = 'borderedHeight'
    insName = str(self)
    clsName = self.__class__
    raise ProtectedAttributeError(attName, insName, clsName)

  # | _________________________________________________________________ | #
  # | <<<<<<<<<<<<<<<<<<<<<<<<<  borderedArea  >>>>>>>>>>>>>>>>>>>>>>>> | #
  # | ¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨ | #
  @borderedArea.GET
  def getBorderedArea(self, ) -> int:
    """Getter-function for borderedArea"""
    return self.borderedWidth * self.borderedHeight

  @borderedArea.SET
  def setBorderedArea(self, *_) -> Never:
    """Illegal setter-function for borderedArea"""
    from worktoy.waitaminute import ReadOnlyException
    attName = 'borderedArea'
    insName = str(self)
    clsName = self.__class__
    raise ReadOnlyException(attName, insName, clsName)

  @borderedArea.DEL
  def delBorderedArea(self, *_) -> Never:
    """Illegal deleter-function for borderedArea"""
    from worktoy.waitaminute import ProtectedAttributeError
    attName = 'borderedArea'
    insName = str(self)
    clsName = self.__class__
    raise ProtectedAttributeError(attName, insName, clsName)

  # | _________________________________________________________________ | #
  # | <<<<<<<<<<<<<<<<<<<<<<<<<  borderedSize  >>>>>>>>>>>>>>>>>>>>>>>> | #
  # | ¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨ | #
  @borderedSize.GET
  def getBorderedSize(self, ) -> QSize:
    """Getter-function for borderedSize"""
    return QSize(self.borderedWidth, self.borderedHeight)

  @borderedSize.SET
  def setBorderedSize(self, *_) -> Never:
    """Illegal setter-function for borderedSize"""
    from worktoy.waitaminute import ReadOnlyException
    attName = 'borderedSize'
    insName = str(self)
    clsName = self.__class__
    raise ReadOnlyException(attName, insName, clsName)

  @borderedSize.DEL
  def delBorderedSize(self, *_) -> Never:
    """Illegal deleter-function for borderedSize"""
    from worktoy.waitaminute import ProtectedAttributeError
    attName = 'borderedSize'
    insName = str(self)
    clsName = self.__class__
    raise ProtectedAttributeError(attName, insName, clsName)

  # | _________________________________________________________________ | #
  # | <<<<<<<<<<<<<<<<<<<<<<<<<  borderedRect  >>>>>>>>>>>>>>>>>>>>>>>> | #
  # | ¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨ | #
  @borderedRect.GET
  def getBorderedRect(self, ) -> QRect:
    """Getter-function for borderedRect"""
    return QRect(self.borderedTopLeft, self.borderedBottomRight)

  @borderedRect.SET
  def setBorderedRect(self, *_) -> Never:
    """Illegal setter-function for borderedRect"""
    from worktoy.waitaminute import ReadOnlyException
    attName = 'borderedRect'
    insName = str(self)
    clsName = self.__class__
    raise ReadOnlyException(attName, insName, clsName)

  @borderedRect.DEL
  def delBorderedRect(self, *_) -> Never:
    """Illegal deleter-function for borderedRect"""
    from worktoy.waitaminute import ProtectedAttributeError
    attName = 'borderedRect'
    insName = str(self)
    clsName = self.__class__
    raise ProtectedAttributeError(attName, insName, clsName)

  # | _________________________________________________________________ | #
  # | <<<<<<<<<<<<<<<<<<<<<<<  borderedTopLeft  >>>>>>>>>>>>>>>>>>>>>>> | #
  # | ¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨ | #
  @borderedTopLeft.GET
  def getBorderedTopLeft(self, ) -> QPoint:
    """Getter-function for borderedTopLeft"""
    return QPoint(self.borderedLeft, self.borderedTop)

  @borderedTopLeft.SET
  def setBorderedTopLeft(self, *_) -> Never:
    """Illegal setter-function for borderedTopLeft"""
    from worktoy.waitaminute import ReadOnlyException
    attName = 'borderedTopLeft'
    insName = str(self)
    clsName = self.__class__
    raise ReadOnlyException(attName, insName, clsName)

  @borderedTopLeft.DEL
  def delBorderedTopLeft(self, *_) -> Never:
    """Illegal deleter-function for borderedTopLeft"""
    from worktoy.waitaminute import ProtectedAttributeError
    attName = 'borderedTopLeft'
    insName = str(self)
    clsName = self.__class__
    raise ProtectedAttributeError(attName, insName, clsName)

  # | _________________________________________________________________ | #
  # | <<<<<<<<<<<<<<<<<<<<<<<  borderedTopRight  >>>>>>>>>>>>>>>>>>>>>> | #
  # | ¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨ | #
  @borderedTopRight.GET
  def getBorderedTopRight(self, ) -> QPoint:
    """Getter-function for borderedTopRight"""
    return QPoint(self.borderedRight, self.borderedTop)

  @borderedTopRight.SET
  def setBorderedTopRight(self, *_) -> Never:
    """Illegal setter-function for borderedTopRight"""
    from worktoy.waitaminute import ReadOnlyException
    attName = 'borderedTopRight'
    insName = str(self)
    clsName = self.__class__
    raise ReadOnlyException(attName, insName, clsName)

  @borderedTopRight.DEL
  def delBorderedTopRight(self, *_) -> Never:
    """Illegal deleter-function for borderedTopRight"""
    from worktoy.waitaminute import ProtectedAttributeError
    attName = 'borderedTopRight'
    insName = str(self)
    clsName = self.__class__
    raise ProtectedAttributeError(attName, insName, clsName)

  # | _________________________________________________________________ | #
  # | <<<<<<<<<<<<<<<<<<<<<  borderedBottomRight  >>>>>>>>>>>>>>>>>>>>> | #
  # | ¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨ | #
  @borderedBottomRight.GET
  def getBorderedBottomRight(self, ) -> QPoint:
    """Getter-function for borderedBottomRight"""
    return QPoint(self.borderedRight, self.borderedBottom)

  @borderedBottomRight.SET
  def setBorderedBottomRight(self, *_) -> Never:
    """Illegal setter-function for borderedBottomRight"""
    from worktoy.waitaminute import ReadOnlyException
    attName = 'borderedBottomRight'
    insName = str(self)
    clsName = self.__class__
    raise ReadOnlyException(attName, insName, clsName)

  @borderedBottomRight.DEL
  def delBorderedBottomRight(self, *_) -> Never:
    """Illegal deleter-function for borderedBottomRight"""
    from worktoy.waitaminute import ProtectedAttributeError
    attName = 'borderedBottomRight'
    insName = str(self)
    clsName = self.__class__
    raise ProtectedAttributeError(attName, insName, clsName)

  # | _________________________________________________________________ | #
  # | <<<<<<<<<<<<<<<<<<<<<<  borderedBottomLeft  >>>>>>>>>>>>>>>>>>>>> | #
  # | ¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨ | #
  @borderedBottomLeft.GET
  def getBorderedBottomLeft(self, ) -> QPoint:
    """Getter-function for borderedBottomLeft"""
    return QPoint(self.borderedLeft, self.borderedBottom)

  @borderedBottomLeft.SET
  def setBorderedBottomLeft(self, *_) -> Never:
    """Illegal setter-function for borderedBottomLeft"""
    from worktoy.waitaminute import ReadOnlyException
    attName = 'borderedBottomLeft'
    insName = str(self)
    clsName = self.__class__
    raise ReadOnlyException(attName, insName, clsName)

  @borderedBottomLeft.DEL
  def delBorderedBottomLeft(self, *_) -> Never:
    """Illegal deleter-function for borderedBottomLeft"""
    from worktoy.waitaminute import ProtectedAttributeError
    attName = 'borderedBottomLeft'
    insName = str(self)
    clsName = self.__class__
    raise ProtectedAttributeError(attName, insName, clsName)

  # | _________________________________________________________________ | #
  # | <<<<<<<<<<<<<<<<<<<<<<<<<<  paddedLeft  >>>>>>>>>>>>>>>>>>>>>>>>> | #
  # | ¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨ | #
  @paddedLeft.GET
  def getPaddedLeft(self, ) -> int:
    """Getter-function for paddedLeft"""
    return self.borderedLeft + self.borderLeft

  @paddedLeft.SET
  def setPaddedLeft(self, *_) -> Never:
    """Illegal setter-function for paddedLeft"""
    from worktoy.waitaminute import ReadOnlyException
    attName = 'paddedLeft'
    insName = str(self)
    clsName = self.__class__
    raise ReadOnlyException(attName, insName, clsName)

  @paddedLeft.DEL
  def delPaddedLeft(self, *_) -> Never:
    """Illegal deleter-function for paddedLeft"""
    from worktoy.waitaminute import ProtectedAttributeError
    attName = 'paddedLeft'
    insName = str(self)
    clsName = self.__class__
    raise ProtectedAttributeError(attName, insName, clsName)

  # | _________________________________________________________________ | #
  # | <<<<<<<<<<<<<<<<<<<<<<<<<<  paddedTop  >>>>>>>>>>>>>>>>>>>>>>>>>> | #
  # | ¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨ | #
  @paddedTop.GET
  def getPaddedTop(self, ) -> int:
    """Getter-function for paddedTop"""
    return self.borderedTop + self.borderTop

  @paddedTop.SET
  def setPaddedTop(self, *_) -> Never:
    """Illegal setter-function for paddedTop"""
    from worktoy.waitaminute import ReadOnlyException
    attName = 'paddedTop'
    insName = str(self)
    clsName = self.__class__
    raise ReadOnlyException(attName, insName, clsName)

  @paddedTop.DEL
  def delPaddedTop(self, *_) -> Never:
    """Illegal deleter-function for paddedTop"""
    from worktoy.waitaminute import ProtectedAttributeError
    attName = 'paddedTop'
    insName = str(self)
    clsName = self.__class__
    raise ProtectedAttributeError(attName, insName, clsName)

  # | _________________________________________________________________ | #
  # | <<<<<<<<<<<<<<<<<<<<<<<<<  paddedRight  >>>>>>>>>>>>>>>>>>>>>>>>> | #
  # | ¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨ | #
  @paddedRight.GET
  def getPaddedRight(self, ) -> int:
    """Getter-function for paddedRight"""
    return self.innerRight + self.paddingRight

  @paddedRight.SET
  def setPaddedRight(self, *_) -> Never:
    """Illegal setter-function for paddedRight"""
    from worktoy.waitaminute import ReadOnlyException
    attName = 'paddedRight'
    insName = str(self)
    clsName = self.__class__
    raise ReadOnlyException(attName, insName, clsName)

  @paddedRight.DEL
  def delPaddedRight(self, *_) -> Never:
    """Illegal deleter-function for paddedRight"""
    from worktoy.waitaminute import ProtectedAttributeError
    attName = 'paddedRight'
    insName = str(self)
    clsName = self.__class__
    raise ProtectedAttributeError(attName, insName, clsName)

  # | _________________________________________________________________ | #
  # | <<<<<<<<<<<<<<<<<<<<<<<<<  paddedBottom  >>>>>>>>>>>>>>>>>>>>>>>> | #
  # | ¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨ | #
  @paddedBottom.GET
  def getPaddedBottom(self, ) -> int:
    """Getter-function for paddedBottom"""
    return self.innerBottom + self.paddingBottom

  @paddedBottom.SET
  def setPaddedBottom(self, *_) -> Never:
    """Illegal setter-function for paddedBottom"""
    from worktoy.waitaminute import ReadOnlyException
    attName = 'paddedBottom'
    insName = str(self)
    clsName = self.__class__
    raise ReadOnlyException(attName, insName, clsName)

  @paddedBottom.DEL
  def delPaddedBottom(self, *_) -> Never:
    """Illegal deleter-function for paddedBottom"""
    from worktoy.waitaminute import ProtectedAttributeError
    attName = 'paddedBottom'
    insName = str(self)
    clsName = self.__class__
    raise ProtectedAttributeError(attName, insName, clsName)

  # | _________________________________________________________________ | #
  # | <<<<<<<<<<<<<<<<<<<<<<<<<  paddedWidth  >>>>>>>>>>>>>>>>>>>>>>>>> | #
  # | ¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨ | #
  @paddedWidth.GET
  def getPaddedWidth(self, ) -> int:
    """Getter-function for paddedWidth"""
    return self.innerWidth + self.paddingLeft + self.paddingRight

  @paddedWidth.SET
  def setPaddedWidth(self, *_) -> Never:
    """Illegal setter-function for paddedWidth"""
    from worktoy.waitaminute import ReadOnlyException
    attName = 'paddedWidth'
    insName = str(self)
    clsName = self.__class__
    raise ReadOnlyException(attName, insName, clsName)

  @paddedWidth.DEL
  def delPaddedWidth(self, *_) -> Never:
    """Illegal deleter-function for paddedWidth"""
    from worktoy.waitaminute import ProtectedAttributeError
    attName = 'paddedWidth'
    insName = str(self)
    clsName = self.__class__
    raise ProtectedAttributeError(attName, insName, clsName)

  # | _________________________________________________________________ | #
  # | <<<<<<<<<<<<<<<<<<<<<<<<<  paddedHeight  >>>>>>>>>>>>>>>>>>>>>>>> | #
  # | ¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨ | #
  @paddedHeight.GET
  def getPaddedHeight(self, ) -> int:
    """Getter-function for paddedHeight"""
    return self.innerHeight + self.paddingTop + self.paddingBottom

  @paddedHeight.SET
  def setPaddedHeight(self, *_) -> Never:
    """Illegal setter-function for paddedHeight"""
    from worktoy.waitaminute import ReadOnlyException
    attName = 'paddedHeight'
    insName = str(self)
    clsName = self.__class__
    raise ReadOnlyException(attName, insName, clsName)

  @paddedHeight.DEL
  def delPaddedHeight(self, *_) -> Never:
    """Illegal deleter-function for paddedHeight"""
    from worktoy.waitaminute import ProtectedAttributeError
    attName = 'paddedHeight'
    insName = str(self)
    clsName = self.__class__
    raise ProtectedAttributeError(attName, insName, clsName)

  # | _________________________________________________________________ | #
  # | <<<<<<<<<<<<<<<<<<<<<<<<<<  paddedArea  >>>>>>>>>>>>>>>>>>>>>>>>> | #
  # | ¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨ | #
  @paddedArea.GET
  def getPaddedArea(self, ) -> int:
    """Getter-function for paddedArea"""
    return self.paddedWidth * self.paddedHeight

  @paddedArea.SET
  def setPaddedArea(self, *_) -> Never:
    """Illegal setter-function for paddedArea"""
    from worktoy.waitaminute import ReadOnlyException
    attName = 'paddedArea'
    insName = str(self)
    clsName = self.__class__
    raise ReadOnlyException(attName, insName, clsName)

  @paddedArea.DEL
  def delPaddedArea(self, *_) -> Never:
    """Illegal deleter-function for paddedArea"""
    from worktoy.waitaminute import ProtectedAttributeError
    attName = 'paddedArea'
    insName = str(self)
    clsName = self.__class__
    raise ProtectedAttributeError(attName, insName, clsName)

  # | _________________________________________________________________ | #
  # | <<<<<<<<<<<<<<<<<<<<<<<<<<  paddedSize  >>>>>>>>>>>>>>>>>>>>>>>>> | #
  # | ¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨ | #
  @paddedSize.GET
  def getPaddedSize(self, ) -> QSize:
    """Getter-function for paddedSize"""
    return QSize(self.paddedWidth, self.paddedHeight)

  @paddedSize.SET
  def setPaddedSize(self, *_) -> Never:
    """Illegal setter-function for paddedSize"""
    from worktoy.waitaminute import ReadOnlyException
    attName = 'paddedSize'
    insName = str(self)
    clsName = self.__class__
    raise ReadOnlyException(attName, insName, clsName)

  @paddedSize.DEL
  def delPaddedSize(self, *_) -> Never:
    """Illegal deleter-function for paddedSize"""
    from worktoy.waitaminute import ProtectedAttributeError
    attName = 'paddedSize'
    insName = str(self)
    clsName = self.__class__
    raise ProtectedAttributeError(attName, insName, clsName)

  # | _________________________________________________________________ | #
  # | <<<<<<<<<<<<<<<<<<<<<<<<<<  paddedRect  >>>>>>>>>>>>>>>>>>>>>>>>> | #
  # | ¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨ | #
  @paddedRect.GET
  def getPaddedRect(self, ) -> QRect:
    """Getter-function for paddedRect"""
    return QRect(self.paddedTopLeft, self.paddedBottomRight)

  @paddedRect.SET
  def setPaddedRect(self, *_) -> Never:
    """Illegal setter-function for paddedRect"""
    from worktoy.waitaminute import ReadOnlyException
    attName = 'paddedRect'
    insName = str(self)
    clsName = self.__class__
    raise ReadOnlyException(attName, insName, clsName)

  @paddedRect.DEL
  def delPaddedRect(self, *_) -> Never:
    """Illegal deleter-function for paddedRect"""
    from worktoy.waitaminute import ProtectedAttributeError
    attName = 'paddedRect'
    insName = str(self)
    clsName = self.__class__
    raise ProtectedAttributeError(attName, insName, clsName)

  # | _________________________________________________________________ | #
  # | <<<<<<<<<<<<<<<<<<<<<<<<  paddedTopLeft  >>>>>>>>>>>>>>>>>>>>>>>> | #
  # | ¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨ | #
  @paddedTopLeft.GET
  def getPaddedTopLeft(self, ) -> QPoint:
    """Getter-function for paddedTopLeft"""
    return QPoint(self.paddedLeft, self.paddedTop)

  @paddedTopLeft.SET
  def setPaddedTopLeft(self, *_) -> Never:
    """Illegal setter-function for paddedTopLeft"""
    from worktoy.waitaminute import ReadOnlyException
    attName = 'paddedTopLeft'
    insName = str(self)
    clsName = self.__class__
    raise ReadOnlyException(attName, insName, clsName)

  @paddedTopLeft.DEL
  def delPaddedTopLeft(self, *_) -> Never:
    """Illegal deleter-function for paddedTopLeft"""
    from worktoy.waitaminute import ProtectedAttributeError
    attName = 'paddedTopLeft'
    insName = str(self)
    clsName = self.__class__
    raise ProtectedAttributeError(attName, insName, clsName)

  # | _________________________________________________________________ | #
  # | <<<<<<<<<<<<<<<<<<<<<<<<  paddedTopRight  >>>>>>>>>>>>>>>>>>>>>>> | #
  # | ¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨ | #
  @paddedTopRight.GET
  def getPaddedTopRight(self, ) -> QPoint:
    """Getter-function for paddedTopRight"""
    return QPoint(self.paddedRight, self.paddedTop)

  @paddedTopRight.SET
  def setPaddedTopRight(self, *_) -> Never:
    """Illegal setter-function for paddedTopRight"""
    from worktoy.waitaminute import ReadOnlyException
    attName = 'paddedTopRight'
    insName = str(self)
    clsName = self.__class__
    raise ReadOnlyException(attName, insName, clsName)

  @paddedTopRight.DEL
  def delPaddedTopRight(self, *_) -> Never:
    """Illegal deleter-function for paddedTopRight"""
    from worktoy.waitaminute import ProtectedAttributeError
    attName = 'paddedTopRight'
    insName = str(self)
    clsName = self.__class__
    raise ProtectedAttributeError(attName, insName, clsName)

  # | _________________________________________________________________ | #
  # | <<<<<<<<<<<<<<<<<<<<<<  paddedBottomRight  >>>>>>>>>>>>>>>>>>>>>> | #
  # | ¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨ | #
  @paddedBottomRight.GET
  def getPaddedBottomRight(self, ) -> QPoint:
    """Getter-function for paddedBottomRight"""
    return QPoint(self.paddedRight, self.paddedBottom)

  @paddedBottomRight.SET
  def setPaddedBottomRight(self, *_) -> Never:
    """Illegal setter-function for paddedBottomRight"""
    from worktoy.waitaminute import ReadOnlyException
    attName = 'paddedBottomRight'
    insName = str(self)
    clsName = self.__class__
    raise ReadOnlyException(attName, insName, clsName)

  @paddedBottomRight.DEL
  def delPaddedBottomRight(self, *_) -> Never:
    """Illegal deleter-function for paddedBottomRight"""
    from worktoy.waitaminute import ProtectedAttributeError
    attName = 'paddedBottomRight'
    insName = str(self)
    clsName = self.__class__
    raise ProtectedAttributeError(attName, insName, clsName)

  # | _________________________________________________________________ | #
  # | <<<<<<<<<<<<<<<<<<<<<<<  paddedBottomLeft  >>>>>>>>>>>>>>>>>>>>>> | #
  # | ¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨ | #
  @paddedBottomLeft.GET
  def getPaddedBottomLeft(self, ) -> QPoint:
    """Getter-function for paddedBottomLeft"""
    return QPoint(self.paddedLeft, self.paddedBottom)

  @paddedBottomLeft.SET
  def setPaddedBottomLeft(self, *_) -> Never:
    """Illegal setter-function for paddedBottomLeft"""
    from worktoy.waitaminute import ReadOnlyException
    attName = 'paddedBottomLeft'
    insName = str(self)
    clsName = self.__class__
    raise ReadOnlyException(attName, insName, clsName)

  @paddedBottomLeft.DEL
  def delPaddedBottomLeft(self, *_) -> Never:
    """Illegal deleter-function for paddedBottomLeft"""
    from worktoy.waitaminute import ProtectedAttributeError
    attName = 'paddedBottomLeft'
    insName = str(self)
    clsName = self.__class__
    raise ProtectedAttributeError(attName, insName, clsName)

  # | _________________________________________________________________ | #
  # | <<<<<<<<<<<<<<<<<<<<<<<<<<  innerLeft  >>>>>>>>>>>>>>>>>>>>>>>>>> | #
  # | ¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨ | #
  @innerLeft.GET
  def getInnerLeft(self, ) -> int:
    """Getter-function for innerLeft"""
    return self.paddedLeft + self.paddingLeft

  @innerLeft.SET
  def setInnerLeft(self, *_) -> Never:
    """Illegal setter-function for innerLeft"""
    from worktoy.waitaminute import ReadOnlyException
    attName = 'innerLeft'
    insName = str(self)
    clsName = self.__class__
    raise ReadOnlyException(attName, insName, clsName)

  @innerLeft.DEL
  def delInnerLeft(self, *_) -> Never:
    """Illegal deleter-function for innerLeft"""
    from worktoy.waitaminute import ProtectedAttributeError
    attName = 'innerLeft'
    insName = str(self)
    clsName = self.__class__
    raise ProtectedAttributeError(attName, insName, clsName)

  # | _________________________________________________________________ | #
  # | <<<<<<<<<<<<<<<<<<<<<<<<<<<  innerTop  >>>>>>>>>>>>>>>>>>>>>>>>>> | #
  # | ¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨ | #
  @innerTop.GET
  def getInnerTop(self, ) -> int:
    """Getter-function for innerTop"""
    return self.paddedTop + self.paddingTop

  @innerTop.SET
  def setInnerTop(self, *_) -> Never:
    """Illegal setter-function for innerTop"""
    from worktoy.waitaminute import ReadOnlyException
    attName = 'innerTop'
    insName = str(self)
    clsName = self.__class__
    raise ReadOnlyException(attName, insName, clsName)

  @innerTop.DEL
  def delInnerTop(self, *_) -> Never:
    """Illegal deleter-function for innerTop"""
    from worktoy.waitaminute import ProtectedAttributeError
    attName = 'innerTop'
    insName = str(self)
    clsName = self.__class__
    raise ProtectedAttributeError(attName, insName, clsName)

  # | _________________________________________________________________ | #
  # | <<<<<<<<<<<<<<<<<<<<<<<<<<  innerRight  >>>>>>>>>>>>>>>>>>>>>>>>> | #
  # | ¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨ | #
  @innerRight.GET
  def getInnerRight(self, ) -> int:
    """Getter-function for innerRight"""
    return self.innerLeft + self.innerWidth

  @innerRight.SET
  def setInnerRight(self, *_) -> Never:
    """Illegal setter-function for innerRight"""
    from worktoy.waitaminute import ReadOnlyException
    attName = 'innerRight'
    insName = str(self)
    clsName = self.__class__
    raise ReadOnlyException(attName, insName, clsName)

  @innerRight.DEL
  def delInnerRight(self, *_) -> Never:
    """Illegal deleter-function for innerRight"""
    from worktoy.waitaminute import ProtectedAttributeError
    attName = 'innerRight'
    insName = str(self)
    clsName = self.__class__
    raise ProtectedAttributeError(attName, insName, clsName)

  # | _________________________________________________________________ | #
  # | <<<<<<<<<<<<<<<<<<<<<<<<<  innerBottom  >>>>>>>>>>>>>>>>>>>>>>>>> | #
  # | ¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨ | #
  @innerBottom.GET
  def getInnerBottom(self, ) -> int:
    """Getter-function for innerBottom"""
    return self.innerHeight + self.innerTop

  @innerBottom.SET
  def setInnerBottom(self, *_) -> Never:
    """Illegal setter-function for innerBottom"""
    from worktoy.waitaminute import ReadOnlyException
    attName = 'innerBottom'
    insName = str(self)
    clsName = self.__class__
    raise ReadOnlyException(attName, insName, clsName)

  @innerBottom.DEL
  def delInnerBottom(self, *_) -> Never:
    """Illegal deleter-function for innerBottom"""
    from worktoy.waitaminute import ProtectedAttributeError
    attName = 'innerBottom'
    insName = str(self)
    clsName = self.__class__
    raise ProtectedAttributeError(attName, insName, clsName)

  # | _________________________________________________________________ | #
  # | <<<<<<<<<<<<<<<<<<<<<<<<<<  innerArea  >>>>>>>>>>>>>>>>>>>>>>>>>> | #
  # | ¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨ | #
  @innerArea.GET
  def getInnerArea(self, ) -> int:
    """Getter-function for innerArea"""
    return self.innerWidth * self.innerHeight

  @innerArea.SET
  def setInnerArea(self, *_) -> Never:
    """Illegal setter-function for innerArea"""
    from worktoy.waitaminute import ReadOnlyException
    attName = 'innerArea'
    insName = str(self)
    clsName = self.__class__
    raise ReadOnlyException(attName, insName, clsName)

  @innerArea.DEL
  def delInnerArea(self, *_) -> Never:
    """Illegal deleter-function for innerArea"""
    from worktoy.waitaminute import ProtectedAttributeError
    attName = 'innerArea'
    insName = str(self)
    clsName = self.__class__
    raise ProtectedAttributeError(attName, insName, clsName)

  # | _________________________________________________________________ | #
  # | <<<<<<<<<<<<<<<<<<<<<<<<<  innerTopLeft  >>>>>>>>>>>>>>>>>>>>>>>> | #
  # | ¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨ | #
  @innerTopLeft.GET
  def getInnerTopLeft(self, ) -> QPoint:
    """Getter-function for innerTopLeft"""
    return QPoint(self.innerLeft, self.innerTop)

  @innerTopLeft.SET
  def setInnerTopLeft(self, *_) -> Never:
    """Illegal setter-function for innerTopLeft"""
    from worktoy.waitaminute import ReadOnlyException
    attName = 'innerTopLeft'
    insName = str(self)
    clsName = self.__class__
    raise ReadOnlyException(attName, insName, clsName)

  @innerTopLeft.DEL
  def delInnerTopLeft(self, *_) -> Never:
    """Illegal deleter-function for innerTopLeft"""
    from worktoy.waitaminute import ProtectedAttributeError
    attName = 'innerTopLeft'
    insName = str(self)
    clsName = self.__class__
    raise ProtectedAttributeError(attName, insName, clsName)

  # | _________________________________________________________________ | #
  # | <<<<<<<<<<<<<<<<<<<<<<<<  innerTopRight  >>>>>>>>>>>>>>>>>>>>>>>> | #
  # | ¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨ | #
  @innerTopRight.GET
  def getInnerTopRight(self, ) -> QPoint:
    """Getter-function for innerTopRight"""
    return QPoint(self.innerRight, self.innerTop)

  @innerTopRight.SET
  def setInnerTopRight(self, *_) -> Never:
    """Illegal setter-function for innerTopRight"""
    from worktoy.waitaminute import ReadOnlyException
    attName = 'innerTopRight'
    insName = str(self)
    clsName = self.__class__
    raise ReadOnlyException(attName, insName, clsName)

  @innerTopRight.DEL
  def delInnerTopRight(self, *_) -> Never:
    """Illegal deleter-function for innerTopRight"""
    from worktoy.waitaminute import ProtectedAttributeError
    attName = 'innerTopRight'
    insName = str(self)
    clsName = self.__class__
    raise ProtectedAttributeError(attName, insName, clsName)

  # | _________________________________________________________________ | #
  # | <<<<<<<<<<<<<<<<<<<<<<<  innerBottomRight  >>>>>>>>>>>>>>>>>>>>>> | #
  # | ¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨ | #
  @innerBottomRight.GET
  def getInnerBottomRight(self, ) -> QPoint:
    """Getter-function for innerBottomRight"""
    return QPoint(self.innerRight, self.innerBottom, )

  @innerBottomRight.SET
  def setInnerBottomRight(self, *_) -> Never:
    """Illegal setter-function for innerBottomRight"""
    from worktoy.waitaminute import ReadOnlyException
    attName = 'innerBottomRight'
    insName = str(self)
    clsName = self.__class__
    raise ReadOnlyException(attName, insName, clsName)

  @innerBottomRight.DEL
  def delInnerBottomRight(self, *_) -> Never:
    """Illegal deleter-function for innerBottomRight"""
    from worktoy.waitaminute import ProtectedAttributeError
    attName = 'innerBottomRight'
    insName = str(self)
    clsName = self.__class__
    raise ProtectedAttributeError(attName, insName, clsName)

  # | _________________________________________________________________ | #
  # | <<<<<<<<<<<<<<<<<<<<<<<  innerBottomLeft  >>>>>>>>>>>>>>>>>>>>>>> | #
  # | ¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨ | #
  @innerBottomLeft.GET
  def getInnerBottomLeft(self, ) -> QPoint:
    """Getter-function for innerBottomLeft"""
    return QPoint(self.innerLeft, self.innerBottom)

  @innerBottomLeft.SET
  def setInnerBottomLeft(self, *_) -> Never:
    """Illegal setter-function for innerBottomLeft"""
    from worktoy.waitaminute import ReadOnlyException
    attName = 'innerBottomLeft'
    insName = str(self)
    clsName = self.__class__
    raise ReadOnlyException(attName, insName, clsName)

  @innerBottomLeft.DEL
  def delInnerBottomLeft(self, *_) -> Never:
    """Illegal deleter-function for innerBottomLeft"""
    from worktoy.waitaminute import ProtectedAttributeError
    attName = 'innerBottomLeft'
    insName = str(self)
    clsName = self.__class__
    raise ProtectedAttributeError(attName, insName, clsName)

  # | _________________________________________________________________ | #
  # | <<<<<<<<<<<<<<<<<<<<<<<<<<  innerSize  >>>>>>>>>>>>>>>>>>>>>>>>>> | #
  # | ¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨ | #
  @innerSize.GET
  def getInnerSize(self, ) -> QSize:
    """Getter-function for innerSize"""
    return QSize(self.innerWidth, self.innerHeight)

  @innerSize.SET
  def setInnerSize(self, *_) -> Never:
    """Illegal setter-function for innerSize"""
    from worktoy.waitaminute import ReadOnlyException
    attName = 'innerSize'
    insName = str(self)
    clsName = self.__class__
    raise ReadOnlyException(attName, insName, clsName)

  @innerSize.DEL
  def delInnerSize(self, *_) -> Never:
    """Illegal deleter-function for innerSize"""
    from worktoy.waitaminute import ProtectedAttributeError
    attName = 'innerSize'
    insName = str(self)
    clsName = self.__class__
    raise ProtectedAttributeError(attName, insName, clsName)

  # | _________________________________________________________________ | #
  # | <<<<<<<<<<<<<<<<<<<<<<<<<<  innerRect  >>>>>>>>>>>>>>>>>>>>>>>>>> | #
  # | ¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨ | #
  @innerRect.GET
  def getInnerRect(self, ) -> QRect:
    """Getter-function for innerRect"""
    return QRect(self.innerTopLeft, self.innerBottomRight)

  @innerRect.SET
  def setInnerRect(self, *_) -> Never:
    """Illegal setter-function for innerRect"""
    from worktoy.waitaminute import ReadOnlyException
    attName = 'innerRect'
    insName = str(self)
    clsName = self.__class__
    raise ReadOnlyException(attName, insName, clsName)

  @innerRect.DEL
  def delInnerRect(self, *_) -> Never:
    """Illegal deleter-function for innerRect"""
    from worktoy.waitaminute import ProtectedAttributeError
    attName = 'innerRect'
    insName = str(self)
    clsName = self.__class__
    raise ProtectedAttributeError(attName, insName, clsName)

  # | _________________________________________________________________ | #
