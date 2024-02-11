"""MinescriptWrapper - World
Class representation of world properties."""
#  Copyright (c) 2023 Asger Jon Vistisen
#  MIT Licence
from __future__ import annotations

from worktoy.descriptors import Attribute
from worktoy.worktoyclass import WorkToyClass


class World(WorkToyClass):
  """MinescriptWrapper - World
  Class representation of world properties."""

  thunder = Attribute()
  raining = Attribute()

  hardCore = Attribute()
  spawn = Attribute()
  dayTicks = Attribute(0)
  difficulty = Attribute()
  name = Attribute()
  address = Attribute()
