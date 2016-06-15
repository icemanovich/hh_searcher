from hhs.hhsearcher import HHSearcher


if __name__ == '__main__':

    scanner = HHSearcher()
    v = scanner.search('Python')

    for i in v:
        print(i)

    f = ''

    '''
    request examples

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