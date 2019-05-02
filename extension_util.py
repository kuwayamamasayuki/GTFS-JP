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

import re

from transitfeed import problems as problems_class
from transitfeed import util


def IsValidLanguageCode(lang):
  """
  Checks the validity of a language code value:
    - 'agency_lang'が'ja'（固定文字列）であることの確認
  """
  return lang == 'ja'

def ValidateLanguageCode(lang, column_name=None, problems=None):
  """
  Validates a non-required language code value using IsValidLanguageCode():
    - if invalid adds InvalidValue error (if problems accumulator is provided)
    - an empty language code is regarded as valid! Otherwise we might end up
      with many duplicate errors because of the required field checks.
    - 'agency_lang'が'ja'（固定文字列）であればtrueを返す。
  """
  if IsEmpty(lang) or IsValidLanguageCode(lang):
    return True
  else:
    if problems:
      problems.InvalidValue(column_name, lang,
      'langは，日本の場合「ja」である必要があります。（GTFS-JP仕様書(第２版) 2-1.等参照）')
    return False

def IsEmpty(value):
  return value is None or (isinstance(value, basestring) and not value.strip())


def IsValidTimezone(timezone):
  """
  Checks the validity of a timezone string value:
    - 日本の場合、「Asia/Tokyo」を設定することとなっているのでそのチェックを行う。
  """

  return timezone == "Asia/Tokyo"

def ValidateTimezone(timezone, column_name=None, problems=None):
  """
  Validates a non-required timezone string value using IsValidTimezone():
    - if invalid adds InvalidValue error (if problems accumulator is provided)
    - an empty timezone string is regarded as valid! Otherwise we might end up
      with many duplicate errors because of the required field checks.
  """
  if IsEmpty(timezone) or IsValidTimezone(timezone):
    return True
  else:
    if problems:
      problems.InvalidValue(
          column_name, timezone,
          'agency_timezoneは，日本の場合「Asia/Tokyo」である必要があります。（GTFS-JP仕様書(第２版) 2-1.参照）')
    return False


def IsValidZipNumber(zipnumber):
  """
  Checks the validity of a zip_number string value:
    - ハイフンなしの半角数字７桁となっているかどうかのチェックを行う。
  """

  return not re.match('^[0-9]{7}$', zipnumber) == None

def ValidateZipNumber(zipnumber, column_name=None, problems=None):
  """
  郵便番号が，ハイフンなしの半角数字７桁であるかどうかを確認する。
  """

  if IsEmpty(zipnumber) or IsValidZipNumber(zipnumber):
    return True
  else:
    if problems:
      problems.InvalidValue(
        column_name, zipnumber,
        'agency_zip_numberは，ハイフンなしの半角数字７桁である必要があります。（GTFS-JP仕様書(第２版) 2-1.参照）'
      )
    return False


def IsValidPresidentName(presidentname):
  """
  Checks the validity of a president_name string value:
    - 姓と名の間は全角スペース１文字となっているかどうかのチェックを行う。
  """
  return not re.match(u'^.+　.+$', presidentname) == None

def ValidatePresidentName(presidentname, column_name=None, problems=None):
  """
  姓と名の間は全角スペース１文字となっているかどうかのチェックを行う。
  """

  if IsEmpty(presidentname) or IsValidPresidentName(presidentname):
    return True
  else:
    if problems:
      problems.InvalidValue(
        column_name, presidentname,
        'agency_president_nameは，姓と名の間は全角スペース１文字である必要があります。（GTFS-JP仕様書(第２版) 2-1.参照）'
      )
    return False

def ValidateAgencyId(agencyid, column_name=None, problems=None):
  if not IsEmpty(agencyid):
    return True
  else:
    if problems:
      problems.InvalidValue(column_name, agencyid,
      'agency_idは必須項目です。')
    return False
    