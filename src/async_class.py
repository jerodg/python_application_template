#!/usr/bin/env python3.9
"""Python Application Template
Copyright (C) 2018-2020 Jerod Gawne <https://github.com/jerodg/>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""
from logging import getLogger
from logging.config import dictConfig
from os.path import basename

import logging_config

dictConfig(logging_config.LOGGING_CONFIG)
logger = getLogger(basename(__file__)[:-3])


class MyClass(object):
    """My Class"""

    def __init__(self):
        pass

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        pass


if __name__ == '__main__':
    print(__doc__)
