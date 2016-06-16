import telebot
import config
import logging

"""
Telegram bot
"""

class Client(object):

    def __init__(self, token: str, channel: str):
        """

        :param token: str
        :param channel: str channel name to post data
        """
        self.bot = telebot.TeleBot(token)
        # self.channel = channel
        self.channel = 91040284

        logging.info('Start Bot to channel {0}'.format(self.channel))

        # self.set_listener(self.send_posts)

    def get_bot(self) -> telebot.TeleBot:
        return self.bot

    def set_listener(self, method):
        self.bot.set_update_listener(method)
        self.bot.polling(none_stop=True)

    def send_posts(self, message):
        self.bot.send_message(self.channel, message)


ID = 12344

# bot = telebot.TeleBot(config.token)
# @bot.message_handler(content_types=["text"])
# def repeat_all_messages(message): # Название функции не играет никакой роли, в принципе
#     bot.send_message(message.chat.id, message.text)

if __name__ == '__main__':
    bot = Client(config.TELEGRAM_TOKEN, config.CHANNEL_NAME)
    bot.set_listener(bot.send_posts)

