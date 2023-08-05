"""CircularReferenceError should be raised instead of waiting for the
interpreter to raise a RecursionError itself."""
#  Copyright (c) 2023 Asger Jon Vistisen
#  MIT Licence
from __future__ import annotations

from moreworktoy.waitaminute import ArgumentError


class CircularReferenceError(Exception):
  """CircularReferenceError should be raised instead of waiting for the
  interpreter to raise a RecursionError itself. The constructor expects a
  type and a string indicating the expected type and name of the variable
  being referred to respectively."""

  def __init__(self, type_: type = None, name: str = None) -> None:
    if type_ is None:
      raise ArgumentError(type_=type, name='type_')
    if name is None:
      raise ArgumentError(type_=str, name='name')
    msg = """Attempt at referencing variable %s of type %s led to pattern 
    of infinite recursion!""" % (name, type_)
    super().__init__(msg)
