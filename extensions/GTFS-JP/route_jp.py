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

class Route_jp(transitfeed.Route):
  """Extension of transitfeed.Route:
  """

  _REQUIRED_FIELD_NAMES = ['route_id']
  _FIELD_NAMES = _REQUIRED_FIELD_NAMES + ['route_update_date', 'origin_stop', 'via_stop', 
                                          'destination_stop']

  def __init__(self, route_id=None, route_update_date=None, origin_stop=None, via_stop=None, 
               destination_stop=None, field_dict=None, **kwargs):
    """Initialize a new Route_jp object.

    Args:
      field_dict: A dictionary mapping attribute name to unicode string
      route_id: a string, ignored when field_dict is present
      route_update_date: a string, ignored when field_dict is present
      origin_stop: a string, ignored when field_dict is present
      via_stop: a string, ignored when field_dict is present
      destination_stop: a string, ignored when field_dict is present
      kwargs: arbitrary keyword arguments may be used to add attributes to the
        new object, ignored when field_dict is present
    """
    self._schedule = None

    if not field_dict:
      if route_id:
        kwargs['route_id'] = route_id
      if route_update_date:
        kwargs['route_update_date'] = route_update_date
      if origin_stop:
        kwargs['origin_stop'] = origin_stop
      if via_stop:
        kwargs['via_stop'] = via_stop
      if destination_stop:
        kwargs['destination_stop'] = destination_stop
      field_dict = kwargs

    self.__dict__.update(field_dict)


  def ValidateUpdateDate(self, problems):
    if not util.ValidateDate(self.route_update_date, 'route_update_date', problems):
      problems.InvalidValue('route_update_date', self.route_update_date,
                              'route_update_dateが適切な日付形式ではありません。')
      return False
    return True
    

  def ValidateBeforeAdd(self, problems):
    self.ValidateRouteIdIsPresent(problems)
    self.ValidateUpdateDate(problems)
    # None of these checks are blocking
    return True

  def AddToSchedule(self, schedule, problems):
    pass


