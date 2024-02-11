"""MinescriptWrapper - Entity
Class representation of entity data."""
#  MIT Licence
#  Copyright (c) 2023 Asger Jon Vistisen
from __future__ import annotations

from mineside.minescript_wrapper import PositionFieldF
from mineside.worktoy.base import DefaultClass
from mineside.worktoy.fields import StrAttribute, FloatAttribute


class Entity(DefaultClass):
  """MinescriptWrapper - Entity
  Class representation of entity data."""

  name = StrAttribute()
  position = PositionFieldF()
  velocity = PositionFieldF()
  health = FloatAttribute()
  nbt = None  # Not implemented

  def __init__(self, *args, **kwargs) -> None:
    DefaultClass.__init__(self, *args, **kwargs)
