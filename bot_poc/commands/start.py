# coding: utf-8
"""
usage: /start
"""
from .utility import send_send_typing_action
from bot_poc import Commands
from telegram.ext import CommandHandler, Filters
from telegram.utils.helpers import escape_markdown

class StartCommand():
    def __init__(self):
        self.name = "start"
        self.usage   = "/start ,顯示初始資訊"
        self.handler = CommandHandler
        self.filter  = Filters.text
        
    @send_send_typing_action
    def _execute(self, bot, update):
        """ 顯示初始資訊 """
        commands_str = "\n".join(["- /{}".format(c.name) for c in Commands])
        update.message.reply_text('歡迎使用本機器人!\
        \n提供的指令如下: \
        \n{} \
        \n\n請透過 /help 指令查閱更多。'.format(commands_str))

    def registe(self,dispatcher):
        dispatcher.add_handler(self.handler(self.name, self._execute))
        print("{} command registered!".format(self.name))