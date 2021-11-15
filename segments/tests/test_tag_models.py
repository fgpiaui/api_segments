from segments.models import Tag
from segments.tests.cases.case_base import BaseCase


class TestTagModels(BaseCase):
    def setUp(self) -> None:
        self.tag = Tag.objects.create(
            name='Projetos'
        )


    def test_create_user_success(self):
        self.assertTrue(isinstance(self.tag, Tag))


    def test_update_user(self):
        novo_nome = 'Nova Tag'
        self.tag.name = novo_nome
        self.tag.save()
        self.assertEqual(self.tag.name,novo_nome)


    def test_delete_user(self):
        antes = Tag.objects.all()
        tag = Tag.objects.create(
            name='Engenharia',
        )
        tag.delete()
        depois = Tag.objects.all()
        self.assertEqual(len(antes), len(depois))