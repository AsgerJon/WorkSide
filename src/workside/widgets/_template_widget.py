"""WorkToy - Core - AbstractTemplateWidget
Code writing assistant"""
#  MIT Licence
#  Copyright (c) 2023 Asger Jon Vistisen
from __future__ import annotations

from workside.widgets import AbstractWidget
from worktoy.descriptors import Attribute


class AbstractTemplateWidget(AbstractWidget):
  """The template widget should define attributes that are to be shared by 
  a group of widgets. Grouped widgets should share template widget created
  on their most specific common parent. Thus, general widgets such as
  TextWidget should implement a templated version. """

  sharedAttributes = Attribute([])

  @sharedAttributes.GET
  def getSharedAttributes(self) -> list:
    """Getter-function for shared attributes"""
    return self.__shared_attributes__

  def __init__(self, *args, **kwargs) -> None:
    AbstractWidget.__init__(self, *args, **kwargs)
    self.__shared_attributes__ = []
