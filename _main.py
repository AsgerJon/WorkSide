"""Main Tester Script"""
#  Copyright (c) 2023 Asger Jon Vistisen
#  MIT Licence
from __future__ import annotations

import os
import sys
import time
from typing import NoReturn, Never, Any

from PySide6.QtWidgets import QApplication
from icecream import ic
from pyperclip import copy
from moreworktoy.descriptors import AttributeClass
from worktoy.worktoyclass import WorkToyClass

from workside.widgets import AbstractButtonTimer
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

  documentation = fuck.monoSpace("""Defines the area of the widget 
  considered by the mouse""")
  cunt = AttributeClass()
  cunt.setCls('AbstractMouseRegionProperties')
  cunt.setDoc(documentation)
  cunt.setParent(AbstractButtonTimer)

  cunt.addAttribute('mousePoint', 'QPointF(0, 0)', 'QPointF()')
  cunt.addAttribute('underMouse', 'False', 'bool')

  cunt.addAttribute('mousePX', '0.0', 'float')
  cunt.addAttribute('mousePY', '0.0', 'float')
  cunt.addAttribute('mouseVX', '0.0', 'float')
  cunt.addAttribute('mouseVY', '0.0', 'float')
  cunt.addAttribute('mouseAX', '0.0', 'float')
  cunt.addAttribute('mouseAY', '0.0', 'float')

  cunt.addAttribute('mouseState', 'NoBtn', 'Mouse')
  cunt.addAttribute('mouseRegion', 'QRectF()', 'QRectF')
  cunt.addAttribute('mouseLeft', '0', 'float', )
  cunt.addAttribute('mouseTop', '0', 'float', )
  cunt.addAttribute('mouseRight', '0', 'float', )
  cunt.addAttribute('mouseBottom', '0', 'float', )

  copy(cunt.buildCode())


def tester02() -> None:
  """LMAO"""

  app = QApplication(sys.argv)
  window = MainWindow()
  window.show()
  sys.exit(app.exec())


if __name__ == '__main__':
  print(77 * '_')
  print(time.ctime())
  tester02()
  print(77 * '¨')
