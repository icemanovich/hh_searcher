
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

        self.currency = 'RUR'

    def __repr__(self):
        """ Detailed model view

        :return: object
        """
        return 'Vacancy(%r, %r, %r, %r, %r, %r, %r, %r)' % (
            self.name,
            self.salary,
            self.url,
            self.archived,
            self.area,
            self.employer,
            self.created_at,
            self.published_at
        )

    def __str__(self):
        """ Short description of filled model

        :return: object
        """
        return '%s [ Salary: %s]: - %s, %s' % (
            self.name,
            self.salary_info(),
            self.employer['name'],
            self.url
        )

    def salary_info(self):
        value = self.salary
        if self.salary:
            self.currency = self.salary['currency']
            value = '{0}-{1} {2}'.format(self.salary['from'], self.salary['to'], self.currency)
        return value

    @classmethod
    def from_dict(cls, data: dict) -> object:
        """ Create model instance from dictionary

        :param data:
        :return: object
        """
        return cls(
            url=data['alternate_url'],
            archived=data['archived'],
            area=data['area'],
            employer=data['employer'],
            name=data['name'],
            salary=data['salary'],
            created_at=data['created_at'],
            published_at=data['published_at']
        )

    def to_dict(self) -> dict:
        """ Convert filled model into dictionary

        :return:
        """
        return dict(
            url=self.url,
            archived=self.archived,
            area=self.area,
            employer=self.employer,
            name=self.name,
            salary=self.salary,
            created_at=self.created_at,
            published_at=self.published_at
        )


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
