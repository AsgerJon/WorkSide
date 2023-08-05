"""ArgumentError should be invoked where required arguments are missing."""
#  Copyright (c) 2023 Asger Jon Vistisen
#  MIT Licence
from __future__ import annotations

from icecream import ic
from worktoy.parsing import extractArg
from worktoy.stringtools import stringList

ic.configureOutput(includeContext=True)


class ArgumentError(Exception):
  """ArgumentError should be invoked when a particular argument is
  missing."""

  def __init__(self, *args, **kwargs) -> None:
    typeKeys = stringList('type_, class, cls')
    argType, args, kwargs = extractArg(type, typeKeys, *args, **kwargs)
    nameKeys = stringList('argName, name, variable')
    argName, args, kwargs = extractArg(type, nameKeys, *args, **kwargs)
    msg = """Unable to obtain argument named %s of type %s!"""
    super().__init__(msg % (argName, argType))
