#  Copyright (c) 2023 Asger Jon Vistisen
#  MIT Licence
from __future__ import annotations

from PySide6.QtWidgets import (QMainWindow, QWidget, QVBoxLayout,
                               QGridLayout, \
  QLabel)

from workside.widgets._thematica import CustomButton


class CustomMainWindow(QMainWindow):
  """Main window class for the desktop application."""

  def __init__(self):
    super().__init__()
    self.setWindowTitle("Custom Buttons Demo")

    centralWidget = QWidget()
    self.setCentralWidget(centralWidget)

    layout = QVBoxLayout()
    centralWidget.setLayout(layout)

    gridLayout = QGridLayout()
    layout.addLayout(gridLayout)

    for i in range(3):
      for j in range(3):
        button = CustomButton()
        gridLayout.addWidget(button, i, j)

    layout.addWidget(QLabel("Below is a grid of custom buttons"))
