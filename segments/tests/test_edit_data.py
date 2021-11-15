from segments.controllers.edit_data import EditData
from segments.models import Tag
from segments.tests.cases.case_base import BaseCase


class TestEditData(BaseCase):
    def setUp(self) -> None:
        tag = Tag.objects.create(name='Tag Antiga')
        self._nome_novo = 'Tag Nova'
        self._edit_data = EditData('name', self._nome_novo, tag)

    def test_update(self):
        tag = self._edit_data.update()
        self.assertEqual(tag.name, self._nome_novo)