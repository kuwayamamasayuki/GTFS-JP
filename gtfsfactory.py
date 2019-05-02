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

# Copyright (C) 2010 Google Inc.
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
from agency_jp import Agency_jp
from route_jp import Route_jp
from office_jp import Office_jp
from translation import Translation

class GtfsFactory(transitfeed.GtfsFactory):
  """Extension of transitfeed.GtfsFactory:
     'agency_jp.txt', 'route_jp.txt', 'office_jp.txt', 'translations.txt' を追加。
  """

  def __init__(self):

    super(GtfsFactory, self).__init__()
    # agency_jp.txt, routes.jp.txt, office_jp.txt, translations.txt を追加。
    self._class_mapping = dict(self._class_mapping.items() + {
      'Agency_jp': Agency_jp,
      'Route_jp': Route_jp,
      'Office_jp': Office_jp,
      'Translation': Translation,
    }.items())

    self._file_mapping['fare_attributes.txt']['required'] = True
    self._file_mapping['feed_info.txt']['required'] = True

    self._file_mapping = dict(self._file_mapping.items() + {
        'agency_jp.txt': { 'required': True, 'loading_order': 5,
                           'classes': ['Agency_jp']},

        'routes_jp.txt': { 'required': False, 'loading_order': 25,
                        'classes': ['Route_jp']},

        'office_jp.txt': { 'required': False, 'loading_order': 35,
                           'classes': ['Office_jp']},

        'translations.txt': { 'required': True, 'loading_order': 110,
                        'classes': ['Translation']},

        }.items())



    
def GetGtfsFactory():
  """Called by FeedValidator to retrieve this extension's GtfsFactory.
     Extensions will most likely only need to create an instance of
     transitfeed.GtfsFactory, call {Remove,Add,Update}Mapping as needed, and
     return that instance"""
  return GtfsFactory()
