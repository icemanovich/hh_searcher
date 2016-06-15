
class Vacancy(object):
    def __init__(self, url, archived, area, employer, name, salary, created_at, published_at):

        self.url = url
        self.archived = archived
        self.area = area
        self.employer = employer
        self.name = name
        self.salary = salary
        self.created_at = created_at
        self.published_at = published_at


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
