# coding: utf-8
"""
The flask application package.
"""
import logging
import telegram
import requests as req
from flask import Flask, request
from flask_restful import Api, Resource, reqparse
from telegram.ext import Dispatcher, MessageHandler, Filters
#from bot_poc.controllers.api import *
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

import bot_poc.config
app = Flask(__name__)
app.config.from_object(config)

import redis
connectionPool = redis.ConnectionPool(host='redis', port=6379 ,decode_responses=True)
redisInst = redis.Redis(connection_pool=connectionPool)
redisInst.set('test','ok')

logger.info("Config Loaded!")
if(app.config['TEMPLATES_AUTO_RELOAD']==True):
    app.jinja_env.auto_reload = True
    print('enabled auto_reload')

print("api key: {}".format(app.config['BOT_API_KEY']))
bot = telegram.Bot(token=(app.config['BOT_API_KEY']))

@app.route("/")
def index():
    logging.info("Web service works!")
    return "Service works!"

@app.route("/setHook")
def setHook():
    try:    
        url = "https://api.telegram.org/bot{}/setWebhook?url={}".format(app.config['BOT_API_KEY'],app.config['BOT_HOOK_URL'])
        res = req.get(url)
        result = "setting hook to {}.<br>result:{}".format(url,res.text)
        return res.text
    except:
        return "send failed."

@app.route('/hook', methods=['POST'])
def webhook_handler():
    """Set route /hook with POST method will trigger this method."""
    if request.method == "POST":
        update = telegram.Update.de_json(request.get_json(force=True), bot)

        dispatcher.process_update(update)
    return 'ok'

def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)

dispatcher = Dispatcher(bot, None)

Commands = []
from bot_poc.commands.start import StartCommand
Commands.append(StartCommand())

from bot_poc.commands.help import HelpCommand
Commands.append(HelpCommand())

from bot_poc.commands.match import MatchCommand
Commands.append(MatchCommand())

from bot_poc.commands.leave import LeaveCommand
Commands.append(LeaveCommand())

for command in Commands:
    command.registe(dispatcher)

from bot_poc.commands.genericMessage import GenericMessageCommand
GenericMessageCommand(dispatcher)

dispatcher.add_error_handler(error)
