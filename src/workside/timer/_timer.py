"""WorkToy - Core - Timer
Subclass of QTimer collecting settings from the settings module"""
#  MIT Licence
#  Copyright (c) 2023 Asger Jon Vistisen
from __future__ import annotations

from PySide6.QtCore import QTimer, QObject
from icecream import ic

from workside.settings import Precise
from worktoy.descriptors import Attribute
from worktoy.worktoyclass import WorkToyClass

ic.configureOutput(includeContext=True)


class Timer(QTimer, WorkToyClass):
  """WorkToy - Core - Timer
  Subclass of QTimer collecting settings from the settings module."""

  name = Attribute()
  isFake = Attribute()
  fakeState = Attribute()

  def __init__(self, parent: QObject, interval: int, name: str = None,
               *args, **kwargs) -> None:
    WorkToyClass.__init__(self, *args, **kwargs)
    QTimer.__init__(self, parent)
    self.isFake = False
    self.fakeState = False
    self.name = self.maybe(name, 'lmao')
    if interval > 0:
      self.setTimerType(Precise)
      self.setInterval(interval)
      self.setSingleShot(True)
    else:
      self.isFake = True

  def isActive(self) -> bool:
    """Reimplementation allowing fake instances."""
    return self.fakeState if self.isFake else QTimer.isActive(self)

  def start(self) -> None:
    """Reimplementation allowing fake instances."""
    if self.isFake:
      self.fakeState = True
    else:
      return QTimer.start(self)

  def stop(self) -> None:
    """Reimplementation allowing fake instances."""
    if self.isFake:
      self.fakeState = False
    else:
      return QTimer.stop(self)

  def __bool__(self) -> bool:
    """Returns True if timer is active, otherwise it returns False."""
    if self.isFake and self.fakeState:
      return True
    if self.isFake:
      return False
    return QTimer.isActive(self)

  def __str__(self, ) -> str:
    """String representation"""
    return '%s: %s' % (self.__class__.__qualname__, self.name)

  def __repr__(self, ) -> str:
    """Code representation"""
    cls = self.__class__.__qualname__
    parent = self.parent().__class__.__qualname__
    interval = '%d' % self.interval()
    name = self.name
    return '%s(%s, %s, %s)' % (cls, parent, interval, name)
