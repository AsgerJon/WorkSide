"""WorkSide - Tools - AbstractFactory
Baseclass for factories creating instances of painter tools."""
#  Copyright (c) 2023 Asger Jon Vistisen
#  MIT Licence
from __future__ import annotations

from worktoy.worktoyclass import WorkToyClass


class AbstractFactory(WorkToyClass):
  """WorkSide - Tools - AbstractFactory
  Baseclass for factories creating instances of painter tools."""

  def __init__(self, *args, **kwargs) -> None:
    WorkToyClass.__init__(self, *args, **kwargs)
