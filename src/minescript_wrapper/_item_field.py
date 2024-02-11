"""MinescriptWrapper - ItemField
Item valued descriptor implementation."""
#  MIT Licence
#  Copyright (c) 2023 Asger Jon Vistisen
from __future__ import annotations

from mineside.minescript_wrapper import Item
from mineside.worktoy.fields import TypedAttribute, IntAttribute


class ItemField(TypedAttribute):
  """MinescriptWrapper - ItemField
  Item valued descriptor implementation."""

  slotId = IntAttribute(-1)

  def __init__(self, *args, **kwargs) -> None:
    TypedAttribute.__init__(self, *args, **kwargs)
    self._defaultValue = Item.getNullItem()
    self._type = Item
    index = kwargs.get('index', None)
    if isinstance(index, int):
      self.slotId = index
