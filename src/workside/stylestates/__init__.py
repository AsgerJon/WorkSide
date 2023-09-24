"""WorkSide - StateStyles
Abstract base class for style states that are state aware. This class defines
the supported states. This class provides a collection of common states.
The suggested use is to implement a system of style states from this class
adding support for each state and for each widget class required.

If the system requires more states than those provided here, the system
should begin with a subclass of this class implementing the required
states.

The structure of the state aware style states are illustrated below:

  - AbstractStyleStates (or subclass) -
  Bases class that defines the supported states. The default
  implementation derives states from the following flags:

  * Enabled
  * Hovered
  * Pressed
  * Toggled

Since each of the four flags have two states, 16 states are uniquely
identified. Style systems should define their styles in terms of these
flags. (Not all 16 are expected to be defined.)

  - ContextDimension -
  The StyleStates in WorkSide suggests that changes in style should
  associate to particular contexts. Widgets that share functionality,
  but differ in some higher abstraction should be represented by changes
  in styles.

  - ContextWidgets -
  Visual representations of values that vary with respect to some
  ContextDimension, but which have identical function, belong to the same
  group of widgets. Text based widgets may have identical functionalities,
  whilst representing values that vary across partition levels:
  For example,
    1.  Paragraph - Text in this category does not represent a partition
    level.
    2.  Paragraph Header - Representing the lowest partition level
    3.  Section Header - Representing the next partition level
    4.  Title - Representing the highest partition level
  The above categories all represent text. The StyleStates framework
  allows one widget class to define how a type of information is rendered,
  while allowing instances to scale on dimensions of higher abstraction.
  In the above example, this means one widget class: TextWidget, instead
  of ParagraphWidget, ParagraphHeader, etc.

  - ContextStyle and FreeStyle -
  A ContextStyle is a style depending on the context dimension. A
  FreeStyle is one that is context independent. For text based widgets,
  font size and font weight might represent partition levels. In contrast,
  font family and font color might remain constant across the context.

  - StyleTheme -
  This class defines a centrally defined basic style definition shared by
  the widget classes. This allows for classes to implement their style
  relative to a central theme rather than absolute values."""
#  MIT Licence
#  Copyright (c) 2023 Asger Jon Vistisen
from __future__ import annotations

from ._state import State
from ._abstract_style_state import AbstractStyleState
from ._style_state import StyleState
