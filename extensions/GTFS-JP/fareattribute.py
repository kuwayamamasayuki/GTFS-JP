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
from transitfeed import util


class FareAttribute(transitfeed.FareAttribute):
  """Extension of transitfeed.FareAttribute:
  - currency_typeが「JPY」であることの確認を行う。
  """

  def ValidateCurrencyType(self, problems):
    if util.IsEmpty(self.currency_type):
      problems.MissingValue("currency_type")
    elif self.currency_type != 'JPY':
      problems.InvalidValue("currency_type", self.currency_type,
      'currency_typeは「JPY」である必要があります。（GTFS-JP仕様書(第２版) 2-8.参照）')
