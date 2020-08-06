#!/usr/bin/env python3.8
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
along with this program.  If not, see <http://www.gnu.org/licenses/>."""
from os.path import realpath

LOGGING_CONFIG = {
        'version':                  1,
        'disable_existing_loggers': False,
        'propagate':                True,
        'formatters':               {
                'terse': {
                        'class':   'logging.Formatter',
                        'style':   '{',
                        'datefmt': '%I:%M:%S',
                        'format':  '<{levelname}> [{name}] ({lineno}) {asctime} => {message}'
                        }
                },
        'handlers':                 {
                'terse_console': {
                        'level':     'DEBUG',
                        'class':     'logging.StreamHandler',
                        'formatter': 'terse',
                        'stream':    'ext://sys.stdout'
                        },
                'file':          {
                        'level':       'INFO',
                        'class':       'logging.handlers.TimedRotatingFileHandler',
                        'formatter':   'terse',
                        'filename':    realpath('../logs/script.log'),
                        'when':        'd',
                        'interval':    1,
                        'backupCount': 30
                        }
                },
        'loggers':                  {
                'et_accounts': {
                        'handlers': ['file'],
                        'level':    'INFO'
                        }
                },
        'root':                     {
                'handlers': ['terse_console'],
                'level':    'DEBUG'
                }
        }
