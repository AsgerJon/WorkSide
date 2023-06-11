"""The styles package provides centrally defined style settings."""
#  Copyright (c) 2023 Asger Jon Vistisen
#  MIT Licence
from __future__ import annotations

from icecream import ic

ic.configureOutput(includeContext=True)

from ._basestyle import BaseStyle
from ._fontfamily import Family
from ._styleinstances import backgroundStyle, labelStyle, headerStyle
