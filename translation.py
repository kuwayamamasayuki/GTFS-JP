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

class Translation(GtfsObjectBase):
  """
  - translation.txtに関する確認を行う。
  """
  _REQUIRED_FIELD_NAMES = ['trans_id', 'lang', 'translation']
  _FIELD_NAMES = _REQUIRED_FIELD_NAMES 

  def __init__(self, trans_id=None, lang=None, translation=None, field_dict=None, **kwargs):
    """Initialize a new Agency_jp object.

    Args:
      field_dict: A dictionary mapping attribute name to unicode string
      trans_id: a string, ignored when field_dict is present
      lang: a string, ignored when field_dict is present
      translation: a string, ignored when field_dict is present
      kwargs: arbitrary keyword arguments may be used to add attributes to the
        new object, ignored when field_dict is present
    """
    self._schedule = None

    if not field_dict:
      if trans_id:
        kwargs['trans_id'] = trans_id
      if lang:
        kwargs['lang'] = lang
      if translation:
        kwargs['translation'] = translation
      field_dict = kwargs

    self.__dict__.update(field_dict)

  def ValidateBeforeAdd(self, problems):
     util.ValidateRequiredFieldsAreNotEmpty(
                          self, self._REQUIRED_FIELD_NAMES, problems)