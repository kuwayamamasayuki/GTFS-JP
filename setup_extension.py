#!/usr/bin/python2.5

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

import agency
import agency_jp
import stop
import route
import route_jp
import trip
import office_jp
import fareattribute
import farerule
import shape
import feedinfo
import translation
import gtfsfactory
import schedule

def GetGtfsFactory(factory = None):
  if not factory:
    factory = gtfsfactory.GetGtfsFactory()

  # Agency class extension
  factory.UpdateClass('Agency', agency.Agency)

  # Agency_jp class extension
  factory.UpdateClass('Agency_jp', agency_jp.Agency_jp)

  # Stop class extension
  factory.UpdateClass('Stop', stop.Stop)

  # Route class extension
  factory.UpdateClass('Route', route.Route)

  # Route_jp class extension
  factory.UpdateClass('Route_jp', route_jp.Route_jp)

  # Trip class extension
  factory.UpdateClass('Trip', trip.Trip)

  # Office_jp class extension
  factory.UpdateClass('Office_jp', office_jp.Office_jp)

  # FareAttribute class extension
  factory.UpdateClass('FareAttribute', fareattribute.FareAttribute)

  # FareRUles class extension
  factory.UpdateClass('FareRule', farerule.FareRule)

  # Shape class extension
  factory.UpdateClass('Shape', shape.Shape)

  # FeedInfo class extension
  factory.UpdateClass('FeedInfo', feedinfo.FeedInfo)

  # Translation class extension
  factory.UpdateClass('Translation', translation.Translation)

  # Schedule class extension
  factory.UpdateClass('Schedule', schedule.Schedule)

  return factory
