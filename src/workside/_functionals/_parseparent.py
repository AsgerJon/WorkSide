"""The parseParent function finds an instance of QWidget or a of a
subclass of QWidget from given arguments. Keyword arguments take precedent
over positional arguments. Any of the following keys may be used to
indicate the parent:
  - parent
  - main
  - window
Please note that the above keys are case insensitive.

"""
#  Copyright (c) 2023 Asger Jon Vistisen
#  MIT Licence
from __future__ import annotations

from PySide6.QtWidgets import QWidget
from worktoy.parsing import extractArg
from worktoy.stringtools import stringList


def parseParent(*args, **kwargs) -> QWidget:
  """Parses arguments to instance of QWidget"""
  parentKeys = stringList('parent, main, window')
  parent, args, kwargs = extractArg(QWidget, parentKeys, *args, **kwargs)
  if isinstance(parent, QWidget):
    return parent
