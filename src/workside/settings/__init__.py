"""WorkSide - Settings"""
#  MIT Licence
#  Copyright (c) 2023 Asger Jon Vistisen
from __future__ import annotations

from ._timer_settings import *
from ._keyboard import *
from ._brush_settings import *
from ._pen_settings import *
from ._color import *
from ._keyboard import *
from ._event_settings import *
from ._font_settings import *
from ._mouse_settings import *
from ._mono_color_mapping import MonoColorMapping
from ._font_families import FontFamilies
from ._mouse_record import MouseRecord

singlePreReleaseTimeLimit = 250
singlePressHoldingTimeLimit = 350
singlePostReleaseTimeLimit = 200
doublePreReleaseTimeLimit = 50
doublePostReleaseTimeLimit = 25
