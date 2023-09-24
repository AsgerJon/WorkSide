"""WorkSide - Windows - Actions
This package provides custom actions."""
#  MIT Licence
#  Copyright (c) 2023 Asger Jon Vistisen
from __future__ import annotations

from ._abstract_action import AbstractAction
from ._new_action import NewAction
from ._open_action import OpenAction
from ._save_action import SaveAction
from ._save_as_action import SaveAsAction

from ._cut_action import CutAction
from ._copy_action import CopyAction
from ._paste_action import PasteAction
from ._preferences_action import PreferencesAction

from ._about_qt_action import AboutQtAction
from ._about_workside_action import AboutWorkSideAction

from ._debug_action import DebugAction
