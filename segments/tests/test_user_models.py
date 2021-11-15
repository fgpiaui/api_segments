from datetime import date, datetime

from django.db import IntegrityError

from segments.constantes import MALE, FEMALE
from segments.models import User
from segments.tests.cases.case_base import BaseCase


class TestUserModels(BaseCase):
    def setUp(self) -> None:
        self.user = User.objects.create(
            first_name='Teste',
            last_name='Model',
            email='teste@model.com.br',
            birth_date=date.today(),
            admission_date=date.today(),
            last_sign_in=datetime.now(),
            is_active=True,
            sex=MALE
        )



    def test_create_user_success(self):
        self.assertTrue(isinstance(self.user, User))

    def test_create_user_failed(self):
        with self.assertRaises(IntegrityError):
            User.objects.create(
                first_name='1'
            )

    def test_update_user(self):
        novo_nome = 'Novo Nome'
        self.user.first_name = novo_nome
        self.user.save()
        self.assertEqual(self.user.first_name,novo_nome)



    def test_delete_user(self):
        antes = User.objects.all()
        user = User.objects.create(
            first_name='Teste 2',
            last_name='Model 2',
            email='teste2@model.com.br',
            birth_date=date.today(),
            admission_date=date.today(),
            last_sign_in=datetime.now(),
            is_active=False,
            sex=FEMALE
        )
        user.delete()
        depois = User.objects.all()
        self.assertEqual(len(antes), len(depois))