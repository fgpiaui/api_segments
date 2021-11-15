MALE = 'male'
FEMALE = 'female'
ID = 'id'
FIELD = 'field'
VALUE = 'value'
MIN_DATE = 'min_date'
MAX_DATE = 'max_date'
TYPE='type'
EXACT='exact'
CONTAINS='contains'
STARTS_WITH='starts_with'
END_WITH='ends_with'
UPDATE='update'
INCLUDE='INCLUDE'
DATE='date'
AND='and'
OR='or'
NOT='not'
NOR='nor'
OPERATOR='operator'
FIELDS='fields'

SEX = [
    (MALE,MALE),
    (FEMALE, FEMALE)
]

LIST_KEYS_JSON = [ID, FIELD, VALUE]
LIST_KEYS_DATE = [MIN_DATE, MAX_DATE]
LIST_KEYS_STRING = [FIELD, VALUE, TYPE, OPERATOR]
LIST_TYPES = [EXACT, CONTAINS, STARTS_WITH, END_WITH, DATE]
LIST_OPERATORS = [AND, OR, NOT, NOR]

