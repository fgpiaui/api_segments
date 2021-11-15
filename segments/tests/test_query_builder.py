from django.db.models import Q

from segments.constantes import AND, CONTAINS, FIELD, VALUE, OPERATOR, TYPE
from segments.controllers.query_builder import QueryBuilder
from segments.tests.cases.case_base import BaseCase


class TestQueryBuilder(BaseCase):
    def setUp(self) -> None:
        self._query_builder = QueryBuilder()

    def test_update_query(self):
        data= {
            'field': 'user__first_name',
            'value': 'Filipe',
            'operator': AND,
            'type': CONTAINS,
        }


        self._query_builder.update_query(data[FIELD], data[VALUE], data[OPERATOR], data[TYPE])
        gabarito = "(AND: ('user__first_name__icontains', 'Filipe'))"
        self.assertEqual(str(self._query_builder.query), gabarito)

    def test_concat_query(self):
        self._query_builder.queries = Q({'user__last_name':'Pereira'})
        self._query_builder.query = Q({'user__first_name':'Filipe'})
        self._query_builder.concat_query()
        gabarito = "(OR: {'user__last_name': 'Pereira'}, {'user__first_name': 'Filipe'})"
        print(self._query_builder.queries)
        self.assertEqual(str(self._query_builder.queries), gabarito)
