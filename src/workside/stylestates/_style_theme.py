"""WorkSide - StyleStates - StyleTheme
  This class defines a centrally defined basic style definition shared by
  the widget classes. This allows for classes to implement their style
  relative to a central theme rather than absolute values.

  The central theme depends on a few centrally defined values:
   * 'baseColor'
   Defines the fundamental color of the theme. Widgets should generally
   use this color as fill.
   * 'contrastColor'
   Defines colors contrasting to the base color. Text drawn on the base
   color should generally be drawn with this color.
   * 'emphasisColorGrad'
   Defines how changes in contexts should be represented by color changes.
   * 'fontStyle'
   Specifies common style variables relevant for text. Themes can
   implement particular font families, ot just font commonalities. For
   example requiring monospaced fonts."""
#  MIT Licence
#  Copyright (c) 2023 Asger Jon Vistisen
from __future__ import annotations

from worktoy.descriptors import Field
from worktoy.worktoyclass import WorkToyClass


class StyleTheme(WorkToyClass):
  """WorkSide - StyleStates - StyleTheme
  This class defines a centrally defined basic style definition shared by
  the widget classes. This allows for classes to implement their style
  relative to a central theme rather than absolute values."""

  baseColor = Field()
  contrastColor = Field()
  emphasisColorGrad = Field()
  fontStyle = Field()

  def __init__(self, *args, **kwargs) -> None:
    WorkToyClass.__init__(self, *args, **kwargs)
    self.__base_color__ = None
    self.__contrast_color__ = None
