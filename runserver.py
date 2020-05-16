# coding: utf-8
"""
This script runs the bot_poc application using a development server.
"""
import sys
import importlib,sys
importlib.reload(sys)

from os import environ
from bot_poc import app

import ptvsd
ptvsd.enable_attach()

if __name__ == '__main__':
    DEBUG = environ.get('APP_DEBUG', False)
    if(DEBUG):
        app.debug = DEBUG
    HOST = environ.get('SERVER_HOST', '0.0.0.0')
    try:
        PORT = int(environ.get('SERVER_PORT', '5000'))
    except ValueError:
        PORT = 5000
    app.run(HOST, PORT, threaded=True)
