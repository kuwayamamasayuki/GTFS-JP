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

class Trip(transitfeed.Trip):
  _FIELD_NAMES = transitfeed.Trip._FIELD_NAMES + [
    'jp_trip_desc', 'jp_trip_desc_symbol', 'jp_office_id'
    ]

  def __init__(self, headsign=None, service_period=None,
               route=None, trip_id=None, jp_office_id=None, field_dict=None):

    super(Trip, self).__init__()

    if jp_office_id is not None:
      field_dict['jp_office_id'] = jp_office_id
    self.__dict__.update(field_dict)


  def ValidateJpOfficeIdExistsInOfficeIdList(self, problems):
    if self._schedule:
      if self.jp_office_id and self.jp_office_id not in self._schedule.office_id:
        problems.InvalidValue('jp_office_id', self.jp_office_id)


  def ValidateAfterAdd(self, problems):
    pass
    #import pdb; pdb.set_trace()
    #self.ValidateJpOfficeIdExistsInOfficeIdList(problems)
