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

from transitfeed.gtfsobjectbase import GtfsObjectBase
from transitfeed.problems import default_problem_reporter
import extension_util
import transitfeed.util as util
import transitfeed

class Office_jp(GtfsObjectBase):
  """営業所情報
  """

  _REQUIRED_FIELD_NAMES = ['office_id', 'office_name']
  _FIELD_NAMES = _REQUIRED_FIELD_NAMES + ['office_url', 'office_phone']

  def __init__(self, id=None, name=None, url=None, phone=None, 
               field_dict=None, **kwargs):
    """Initialize a new Office_jp object.

    Args:
      field_dict: A dictionary mapping attribute name to unicode string
      id: a string, ignored when field_dict is present
      name: a string, ignored when field_dict is present
      url: a string, ignored when field_dict is present
      phone: a string, ignored when field_dict is present
      kwargs: arbitrary keyword arguments may be used to add attributes to the
        new object, ignored when field_dict is present
    """
    self._schedule = None

    if not field_dict:
      if id:
        kwargs['office_id'] = id
      if name:
        kwargs['office_name'] = name
      if url:
        kwargs['office_url'] = url
      if phone:
        kwargs['office_phone'] = phone
      field_dict = kwargs

    self.__dict__.update(field_dict)


  def ValidateOfficeUrl(self, problems):
    return util.ValidateURL(self.office_url, 'office_url', problems)


  def ValidateBeforeAdd(self, problems):
    util.ValidateRequiredFieldsAreNotEmpty(
                          self, self._REQUIRED_FIELD_NAMES, problems)
    self.ValidateOfficeUrl(problems)
    # None of these checks are blocking
    return True

  def ValidateAfterAdd(self, problems):
    return


  def AddToSchedule(self, schedule, problems):
    schedule.AddOfficeJpObject(self, problems)
    