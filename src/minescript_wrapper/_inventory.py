"""MinescriptWrapper - Inventory
Class representation of inventory."""
#  MIT Licence
#  Copyright (c) 2023 Asger Jon Vistisen
from __future__ import annotations

from mineside.minescript_wrapper import ItemField, Item
from mineside.worktoy.base import DefaultClass


class Inventory(DefaultClass):
  """MinescriptWrapper - Inventory
  Class representation of inventory."""

  def __init__(self, *args, **kwargs) -> None:
    DefaultClass.__init__(self, *args, **kwargs)
    self.__current_index__ = 0
    self._items = [Item.getNullItem() for _ in range(27)]
    self._iterContents = None

  def _resetIterContents(self) -> None:
    self._iterContents = [item for item in self._items]

  def _getIterContents(self) -> list[Item]:
    return self._iterContents

  def _getItems(self) -> list[Item]:
    return self._items

  def __iter__(self) -> Inventory:
    """Implementation of iteration."""
    self._resetIterContents()
    return self

  def __next__(self) -> Item:
    """Implementation of iteration."""
    try:
      return self._getIterContents().pop(0)
    except IndexError:
      raise StopIteration

  def __setitem__(self, key: int, value: Item) -> None:
    if not isinstance(key, int):
      raise KeyError
    if -1 < key < 27:
      self._items[key] = value
    if key < -1:
      return self.__setitem__(key + 27, value)
    if key > 26:
      raise IndexError

  def __getitem__(self, key: int) -> Item:
    if not isinstance(key, int):
      raise KeyError
    if -1 < key < 27:
      return self._items[key]
    if key < -1:
      return self.__getitem__(key + 27)
    if key > 26:
      raise IndexError
