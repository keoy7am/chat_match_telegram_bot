# coding: utf-8
"""
usage: /genericMessage
"""
from .utility import send_send_typing_action
from bot_poc import Commands, redisInst
from telegram import MessageEntity
from telegram.ext import MessageHandler, Filters
from telegram.utils.helpers import escape_markdown

class GenericMessageCommand():
    def __init__(self, dispatcher):
        self.name = "genericMessage"
        self.handler = MessageHandler
        self.filter  = Filters.all

        self._registe(dispatcher)

    @send_send_typing_action
    def _execute(self, bot, update):
        """ 處理未被其他Command捕獲的資訊 """
        text = update.message.text
        photo = update.message.photo
        video = update.message.video
        document = update.message.document
        animation = update.message.animation
        voice = update.message.voice
        sticker = update.message.sticker
        video_note = update.message.video_note

        if(text):
            for c in Commands:
                if '/{}'.format(c.name) in text:
                    c._execute(bot, update)
                    return
        
        sender = str(update.message.chat_id)
        matched = redisInst.get(sender)
        if(matched):
            if(text):
                bot.send_message(chat_id=matched, text=text)
            if(photo):
                bot.send_photo(chat_id=matched, photo=photo)
            if(video):
                bot.send_video(chat_id=matched, video=video)
            if(document):
                bot.send_document(chat_id=matched, document=document)
            if(animation):
                bot.send_animation(chat_id=matched, animation=animation)
            if(voice):
                bot.send_voice(chat_id=matched, voice=voice)
            if(sticker):
                bot.send_sticker(chat_id=matched, sticker=sticker)
            if(video_note):
                bot.send_video_note(chat_id=matched, video_note=video_note)

    def _registe(self,dispatcher):
        dispatcher.add_handler(self.handler(self.filter, self._execute))
        print("{} command registered!".format(self.name))