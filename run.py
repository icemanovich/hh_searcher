from hhs.hhsearcher import HHSearcher
from hhs.client.bot import Client
import config

if __name__ == '__main__':

    scanner = HHSearcher()
    bot = Client(config.TELEGRAM_TOKEN, config.CHANNEL_NAME)

    v = scanner.search('Python', salary=9000, period=7)
    for i in v:
        # print(i)
        bot.send_posts(i)


    '''
    TODO:: return random 5 vacancies
    '''
