#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ACE 

import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7086493048:AAGk3jf37aj-NCpXQYDyvO0oGUb8GU8vhJ8")
    API_ID = int(os.environ.get("API_ID", "24253854"))
    API_HASH = os.environ.get("API_HASH", "1c6be76aed587364829962e4fa1a500f")
    AUTH_USERS = os.environ.get("AUTH_USERS", "5665231556")
