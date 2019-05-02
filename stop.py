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

# Copyright (C) 2011 Google Inc.
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
import transitfeed.util as util
import transitfeed.problems as problems_module

class Stop(transitfeed.Stop):
  """Extension of transitfeed.Stop:
  - stop_timezoneを使用していないことの確認。
  - wheelchair_boardingを使用していないことの確認。
  """

  _FIELD_NAMES = transitfeed.Stop._FIELD_NAMES + ['platform_code']

  def ValidateStopTimezone(self, problems):
    if not util.IsEmpty(self.stop_timezone):
      problems.InvalidValue('stop_timezone', self.stop_timezone,
          reason='標準的なバス情報フォーマットではstop_timezoneは使用しません。（GTFS-JP仕様書(第２版) 2-2.参照）',
          type=problems_module.TYPE_WARNING)

  def ValidateWheelchairBoarding(self, problems):
    if not util.IsEmpty(self.wheelchair_boarding):
      problems.InvalidValue('wheelchair_boarding', self.wheelchair_boarding,
          reason='標準的なバス情報フォーマットではwheelchair_boardingは使用しません。（GTFS-JP仕様書(第２版) 2-2.参照）',
          type=problems_module.TYPE_WARNING)
