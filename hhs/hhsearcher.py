import requests
from hhs import utils
from hhs.model import Vacancy


class HHSearcher(object):
    """
    Main HH Searcher class

    """

    url = 'https://api.hh.ru'

    def __init__(self, delay=60):
        self.delay = delay

    def search(self, text=''):
        url = self.url + '/vacancies'
        params = {
            'text': text,
            'specialization': 1,
            'area': 66,
            'salary': 90000,
            'currency_code': 'RUR',
            'order_by': 'relevance',
            'search_period': 7,
            'items_on_page': 100,
            'no_magic': True,
            'per_page': 100,
            'page': 0
        }
        data = self.__request(url, params)
        print(data)

        '''
        TODO:: Create Vacancy models and send into telegram !!!!!!
        '''

        # vacancies = []
        # for item in data['items']:
        #     v = Vacancy()


    def get_areas(self):
        areas = self.__request(self.url + '/areas')
        return areas

    def __request(self, url, params={}, method='get'):
        """ Request executor

        :param url: str
        :param params: dict - additional parameters to request
        :param method: str - default GET
        :return: str
        """

        if method.lower() == 'get':
            res = requests.get(url, params, headers=self.__get_headers())
        else:
            res = requests.post(url, params, headers=self.__get_headers())

        if res.status_code != 200:
            print("Request error:: {0}:{1}".format(res.status_code, res.text))
            return False
        return res.json()

    @staticmethod
    def __get_headers() -> dict:
        """ Combine Requirement Headers into single dictionary

        :return:
        """
        return {
            'User-Agent': utils.get_random_user_agent()
        }



    '''
    # https://nn.hh.ru/search/vacancy?
    text=Python
    &specialization=1
    &area=66
    &salary=90000
    &currency_code=RUR
    &experience=doesNotMatter
    &order_by=relevance
    &search_period=7
    &items_on_page=100
    &no_magic=true
    '''

    '''
    https://nn.hh.ru/search/vacancy?text=Python&specialization=1&area=66&salary=90000&currency_code=RUR&experience=doesNotMatter&schedule=fullDay&schedule=remote&order_by=relevance&search_period=&items_on_page=50&no_magic=true
    '''
