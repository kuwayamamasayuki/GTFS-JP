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

from transitfeed.problems import default_problem_reporter
from transitfeed import util
import extension_util
import transitfeed

class Route(transitfeed.Route):
  """Represents a single route."""

  _REQUIRED_FIELD_NAMES = transitfeed.Route._REQUIRED_FIELD_NAMES + ['agency_id']
  _FIELD_NAMES = transitfeed.Route._FIELD_NAMES + ['jp_parent_route_id']

  def __init__(self, short_name=None, long_name=None, route_type=None,
               route_id=None, agency_id=None, jp_parent_route_id=None, field_dict=None):

    super(Route, self).__init__()

    if jp_parent_route_id is not None:
      field_dict['jp_parent_route_id'] = jp_parent_route_id
    self.__dict__.update(field_dict)

  def ValidateAgencyIdIsPresent(self, problems):
    if util.IsEmpty(self.agency_id):
      problems.MissingValue('agency_id')
  

  def ValidateRouteType(self, problems):
    if self.route_type == '3':
      return True
    problems.InvalidValue('route_type', self.route_type, 'route_typeは「3」固定です。')
    return False
  

  def ValidateBeforeAdd(self, problems):
    self.ValidateAgencyIdIsPresent(problems)
    self.ValidateRouteType(problems)
    return super(Route, self).ValidateBeforeAdd(problems)

