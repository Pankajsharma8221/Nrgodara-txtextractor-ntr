#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ACE 

import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6772969304:AAG0UbpqrOr09GiaM_hmw5Odwyd7oyZzGBw")
    API_ID = int(os.environ.get("API_ID", "20346550"))
    API_HASH = os.environ.get("API_HASH", "bc79c3bea7a626887bdc0871eecf0327")
    AUTH_USERS = os.environ.get("AUTH_USERS", "5665231556")
