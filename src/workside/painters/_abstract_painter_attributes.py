"""WorkSide - Painters - AbstractPainterProperties
Attribute class for AbstractPainter."""
#  MIT Licence
#  Copyright (c) 2023 Asger Jon Vistisen
from __future__ import annotations

from typing import Never, Any

from PySide6.QtGui import QFont, QBrush, QPen, QColor

from workside.settings import Color, PenStyle, BrushStyle, FontFamilies
from worktoy.descriptors import Attribute
from worktoy.worktoyclass import WorkToyClass


class AbstractPainterProperties(WorkToyClass):
  """ Attribute class for AbstractPainter. """
  baseFont = Attribute(QFont())
  baseBrush = Attribute(QBrush())
  basePen = Attribute(QPen())

  # | _________________________________________________________________ | #
  # | <<<<<<<<<<<<<<<<<<<<<<<<<<<  baseFont  >>>>>>>>>>>>>>>>>>>>>>>>>> | #
  # | ¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨ | #
  @baseFont.GET
  def getBaseFont(self, ) -> QFont:
    """Getter-function for baseFont"""
    return self.__base_font__

  @baseFont.SET
  def setBaseFont(self, other: QFont) -> None:
    """Illegal setter-function for baseFont"""
    if isinstance(other, QFont):
      self.__base_font__.setFamily(other.family())
      self.__base_font__.setPointSize(other.pointSize())
      self.__base_font__.setWeight(other.weight())
    if isinstance(other, str):
      if other in FontFamilies:
        return self.__base_font__.setFamily(FontFamilies[other])
    if isinstance(other, int):
      return self.__base_font__.setPointSize(other)
    if isinstance(other, float):
      return self.__base_font__.setPointSizeF(other)

  @baseFont.DEL
  def delBaseFont(self, *_) -> Never:
    """Illegal deleter-function for baseFont"""
    from worktoy.waitaminute import ProtectedAttributeError
    attName = 'baseFont'
    insName = str(self)
    clsName = self.__class__
    raise ProtectedAttributeError(attName, insName, clsName)

  # | _________________________________________________________________ | #
  # | <<<<<<<<<<<<<<<<<<<<<<<<<<  baseBrush  >>>>>>>>>>>>>>>>>>>>>>>>>> | #
  # | ¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨ | #
  @baseBrush.GET
  def getBaseBrush(self, ) -> QBrush:
    """Getter-function for baseBrush"""
    return self.__base_brush__

  @baseBrush.SET
  def setBaseBrush(self, other: Any) -> None:
    """Setter-function for baseBrush"""
    if isinstance(other, QBrush):
      self.__base_brush__.setColor(other.color())
      self.__base_brush__.setStyle(other.style())
    elif isinstance(other, QColor):
      self.__base_brush__.setColor(other)
    elif isinstance(other, Color):
      qColor = QColor(other.red, other.green, other.blue, other.alpha)
      self.__base_brush__.setColor(qColor)
    elif isinstance(other, BrushStyle):
      self.__base_brush__.setStyle(other)

  @baseBrush.DEL
  def delBaseBrush(self, *_) -> Never:
    """Illegal deleter-function for baseBrush"""
    from worktoy.waitaminute import ProtectedAttributeError
    attName = 'baseBrush'
    insName = str(self)
    clsName = self.__class__
    raise ProtectedAttributeError(attName, insName, clsName)

  # | _________________________________________________________________ | #
  # | <<<<<<<<<<<<<<<<<<<<<<<<<<<  basePen  >>>>>>>>>>>>>>>>>>>>>>>>>>> | #
  # | ¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨ | #
  @basePen.GET
  def getBasePen(self, ) -> QPen:
    """Getter-function for basePen"""
    return self.__base_pen__

  @basePen.SET
  def setBasePen(self, other: Any) -> None:
    """Setter-function for basePen"""
    if isinstance(other, QPen):
      self.__base_pen__.setStyle(other.style())
      self.__base_pen__.setWidth(other.width())
      self.__base_pen__.setColor(other.color())
    elif isinstance(other, QColor):
      self.__base_pen__.setColor(other)
    elif isinstance(other, Color):
      qColor = QColor(other.red, other.green, other.blue, other.alpha)
      self.__base_pen__.setColor(qColor)
    elif isinstance(other, PenStyle):
      self.__base_pen__.setStyle(other)
    elif isinstance(other, int):
      self.__base_pen__.setWidth(other)
    elif isinstance(other, float):
      self.__base_pen__.setWidthF(other)

  @basePen.DEL
  def delBasePen(self, *_) -> Never:
    """Illegal deleter-function for basePen"""
    from worktoy.waitaminute import ProtectedAttributeError
    attName = 'basePen'
    insName = str(self)
    clsName = self.__class__
    raise ProtectedAttributeError(attName, insName, clsName)

  # | _________________________________________________________________ | #
  def __init__(self, *args, **kwargs) -> None:
    WorkToyClass.__init__(self, *args, **kwargs)
    self.__base_font__ = QFont()
    self.__base_brush__ = QBrush()
    self.__base_pen__ = QPen()
