from datetime import datetime, date
from django.test import TestCase
from django.urls import reverse
from segments.constantes import MALE
from segments.models import User, Tag, UserTag
from segments.tests.cases.case_base import BaseCase


class TestCreateView(BaseCase):
    def setUp(self):
        self._user = User.objects.create(
            first_name='Romário',
            last_name='Batista',
            email='fgpiaui@gmail.com',
            birth_date=date.today(),
            admission_date=date.today(),
            last_sign_in=datetime.now(),
            is_active=True,
            sex=MALE
        )
        self._tag = Tag.objects.create(name='Tecnologia')
    def test_create_user_success(self):
        data = {
            'first_name': 'Filipe',
            'last_name': 'Rodrigues',
            'email': 'fgpiaui@gmail.com',
            'birth_date': date.today(),
            'admission_date': date.today(),
            'last_sign_in': datetime.now(),
            'is_active': True,
            'sex': MALE
        }
        response = self.client.post(reverse('create_user'), data)
        resposta = User.objects.get(id=response.data['id'])
        self.assertEqual(response.data['id'], resposta.id)

    def test_create_tag_success(self):
        data = {
            'name':'Produtos'
        }
        response = self.client.post(reverse('create_tag'), data)
        resposta = Tag.objects.get(id=response.data['id'])
        self.assertEqual(response.data['id'], resposta.id)