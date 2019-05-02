#!/usr/bin/python2.5
# coding: utf_8

# Copyright (C) 2019 KUWAYAMA, Masayuki
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Copyright (C) 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import transitfeed

from transitfeed import problems as problems_module
from transitfeed import util

class Shape(transitfeed.Shape):
  """This class represents a geographic shape that corresponds to the route
  taken by one or more Trips."""

  def ValidateBeforeAdd(self, problems):
    if not util.IsEmpty(self.shape_dist_traveled):
      problems.InvalidValue("shape_dist_traveled", self.shape_dist_traveled,
      '標準的なバス情報フォーマットではshape_dist_traveledは使用しません。（GTFS-JP仕様書(第２版) 2-9.参照）')
    return True
