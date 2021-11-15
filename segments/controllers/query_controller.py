from segments.constantes import FIELD, VALUE, OPERATOR, TYPE, FIELDS
from segments.controllers.query_builder import QueryBuilder


class QueryController:
    def __init__(self, data):
        self._data = data
        self._query_builder = QueryBuilder()

    def execute(self):
        for list_data in self._data:
            self.__execute_one_list_query(list_data[FIELDS])
            self._query_builder.concat_query()
        return self._query_builder.queries

    def __execute_one_list_query(self, list_data):
        for data in list_data:
            self._query_builder.update_query(data[FIELD], data[VALUE], data[OPERATOR], data[TYPE])




