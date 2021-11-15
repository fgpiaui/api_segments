from segments.models import Tag
from segments.tests.cases.case_singleton import SingletonCase


class TagCase(metaclass=SingletonCase):
    def __init__(self):
        self.list_tags = []
        for i in range(15):
            Tag.objects.create(name=f"Segments {i}")

    def return_values(self):
        return Tag.objects.all()
