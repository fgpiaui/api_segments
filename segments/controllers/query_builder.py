from django.db.models import Q

from segments.constantes import EXACT, CONTAINS, STARTS_WITH, END_WITH, DATE, MIN_DATE, MAX_DATE, \
    OR, NOT, AND, NOR


class QueryBuilder:
    def __init__(self):
        self.queries = Q()
        self.query = Q()

    def update_query(self, field, value, operator, type):
        query = self.__return_query(field, value, type)
        query = self.__operator_query(query)[operator]
        self.query = query


    def concat_query(self):
         self.queries = (self.queries) | (self.query)


    def __operator_query(self, query):
        return {
            AND: self.query & Q(**query),
            OR: self.query | Q(**query),
            NOT: self.query & ~Q(**query),
            NOR: self.query | ~Q(**query),
        }

    def __return_query(self, field, value, type):
        if type == EXACT:
            return {f'{field}': value}
        elif type == CONTAINS:
            return {f'{field}__icontains': value}
        elif type == STARTS_WITH:
            return {f'{field}__startswith': value}
        elif type == END_WITH:
            return {f'{field}__endswith': value}
        elif type == DATE:
            return self.__assert_date(value, field)
        else:
            return None

    def __assert_date(self, value, field):
        resultado = {}
        if MIN_DATE in value:
            resultado[f'{field}__gte'] =  value[MIN_DATE]
        if MAX_DATE in value:
            resultado[f'{field}__lte'] = value[MAX_DATE]
        return resultado