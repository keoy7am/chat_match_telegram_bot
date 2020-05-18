# coding: utf-8
"""
usage: /genericMessage
"""
from bot_poc import Commands, redisInst
from telegram.ext import MessageHandler, Filters
from telegram.utils.helpers import escape_markdown

class GenericMessageCommand():
    def __init__(self, dispatcher):
        self.name = "genericMessage"
        self.handler = MessageHandler
        self.filter  = Filters.text

        self._registe(dispatcher)
        
    def _execute(self, bot, update):
        """ 處理未被其他Command捕獲的資訊 """
        text = update.message.text
        for c in Commands:
            if '/{}'.format(c.name) in text:
                c._execute(bot, update)
                return
        
        sender = str(update.message.chat_id)
        matched = redisInst.get(sender)
        if(matched):
            bot.send_message(chat_id=matched, text=text)

    def _registe(self,dispatcher):
        dispatcher.add_handler(self.handler(self.filter, self._execute))
        print("{} command registered!".format(self.name))