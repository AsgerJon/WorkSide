"""WorkToy - Core - AbstractTemplate
Code writing assistant"""
#  Copyright (c) 2023 Asger Jon Vistisen
#  MIT Licence
from __future__ import annotations

from abc import abstractmethod
from worktoy.worktoyclass import WorkToyClass


class AbstractTemplate(WorkToyClass):
  """WorkToy - Core - AbstractTemplate
  Code writing assistant"""

  def __init__(self, *args, **kwargs) -> None:
    WorkToyClass.__init__(self, *args, **kwargs)

  @abstractmethod
  def getTags(self) -> dict[str, str]:
    """Getter-function for the dictionary mapping tags to replacements"""

  def render(self, base: str) -> str:
    """Applies tags to base"""
    out = base
    for key, val in self.getTags().items():
      if isinstance(val, str):
        out = out.replace(key, val)
      elif isinstance(val, type):
        out = out.replace(key, val.__qualname__)
      else:
        out = out.replace(key, str(val))

    return out
