"""WorkToy - Core - TimerSettings
Code writing assistant"""
#  MIT Licence
#  Copyright (c) 2023 Asger Jon Vistisen
from __future__ import annotations

from PySide6.QtCore import Qt

TimerType = Qt.TimerType
VeryCoarse = TimerType.VeryCoarseTimer
Coarse = TimerType.CoarseTimer
Precise = TimerType.PreciseTimer

singleClickTimerLimit = 500
pressHoldTimerLimit = 500
singleClickWaitingLimit = 500
doubleClickTimerLimit = 500
doubleClickWaitingLimit = 500

WaitForSingleReleaseLimit = 300
WaitForDoubleCLickLimit = 200
WaitForSingleHoldLimit = 300
WaitForDoubleReleaseLimit = 300
WaitForDoubleHoldLimit = 300
WaitForTripleReleaseLimit = 300
WaitForTripleClickLimit = 200
