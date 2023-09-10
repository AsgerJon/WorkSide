"""WorkSide - Draw - ColorField
Field descriptor for the color value."""
#  Copyright (c) 2023 Asger Jon Vistisen
#  MIT Licence
from __future__ import annotations

from workside.draw import Color
from workside.widgets import CoreWidget
from worktoy.worktoyclass import WorkToyClass
from worktoy.descriptors import StrAttribute


class ColorField(WorkToyClass):
  """WorkSide - Draw - ColorField
  Field descriptor for the color value."""

  fieldName = StrAttribute()

  def __init__(self, *args, **kwargs) -> None:
    WorkToyClass.__init__(self, *args, **kwargs)
    self._defaultValue = Color.getDefaultInstance()
    self._type = Color
    self._fieldOwner = None

  def __set_name__(self, cls: type, name: str) -> None:
    self.fieldName = name
    self.setFieldOwner(cls)

  def setFieldOwner(self, cls: type) -> None:
    """Setter-function for the field owner."""
    self._fieldOwner = cls

  def getFieldOwner(self, ) -> type:
    """Getter-function for the field owner."""
    return self._fieldOwner

  def __get__(self, obj: CoreWidget, cls: type) -> Color:
    """Getter."""

  def __set__(self, obj: CoreWidget, newColor: Color) -> None:
    """Does not replace the color, but updates its values."""
