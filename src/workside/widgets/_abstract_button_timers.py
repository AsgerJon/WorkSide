"""WorkToy - Core - AbstractButtonTimers
Class providing the timers for use by the buttons"""
#  MIT Licence
#  Copyright (c) 2023 Asger Jon Vistisen
from __future__ import annotations

from workside.widgets import AbstractWidget


class AbstractButtonTimers(AbstractWidget):
  """Class providing the timers for use by the buttons."""

  def __init__(self, *args, **kwargs) -> None:
    AbstractWidget.__init__(self, *args, **kwargs)
