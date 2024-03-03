#!/usr/bin/env python3

# Filename: config.py
# Created on: March  2, 2024
# Author: Lucas Araújo <araujolucas@dcc.ufmg.br>

import os

SOCKDIR = os.environ.get("XDG_RUNTIME_DIR", "/var/tmp")
SOCKFILE = os.path.join(SOCKDIR, "pomo.sock")
SERVER_SOCKFILE = os.path.join(SOCKDIR, "server-pomo.sock")

LOGFILE = "/tmp/pomo.log"
DB_FILE = "~/Documents/pomo.db"

SQL_INSERT_CMD = "INSERT INTO sessions VALUES (date('now'), time('now'), NULL, NULL)"
SQL_UPDATE_TABLE_CMD = """UPDATE sessions
                          SET stop = time('now')
                          WHERE start IN (
                             SELECT start FROM sessions
                             ORDER BY start DESC
                             LIMIT 1)
                        """

SQL_CREATE_TABLE_CMD = """CREATE TABLE IF NOT EXISTS sessions (
                            date TEXT,
                            start TEXT,
                            stop TEXT,
                            tag TEXT)
                       """

DAY_FACTOR = 86400
HOUR_FACTOR = 3600
MINUTE_FACTOR = 60

DEFAULT_WORKTIME = 40 * MINUTE_FACTOR
DEFAULT_BREAKTIME = 10 * MINUTE_FACTOR

PACKET_SIZE = 1024 * 2
SOCKET_TIMEOUT = 1e-10
