# coding: utf-8
"""
usage: /help
"""
from .utility import send_send_typing_action
from bot_poc import Commands
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CommandHandler
from telegram.utils.helpers import escape_markdown

class HelpCommand():
    def __init__(self):
        self.name = "help"
        self.usage   = "/help ,顯示指令列表"
        self.handler = CommandHandler

    @send_send_typing_action
    def _execute(self, bot, update):
        """ 顯示指令列表 """
        commands_str = " \n".join(["- {}".format(c.usage) for c in Commands])
        keyboard = [[InlineKeyboardButton("中文化", url='https://t.me/setlanguage/taiwan')]]
        reply_markup = InlineKeyboardMarkup(keyboard)

        update.message.reply_text('提供指令如下：\n{}'.format(commands_str), reply_markup=reply_markup)

    def registe(self,dispatcher):
        dispatcher.add_handler(self.handler(self.name, self._execute))
        print("{} command registered!".format(self.name))