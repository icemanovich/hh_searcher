
class Vacancy(object):
    def __init__(self, ):
        pass


class SearchQuery(object):
    def __init__(self, text, search_field, experience,
                 employment, schedule, area,
                 metro, specialization, industry,
                 currency, salary, label,
                 period=30,
                 order_by='relevance',
                 per_page=100, page=1):
        
        self.search_field = search_field
        self.text = text
        self.order_by = order_by
        self.per_page = per_page
        self.page = page
