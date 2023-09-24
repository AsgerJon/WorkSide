"""WorkToy - Core - MouseRecord
Code writing assistant"""
#  MIT Licence
#  Copyright (c) 2023 Asger Jon Vistisen
from __future__ import annotations

import time

from PySide6.QtCore import QEvent, QPointF, QPoint

from workside.settings import Mouse, EvType, NoBtn
from worktoy.descriptors import Attribute
from worktoy.worktoyclass import WorkToyClass


class MouseRecord(WorkToyClass):
  """Simplified wrapper on QMouseEvent. This provides a persistent record
  of a mouse event. Instances of QEvent and subclasses of it will get
  garbage collected even in certain situations where they are assigned to
  a persistent variable."""

  button = Attribute()
  mouseX = Attribute()
  mouseY = Attribute()
  timeStamp = Attribute()

  def parse(self, *args, **kwargs) -> dict:
    """Parse overload
    x: float, y: float, t: float, b: Mouse, e: EvType
    """
    keys = [k for k, v in kwargs.items()]
    types = [v for k, v in kwargs.items()]
    if len(args) < len(types):
      raise TypeError
    out = {}
    args = [*args, ]
    for key, arg, cls in zip(keys, args, types):
      if isinstance(arg, cls):
        out |= {key: arg}
      else:
        raise TypeError
    return out

  def __init__(self, *args, **kwargs) -> None:
    WorkToyClass.__init__(self, *args, **kwargs)
    pointF = self.maybeType(QPointF, *args)
    point = self.maybeType(QPoint, *args)
    timeStamp = self.maybeType(float, *args)
    button = self.maybeType(Mouse, *args)
    p = self.maybe(pointF, point, QPointF(0, 0))
    t = self.maybe(timeStamp, time.time())
    b = self.maybe(button, NoBtn)
    self.mouseX, self.mouseY = p.x, p.y
    self.timeStamp, self.button = t, b
