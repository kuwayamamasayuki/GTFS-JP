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

import extension_util
import transitfeed
from transitfeed.problems import default_problem_reporter


class Agency(transitfeed.Agency):
  """Extension of transitfeed.Agency:
  - Overriding ValidateAgencyLang() for supporting GTFS-JP agency_lang codes.
  """

  _REQUIRED_FIELD_NAMES = transitfeed.Agency._REQUIRED_FIELD_NAMES + ['agency_id']
  _FIELD_NAMES = _REQUIRED_FIELD_NAMES + ['agency_lang',
                                          'agency_phone', 'agency_fare_url', 'agency_email']

  # Overrides transitfeed.Agency.ValidateAgencyLang() and validates agency_lang
  def ValidateAgencyLang(self, problems):
    return not extension_util.ValidateLanguageCode(self.agency_lang, 'agency_lang', problems)

  def ValidateAgencyTimezone(self, problems):
    return not extension_util.ValidateTimezone(self.agency_timezone, 'agency_timezone', problems)
