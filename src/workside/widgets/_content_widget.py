"""WorkSide - Widgets - ContentWidget
This is the widget actually having content."""
#  Copyright (c) 2023 Asger Jon Vistisen
#  MIT Licence
from __future__ import annotations

from worktoy.descriptors import Field, StrAttribute

from workside.widgets import CoreWidget


class ContentWidget(CoreWidget):
  """WorkSide - Widgets - ContentWidget
  This is the widget actually having content."""

  text = Field()
  textState = StrAttribute('legend')

  def __init__(self, *args, **kwargs) -> None:
    CoreWidget.__init__(self, *args, **kwargs)

  @text.getter
  def getText(self) -> str:
    """Getter-function for the text"""
    return 'x: %.0f | y: %.0f' % (self.mouseX, self.mouseY)
