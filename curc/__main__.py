# Copyright 2021 Oskar Sharipov
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from typing import Optional, List, Dict
import os
import sys
import datetime
import uuid
import pathlib
import tempfile
import enum

from xml.parsers.expat import ExpatError
import requests
import xmltodict

from . import __version__, __doc__

URL = f"https://www.ecb.europa.eu/stats/eurofxref/eurofxref-daily.xml?{uuid.uuid4()}"
FILE_PREFIX = f"curc_v{__version__}_"
RATES_PATH = ["gesmes:Envelope", "Cube", "Cube", "Cube"]
TIME_PATH = RATES_PATH[:-1] + ["@time"]

today = datetime.date.today().strftime("%Y-%m-%d")


def which_file(date: str) -> pathlib.Path:
    path = pathlib.Path(tempfile.gettempdir()) / (FILE_PREFIX + date)
    return path


def load() -> Optional[str]:
    if which_file(today).is_file():
        with open(which_file(today), "r") as file:
            return file.read()
    try:
        response = requests.get(URL)
    except requests.exceptions.ConnectionError:
        return None
    if response.ok:
        return response.text
    return None


def extract(currencies: List[Dict[str, str]]) -> Optional[Dict[str, float]]:
    result = {}
    for element in currencies:
        try:
            result[element["@currency"].upper()] = float(element["@rate"])
        except KeyError:
            return None
    result["EUR"] = 1.0
    return result


class Exit(enum.IntEnum):
    OK = 0
    GETERROR = 1
    PARSEERROR = 2
    EXTRACTERROR = 3
    INPUTERROR = 4


def main() -> Exit:
    string_xml = load()
    if string_xml is None:
        return Exit.GETERROR
    try:
        doc = xmltodict.parse(string_xml)
    except ExpatError:
        return Exit.PARSEERROR

    current = doc
    for p in RATES_PATH:
        if not isinstance(current, dict) or p not in current:
            return Exit.EXTRACTERROR
        current = current[p]

    currencies = extract(current)
    if currencies is None:
        return Exit.EXTRACTERROR
    with open(which_file(today), "w") as file:
        file.write(string_xml)

    if "--help" in sys.argv[1:] or not sys.argv[1:]:
        print(__doc__, file=sys.stderr)
        return Exit.OK

    if "--list" in sys.argv[1:]:
        print(", ".join(sorted(currencies.keys())) + ".")
        return Exit.OK

    try:
        amount = float(sys.argv[1])
        _from = sys.argv[2].upper()
        _ = currencies[_from]
        to = sys.argv[3].upper()
        _ = currencies[to]
    except (IndexError, ValueError, KeyError):
        return Exit.INPUTERROR
    result = amount / currencies[_from] * currencies[to]
    if os.getenv("SCRIPTING") is None:
        print(f"{amount:,.2f} {_from} = {result:,.2f} {to}\t(on {today})")
    else:
        print(f"{result:,.2f}")

    return Exit.OK


def console():
    exit_code = main()
    if exit_code == Exit.GETERROR:
        print("Cannot get response from ECB.", file=sys.stderr)
    elif exit_code == Exit.PARSEERROR:
        print("Cannot parse response from ECB.", file=sys.stderr)
    elif exit_code == Exit.EXTRACTERROR:
        print("Cannot extract rates from ECB response.", file=sys.stderr)
    elif exit_code == Exit.INPUTERROR:
        print(__doc__, file=sys.stderr)
    sys.exit(int(exit_code))


if __name__ == "__main__":
    console()
