"""MinescriptWrapper - Item
Class representation of item."""
#  MIT Licence
#  Copyright (c) 2023 Asger Jon Vistisen
from __future__ import annotations

from mineside.worktoy.base import DefaultClass
from mineside.worktoy.fields import StrAttribute, IntAttribute


class Item(DefaultClass):
  """Class representation of contents of an inventory slot."""

  name = StrAttribute()
  count = IntAttribute()
  nbt = StrAttribute()

  @classmethod
  def getNullItem(cls) -> Item:
    """Creates the special null item"""
    nullItem = cls()
    nullItem.count = 0
    nullItem.nbt = ''
    nullItem.name = 'NULL'
    return nullItem

  def __init__(self, *args, **kwargs) -> None:
    DefaultClass.__init__(self, *args, **kwargs)
    nameKwarg = self.maybeKey('name', 'item', str, **kwargs)
    countKwarg = self.maybeKey('count', 'amount', int, **kwargs)
    nbtKwarg = self.maybeKey('nbt', str, **kwargs)
    strArgs = (*self.maybeTypes(str, *args), None, None)
    nameArg, nbtArg = strArgs[:2]
    countArg = self.maybeType(int, *args)
    nameDefault, countDefault, nbtDefault = '', 0, ''
    self.name = self.maybe(nameKwarg, nameArg, nameDefault)
    self.count = self.maybe(countKwarg, countArg, countDefault)
    self.nbt = self.maybe(nbtKwarg, nbtArg, nbtDefault)
