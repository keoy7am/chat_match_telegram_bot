# coding: utf-8
"""
usage: /match
"""
from bot_poc import redis
from telegram.ext import StringCommandHandler, Filters
from telegram.utils.helpers import escape_markdown

class MatchCommand():
    def __init__(self):
        self.name = "match"
        self.usage   = "/match ,尋找配對"
        self.handler = StringCommandHandler
        self.filter  = Filters.text
        
    def _execute(self, bot, update):
        """ 尋找配對 """
        sender = str(update.message.chat_id)

        if(redis.get(sender)):
            update.message.reply_text('請先離開對話再重新配對!')
            return
        if(redis.lrem("queue", 0, sender) > 0):
            update.message.reply_text('本已在配對佇列中，將重新進入佇列!')
        if(redis.llen("queue") > 0):
            matched = redis.lpop("queue")
            redis.set(sender,matched)
            redis.set(matched,sender)
            # TODO 發送訊息給 matched ('已配對成功! 接下來發言內容將會透過Bot匿名轉發!')
            update.message.reply_text('已配對成功! 接下來發言內容將會透過Bot匿名轉發!')
        else:
            redis.lpush("queue", sender)
            update.message.reply_text('已進入配對序列,將會在配對成功後通知。')

    def registe(self,dispatcher):
        dispatcher.add_handler(self.handler(self.name, self._execute))
        print("{} command registered!".format(self.name))