"""WorkSide - Widgets - TextWidgetVirtuals
Virtual class for TextWidget class. """
#  Copyright (c) 2023 Asger Jon Vistisen
#  MIT Licence
from __future__ import annotations

from typing import Never

from PySide6.QtCore import QRect, QSize
from PySide6.QtGui import QFont, QPen, QFontMetrics, QFontInfo, QPaintEvent
from icecream import ic

from workside.settings import Line, AbsSpacing, getBasePen
from workside.widgets import TextWidgetAttributes
from worktoy.descriptors import Attribute

ic.configureOutput(includeContext=True)


class TextWidgetVirtuals(TextWidgetAttributes):
  """ Attribute class for the TextWidget class """
  textFont = Attribute(QFont())
  textFontInfo = Attribute(QFontInfo(QFont()))
  metrics = Attribute(QFontMetrics(QFont()))
  boundRect = Attribute(QRect())
  boundSize = Attribute(QSize())
  fontPen = Attribute(QPen())

  # | _________________________________________________________________ | #
  # | <<<<<<<<<<<<<<<<<<<<<<<<<<<  textFont  >>>>>>>>>>>>>>>>>>>>>>>>>> | #
  # | ¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨ | #
  @textFont.GET
  def getTextFont(self, ) -> QFont:
    """Getter-function for textFont"""
    textFont = QFont()
    textFont.setFamily(self.fontFamily)
    textFont.setPointSize(self.fontSize)
    textFont.setWeight(self.fontWeight)
    textFont.setCapitalization(self.fontCap)
    textFont.setLetterSpacing(AbsSpacing, self.letterSpacing)
    textFont.setWordSpacing(self.wordSpacing)
    return textFont

  @textFont.SET
  def setTextFont(self, newFont: QFont, *_) -> Never:
    """Illegal setter-function for textFont"""
    self.fontFamily = newFont.family()
    self.fontSize = newFont.pointSize()
    self.fontWeight = newFont.weight()
    self.fontCap = newFont.capitalization()
    self.letterSpacing = newFont.letterSpacing()
    self.wordSpacing = newFont.wordSpacing()

  @textFont.DEL
  def delTextFont(self, *_) -> Never:
    """Illegal deleter-function for textFont"""
    from worktoy.waitaminute import ProtectedAttributeError
    attName = 'textFont'
    insName = str(self)
    clsName = self.__class__
    raise ProtectedAttributeError(attName, insName, clsName)

  # | _________________________________________________________________ | #
  # | <<<<<<<<<<<<<<<<<<<<<<<<<  textFontInfo  >>>>>>>>>>>>>>>>>>>>>>>> | #
  # | ¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨ | #
  @textFontInfo.GET
  def getTextFontInfo(self, ) -> QFontInfo:
    """Getter-function for textFontInfo"""
    return QFontInfo(self.textFont)

  @textFontInfo.SET
  def setTextFontInfo(self, *_) -> Never:
    """Illegal setter-function for textFontInfo"""
    from worktoy.waitaminute import ReadOnlyException
    attName = 'textFontInfo'
    insName = str(self)
    clsName = self.__class__
    raise ReadOnlyException(attName, insName, clsName)

  @textFontInfo.DEL
  def delTextFontInfo(self, *_) -> Never:
    """Illegal deleter-function for textFontInfo"""
    from worktoy.waitaminute import ProtectedAttributeError
    attName = 'textFontInfo'
    insName = str(self)
    clsName = self.__class__
    raise ProtectedAttributeError(attName, insName, clsName)

  # | _________________________________________________________________ | #
  # | <<<<<<<<<<<<<<<<<<<<<<<<<<<  metrics  >>>>>>>>>>>>>>>>>>>>>>>>>>> | #
  # | ¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨ | #
  @metrics.GET
  def getMetrics(self, ) -> QFontMetrics:
    """Getter-function for metrics"""
    return QFontMetrics(self.textFont)

  @metrics.SET
  def setMetrics(self, *_) -> Never:
    """Illegal setter-function for metrics"""
    from worktoy.waitaminute import ReadOnlyException
    attName = 'metrics'
    insName = str(self)
    clsName = self.__class__
    raise ReadOnlyException(attName, insName, clsName)

  @metrics.DEL
  def delMetrics(self, *_) -> Never:
    """Illegal deleter-function for metrics"""
    from worktoy.waitaminute import ProtectedAttributeError
    attName = 'metrics'
    insName = str(self)
    clsName = self.__class__
    raise ProtectedAttributeError(attName, insName, clsName)

  # | _________________________________________________________________ | #
  # | <<<<<<<<<<<<<<<<<<<<<<<<<<  boundRect  >>>>>>>>>>>>>>>>>>>>>>>>>> | #
  # | ¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨ | #
  @boundRect.GET
  def getBoundRect(self, ) -> QRect:
    """Getter-function for boundRect"""
    return self.metrics.tightBoundingRect(self.currentText)

  @boundRect.SET
  def setBoundRect(self, *_) -> Never:
    """Illegal setter-function for boundRect"""
    from worktoy.waitaminute import ReadOnlyException
    attName = 'boundRect'
    insName = str(self)
    clsName = self.__class__
    raise ReadOnlyException(attName, insName, clsName)

  @boundRect.DEL
  def delBoundRect(self, *_) -> Never:
    """Illegal deleter-function for boundRect"""
    from worktoy.waitaminute import ProtectedAttributeError
    attName = 'boundRect'
    insName = str(self)
    clsName = self.__class__
    raise ProtectedAttributeError(attName, insName, clsName)

  # | _________________________________________________________________ | #
  # | <<<<<<<<<<<<<<<<<<<<<<<<<<  boundSize  >>>>>>>>>>>>>>>>>>>>>>>>>> | #
  # | ¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨ | #
  @boundSize.GET
  def getBoundSize(self, ) -> QSize:
    """Getter-function for boundSize"""
    return self.boundRect.size()

  @boundSize.SET
  def setBoundSize(self, *_) -> Never:
    """Illegal setter-function for boundSize"""
    from worktoy.waitaminute import ReadOnlyException
    attName = 'boundSize'
    insName = str(self)
    clsName = self.__class__
    raise ReadOnlyException(attName, insName, clsName)

  @boundSize.DEL
  def delBoundSize(self, *_) -> Never:
    """Illegal deleter-function for boundSize"""
    from worktoy.waitaminute import ProtectedAttributeError
    attName = 'boundSize'
    insName = str(self)
    clsName = self.__class__
    raise ProtectedAttributeError(attName, insName, clsName)

  # | _________________________________________________________________ | #
  # | <<<<<<<<<<<<<<<<<<<<<<<<<<<  fontPen  >>>>>>>>>>>>>>>>>>>>>>>>>>> | #
  # | ¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨ | #
  @fontPen.GET
  def getFontPen(self, ) -> QPen:
    """Getter-function for fontPen"""
    pen = getBasePen()
    pen.setStyle(Line)
    pen.setWidth(1)
    pen.setColor(self.fontColor.Q)
    return pen

  @fontPen.SET
  def setFontPen(self, *_) -> Never:
    """Illegal setter-function for fontPen"""
    from worktoy.waitaminute import ReadOnlyException
    attName = 'fontPen'
    insName = str(self)
    clsName = self.__class__
    raise ReadOnlyException(attName, insName, clsName)

  @fontPen.DEL
  def delFontPen(self, *_) -> Never:
    """Illegal deleter-function for fontPen"""
    from worktoy.waitaminute import ProtectedAttributeError
    attName = 'fontPen'
    insName = str(self)
    clsName = self.__class__
    raise ProtectedAttributeError(attName, insName, clsName)

  # | _________________________________________________________________ | #
  def __init__(self, *args, **kwargs) -> None:
    TextWidgetAttributes.__init__(self, *args, **kwargs)
    self.setMouseTracking(True)
    self.__text_font__ = QFont()
    self.__text_font_info__ = QFontInfo(QFont())
    self.__metrics__ = QFontMetrics(QFont())
    self.__bound_size__ = QSize()
    self.__bound_rect__ = QRect()
    self.__font_pen__ = QPen()

  def paintEvent(self, event: QPaintEvent) -> None:
    """Adds state dependent fill to the inner rectangle."""
    TextWidgetAttributes.paintEvent(self, event)
