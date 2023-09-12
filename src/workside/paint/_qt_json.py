"""WorkSide - Paint - QtJson
Saves and loads Qt Enum instances to json."""
#  Copyright (c) 2023 Asger Jon Vistisen
#  MIT Licence
from __future__ import annotations

from worktoy.worktoyclass import WorkToyClass


class QtJson(WorkToyClass):
  """WorkSide - Paint - QtJson
  Saves and loads Qt Enum instances to json."""

  def __init__(self, *args, **kwargs) -> None:
    WorkToyClass.__init__(self, *args, **kwargs)
    self._wrappedType = None
 