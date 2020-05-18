from functools import wraps
from telegram import ChatAction

def send_send_typing_action(func):
    """Sends typing action while processing func command."""

    @wraps(func)
    def command_func(command ,bot, update, *args, **kwargs):
        bot.send_chat_action(chat_id=update.effective_message.chat_id, action=ChatAction.TYPING)
        return func(command ,bot, update)

    return command_func