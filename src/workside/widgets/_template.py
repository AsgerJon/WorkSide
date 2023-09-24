"""WorkToy - Core - Template 
Code writing assistant"""
#  MIT Licence
#  Copyright (c) 2023 Asger Jon Vistisen
from __future__ import annotations

from typing import Any

from workside.widgets import AbstractWidget
from worktoy.descriptors import Attribute
from worktoy.worktoyclass import WorkToyClass


class Template(WorkToyClass):
  """The template class allows separate widgets to share attribute values.
  Define a list of named attributes and a source widget instance. Then
  call the template instance on the target widget the value of each named
  attribute is copied from the source widget to the target widget."""

  source = Attribute()
  namedAttributes = Attribute()

  def __init__(self, *args, **kwargs) -> None:
    WorkToyClass.__init__(self, *args, **kwargs)
    self.namedAttributes = self.maybeTypes(str, *args)
    src = self.maybeType(AbstractWidget, *args)
    if isinstance(src, AbstractWidget):
      self.source = src

  def __call__(self, target: Any) -> Any:
    """Sets attributes on a target instance if target is an instance of
    AbstractWidget. If target is a subclass of AbstractWidget, the target
    is set as the source. """
    if isinstance(target, type):
      if issubclass(target, AbstractWidget):
        self.source = target
    if isinstance(target, AbstractWidget):
      for name in self.namedAttributes:
        setattr(target, name, getattr(self.source, name))
    return target

  def addName(self, name: str) -> None:
    """Adds name to list of tracked attributes"""
    self.namedAttributes.append(name)

  def updateWidget(self, target: AbstractWidget) -> AbstractWidget:
    """Updates and returns the given widget."""
    for name in self.namedAttributes:
      setattr(target, name, getattr(self.source, name))
    return target
