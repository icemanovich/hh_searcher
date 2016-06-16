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
        self.channel = channel

        logging.info('Start Bot to channel {0}'.format(self.channel))

    def get_bot(self) -> telebot.TeleBot:
        return self.bot

    def set_listener(self, method):
        self.bot.add_message_handler(method)
        self.bot.polling(none_stop=True)

    def send_posts(self, message):
        if isinstance(message, telebot.types.Message) and message.text.startswith('/'):
            line = message.text.split(' ')
            self.handle_commands(line[0], line[1:])
            return

        self.bot.send_message(self.channel, message)

    """
    TODO::handle commands to change query and handle bot
    """
    def handle_commands(self, command, *args):
        print(command, args)
        s = ''

    def __help(self):
        pass

    def __set_query(self):
        pass


if __name__ == '__main__':
    bot = Client(config.TELEGRAM_TOKEN, config.CHANNEL_NAME)
    bot.set_listener(bot.send_posts)


    # bot = telebot.TeleBot(config.TELEGRAM_TOKEN)
    # @bot.inline_handler(lambda query: len(query.query) is 0)
    # def empty_query(query):
        # bot.reply_to('Help was initiated')
        # bot.send_message(91040284, 'asdasda')
        # print(message)
