"""MinescriptWrapper - Player
Class representation of player."""
#  MIT Licence
#  Copyright (c) 2023 Asger Jon Vistisen
from __future__ import annotations

from mineside.minescript_wrapper import PositionFieldF
from mineside.worktoy.base import DefaultClass
from mineside.worktoy.fields import StrAttribute, Flag, FloatAttribute


class Player(DefaultClass):
  """Class representation of player information."""
  name = StrAttribute()
  position = PositionFieldF()
  velocity = PositionFieldF()  # Values are implicitly per second.
  local = Flag()
  health = FloatAttribute
  nbt = None  # Not implemented

  def __init__(self, *args, **kwargs) -> None:
    DefaultClass.__init__(self, *args, **kwargs)
