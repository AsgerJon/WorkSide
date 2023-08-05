"""LayoutWindow"""
#  Copyright (c) 2023 Asger Jon Vistisen
#  MIT Licence
from __future__ import annotations

from PySide6.QtGui import QTextCursor
from PySide6.QtWidgets import QWidget
from icecream import ic

from workside.windows import BaseWindow

wordStart = QTextCursor.MoveOperation.StartOfWord
wordEnd = QTextCursor.MoveOperation.EndOfWord
move = QTextCursor.MoveMode.MoveAnchor
mark = QTextCursor.MoveMode.KeepAnchor

ic.configureOutput(includeContext=True)


class LayoutWindow(BaseWindow):
  """A subclass of BaseWindow that provides layouts and widgets for a simple
  word processing application.

  This class adds a vertical layout to the QMainWindow and populates it
  with a QLabel, a QLineEdit, and a QTextEdit.
  The QLabel displays the current file name, the QLineEdit is used for
  entering search terms, and the QTextEdit is used for editing text."""

  def __init__(self, parent: QWidget = None) -> None:
    BaseWindow.__init__(self, parent)