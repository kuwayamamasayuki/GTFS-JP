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
from transitfeed.problems import default_problem_reporter
from transitfeed import util
import extension_util

class Agency_jp(transitfeed.Agency):
  """Extension of transitfeed.Agency:
  - 標準的なバス情報フォーマットにおけるagency_jp.txtに関するチェックを行う。
    """
  _REQUIRED_FIELD_NAMES = ['agency_id']
  _FIELD_NAMES = _REQUIRED_FIELD_NAMES + ['agency_official_name', 'agency_zip_number', 
                                          'agency_address', 'agency_president_pos', 'agency_president_name']

  def __init__(self, id=None, official_name=None, zip_number=None, address=None, 
               president_pos=None, president_name=None, field_dict=None, **kwargs):
    """Initialize a new Agency_jp object.

    Args:
      field_dict: A dictionary mapping attribute name to unicode string
      id: a string, ignored when field_dict is present
      official_name: a string, ignored when field_dict is present
      zip_naumber: a string, ignored when field_dict is present
      address: a string, ignored when field_dict is present
      president_pos: a string, ignored when field_dict is present
      president_name: a string, ignored when field_dict is present
      kwargs: arbitrary keyword arguments may be used to add attributes to the
        new object, ignored when field_dict is present
    """
    self._schedule = None

    if not field_dict:
      if id:
        kwargs['agency_id'] = id
      if official_name:
        kwargs['agency_official_name'] = official_name
      if zip_number:
        kwargs['agency_zip_number'] = zip_number
      if address:
        kwargs['agency_address'] = address
      if president_pos:
        kwargs['agency_president_pos'] = president_pos
      if president_name:
        kwargs['agency_president_name'] = president_name
      field_dict = kwargs

    self.__dict__.update(field_dict)

  def ValidateAgencyZipNumber(self, problems):
    if not self.agency_zip_number:
      return False
    return not extension_util.ValidateZipNumber(
        self.agency_zip_number, 'agency_zip_number', problems)

  def ValidateAgencyPresidentName(self, problems):
    return not extension_util.ValidatePresidentName(self.agency_president_name, 
                                     'agency_president_name', problems)


  def Validate(self, problems=default_problem_reporter):
    """
    'agency_jp.txt'に関するチェック
    """

    found_problem = False
    found_problem = ((not util.ValidateRequiredFieldsAreNotEmpty(
                          self, self._REQUIRED_FIELD_NAMES, problems))
                          or found_problem) 
    found_problem = self.ValidateAgencyZipNumber(problems) or found_problem
    found_problem = self.ValidateAgencyPresidentName(problems) or found_problem

    return not found_problem

  def ValidateBeforeAdd(self, problems):
    return True

  def ValidateAfterAdd(self, problems):
    self.Validate(problems)

  def AddToSchedule(self, schedule, problems):
    schedule.AddAgencyJpObject(self, problems)
       


