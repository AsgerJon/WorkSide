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
