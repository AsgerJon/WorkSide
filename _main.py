"""Main Tester Script"""
#  Copyright (c) 2023 Asger Jon Vistisen
#  MIT Licence
from __future__ import annotations

import os
import sys
import time
from typing import NoReturn, Never, Any

from PySide6.QtCore import QRect, QRectF, QPointF
from PySide6.QtWidgets import QApplication
from icecream import ic
from pyperclip import copy
from worktoy.descriptors import AttributeClass
from worktoy.worktoyclass import WorkToyClass

from moreworktoy import FieldClass
from workside.settings import Mouse, NoBtn
from workside.widgets import AbstractWidget
from workside.windows import MainWindow


def Remainder(val: Any) -> int:
  """yolo"""
  return int((val * 10 ** 12) // (10 ** 12))


def tester00() -> NoReturn:
  """Hello World!"""
  stuff = ['hello world', os, sys, Never, Any, ]
  stuff = [*stuff, time, ]
  for item in stuff:
    ic(item)


def tester01() -> None:
  """LMAO"""
  fuck = WorkToyClass()

  documentation = fuck.stringList("""Defines the area of the widget 
  considered by the mouse""")
  cunt = FieldClass('AbstractMouseRegion', documentation,
                    parent=AbstractWidget)

  cunt.addField('mousePoint', 'QPointF()', 2)
  cunt.addField('underMouse', 'False', 2)

  cunt.addField('mousePX', 0, 2)
  cunt.addField('mousePY', 0, 2)
  cunt.addField('mouseVX', 0, 2)
  cunt.addField('mouseVY', 0, 2)
  cunt.addField('mouseAX', 0, 2)
  cunt.addField('mouseAY', 0, 2)

  cunt.addField('mouseState', 'NoBtn', 2)
  cunt.addField('mouseRegion', 'QRectF()', 2)
  cunt.addField('mouseLeft', 0, 2)
  cunt.addField('mouseTop', 0, 2)
  cunt.addField('mouseRight', 0, 2)
  cunt.addField('mouseBottom', 0, 2)

  copy(cunt.buildClass())


def tester02() -> None:
  """LMAO"""

  app = QApplication(sys.argv)
  window = MainWindow()
  window.show()
  sys.exit(app.exec())


if __name__ == '__main__':
  print(77 * '_')
  print(time.ctime())
  tester01()
  print(77 * '¨')
