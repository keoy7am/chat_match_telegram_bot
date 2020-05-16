# coding: utf-8
"""
usage: /match
"""
from bot_poc import redis
from telegram.ext import StringCommandHandler, Filters
from telegram.utils.helpers import escape_markdown

class LeaveCommand():
    def __init__(self):
        self.name = "leave"
        self.usage   = "/leave ,離開配對佇列/對話"
        self.handler = StringCommandHandler
        self.filter  = Filters.text
        
    def _execute(self, bot, update):
        """ 離開配對 """
        sender = str(update.message.chat_id)

        if(redis.lrem("queue", 0, sender) > 0):
            update.message.reply_text('已離開配對佇列!')
            return
        if(redis.get(sender)):
            matched = redis.get(sender)
            redis.delete(sender)
            redis.delete(matched)
            # TODO 發送訊息給 matched ('對方已離開對話!!')
            update.message.reply_text('已成功離開對話!!')
        else:
            update.message.reply_text('尚未進入配對或對話中唷!!')

    def registe(self,dispatcher):
        dispatcher.add_handler(self.handler(self.name, self._execute))
        print("{} command registered!".format(self.name))