"""WorkSide - Tools - TextTools - ParagraphAttributes
This class provides the attributes for the paragraph class."""
#  MIT Licence
#  Copyright (c) 2023 Asger Jon Vistisen
from __future__ import annotations

from typing import Never

from worktoy.settings import maxLineLen
from worktoy.texttools import AbstractTextBlock
from worktoy.descriptors import Attribute


class ParagraphAttributes(AbstractTextBlock):
  """ WorkSide - Tools - TextTools - Paragraph The paragraph class
represents justified text. """
  leftMargin = Attribute('  #{| ')
  rightMargin = Attribute(' |}#  ')

  # | _________________________________________________________________ | #
  # | <<<<<<<<<<<<<<<<<<<<<<<<<<  leftMargin  >>>>>>>>>>>>>>>>>>>>>>>>> | #
  # | ¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨ | #
  @leftMargin.GET
  def getLeftMargin(self, ) -> str:
    """Getter-function for leftMargin"""
    return self.__left_margin__

  @leftMargin.SET
  def setLeftMargin(self, newValue: str) -> None:
    """Setter-function for leftMargin"""
    self.__left_margin__ = newValue

  @leftMargin.DEL
  def delLeftMargin(self, *_) -> Never:
    """Illegal deleter-function for leftMargin"""
    from worktoy.waitaminute import ProtectedAttributeError
    attName = 'leftMargin'
    insName = str(self)
    clsName = self.__class__
    raise ProtectedAttributeError(attName, insName, clsName)

  # | _________________________________________________________________ | #
  # | <<<<<<<<<<<<<<<<<<<<<<<<<  rightMargin  >>>>>>>>>>>>>>>>>>>>>>>>> | #
  # | ¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨ | #
  @rightMargin.GET
  def getRightMargin(self, ) -> str:
    """Getter-function for rightMargin"""
    return self.__right_margin__

  @rightMargin.SET
  def setRightMargin(self, newValue: str) -> None:
    """Setter-function for rightMargin"""
    self.__right_margin__ = newValue

  @rightMargin.DEL
  def delRightMargin(self, *_) -> Never:
    """Illegal deleter-function for rightMargin"""
    from worktoy.waitaminute import ProtectedAttributeError
    attName = 'rightMargin'
    insName = str(self)
    clsName = self.__class__
    raise ProtectedAttributeError(attName, insName, clsName)

  # | _________________________________________________________________ | #
  def __init__(self, *args, **kwargs) -> None:
    AbstractTextBlock.__init__(self, *args, **kwargs)
    self.__left_margin__ = '  #{| '
    self.__right_margin__ = ' |}#  '
