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

# Objects in a schedule (Route, Trip, etc) should not keep a strong reference
# to the Schedule object to avoid a reference cycle. Schedule needs to use
# __del__ to cleanup its temporary file. The garbage collector can't handle
# reference cycles containing objects with custom cleanup code.
import weakref

import gtfsfactory
import transitfeed
from transitfeed import problems as problems_module
from transitfeed.util import defaultdict
from transitfeed import util

class Schedule(transitfeed.Schedule):
  """Represents a Schedule, a collection of stops, routes, trips and
  an agency.  This is the main class for this module."""


  def __init__(self, problem_reporter=None,
               memory_db=True, check_duplicate_trips=False,
               gtfs_factory=None):
    super(Schedule,self).__init__()
    self._agency_jps = {}
    self._office_jps = {}



  def AddAgencyJpObject(self, agency_jp, problem_reporter=None, validate=False):
    assert agency_jp._schedule is None

    if not problem_reporter:
      problem_reporter = self.problem_reporter

    if agency_jp.agency_id in self._agency_jps:
      problem_reporter.DuplicateID('agency_id', agency_jp.agency_id)
      return

    self.AddTableColumns('agency_jp', agency_jp._ColumnNames())
    agency_jp._schedule = weakref.proxy(self)

    if validate:
      agency_jp.Validate(problem_reporter)
    self._agency_jps[agency_jp.agency_id] = agency_jp


  def AddOfficeJpObject(self, office_jp, problem_reporter=None, validate=False):
    assert office_jp._schedule is None

    if not problem_reporter:
      problem_reporter = self.problem_reporter

    if office_jp.office_id in self._office_jps:
      problem_reporter.DuplicateID('office_id', office_jp.office_id)
      return

    self.AddTableColumns('office_jp', office_jp._ColumnNames())
    office_jp._schedule = weakref.proxy(self)

    if validate:
      office_jp.Validate(problem_reporter)
    self._office_jps[office_jp.office_id] = office_jp

  def ValidateRouteNames(self, problems, validate_children):
    # Check for multiple routes using same short + long name
    #route_names = {}
    for route in self.routes.values():
      if validate_children:
        route.Validate(problems)
      #short_name = ''
      #if not util.IsEmpty(route.route_short_name):
      #  short_name = route.route_short_name.lower().strip()
      #long_name = ''
      #if not util.IsEmpty(route.route_long_name):
      #  long_name = route.route_long_name.lower().strip()
      #name = (short_name, long_name)
      #if name in route_names:
      #  problems.InvalidValue('route_long_name',
      #                        long_name,
      #                        'The same combination of '
      #                        'route_short_name and route_long_name '
      #                        'shouldn\'t be used for more than one '
      #                        'route, as it is for the for the two routes '
      #                        'with IDs "%s" and "%s".' %
      #                        (route.route_id, route_names[name].route_id),
      #                        type=problems_module.TYPE_WARNING)
      #else:
      #  route_names[name] = route
