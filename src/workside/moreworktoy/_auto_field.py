"""MoreWorkToy - AutoField
This class can hold CoreFields """
#  Copyright (c) 2023 Asger Jon Vistisen
#  MIT Licence
from __future__ import annotations

import json
from typing import Any

from worktoy.worktoyclass import WorkToyClass

from workside.moreworktoy import CoreField


class AutoField(WorkToyClass):
  """MoreWorkToy - AutoField
  This class can hold CoreFields """

  RED = CoreField()
  GREEN = CoreField()
  BLUE = CoreField()
  ALPHA = CoreField()

  def encode(self, obj: Any) -> str:
    """ENCODES"""
    out = {}
    coreFields = getattr(self.__class__, '__core_fields__', {})
    for fieldName, field in coreFields.items():
      out |= {fieldName: field.encode(obj)}
    return json.dumps(out)
