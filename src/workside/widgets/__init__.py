"""WorkSide - Widgets
Subclasses of QWidget"""
#  Copyright (c) 2023 Asger Jon Vistisen
#  MIT Licence
from __future__ import annotations

from ._abstract_widget_attributes import AbstractWidgetAttributes
from ._abstract_widget_virtuals import AbstractWidgetVirtuals
from ._abstract_widget import AbstractWidget
from ._template import Template
from ._spacer_widgets import HorizontalSpacer, VerticalSpacer, DoubleSpacer
from ._test_widget import TestWidget
from ._text_widget_attributes import TextWidgetAttributes
from ._text_widget_virtuals import TextWidgetVirtuals
from ._text_widget import TextWidget
from ._abstract_button_timer import AbstractButtonTimer
from ._abstract_button import AbstractButton
