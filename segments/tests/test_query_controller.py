from segments.controllers.query_controller import QueryController
from segments.tests.cases.case_base import BaseCase


class TestQueryController(BaseCase):
    def setUp(self) -> None:
        data = [
            {
       'fields':[
           {
               'field': 'user__first_name',
               'value':'A',
               'type':'starts_with',
               'operator':'and',
           },
           {
               'field': 'user__last_name',
               'value':'A',
               'type':'ends_with',
               'operator':'or',
           },
       ]
   },
            {
                'fields':[
           {
               'field': 'user__birth_data',
               'value':{'max_date':'1/1/2000'},
               'type':'date',
               'operator':'and',
           },
       ]
   },
        ]
        self._query_controller = QueryController(data)

    def test_execute(self):
        queries = self._query_controller.execute()
        gabarito = "(OR: ('user__first_name__startswith', 'A'), ('user__last_name__endswith', 'A'), (AND: (OR: ('user__first_name__startswith', 'A'), ('user__last_name__endswith', 'A')), ('user__birth_data__lte', '1/1/2000')))"
        print(queries)
        self.assertEqual(str(queries), gabarito)