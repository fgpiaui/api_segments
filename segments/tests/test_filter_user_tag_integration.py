import json
import random

from django.db.models import Q
from django.urls import reverse

from segments.constantes import EXACT, AND, CONTAINS, STARTS_WITH, END_WITH, DATE, OR, NOT, \
    NOR, MIN_DATE, MAX_DATE
from segments.models import UserTag
from segments.tests.cases.case_base import BaseCase


class TestIntegrationFilterUserTag(BaseCase):
    def setUp(self):
        super(TestIntegrationFilterUserTag, self).setUpClass()
        self.user = random.choice(self.users)
        self.tag = random.choice(self.tags)
        self.dict_test = dict()

    def aux_build_case_test(self, list):
        case = []
        for item in list:
            case.append({
                'field': item[0],
                'value': item[1],
                'type': item[2],
                'operator': item[3],
            })

        return case


    def test_filter_first_name_and_exact(self):
        list = [
            ['user__first_name', self.user.first_name, EXACT, AND]
        ]
        data = [{'fields':self.aux_build_case_test(list)}]

        response = self.client.post(reverse('filter'), json.dumps(data), content_type='application/json')
        gabarito = UserTag.objects.filter(user__first_name=self.user.first_name)
        self.assertEqual(len(response.data), len(gabarito))

    def test_filter_first_name_or_exact(self):
        list = [
            ['user__first_name', self.user.first_name, EXACT, AND],
            ['tag__name', self.tag.name, EXACT, OR]
        ]
        data = [{'fields':self.aux_build_case_test(list)}]

        response = self.client.post(reverse('filter'), json.dumps(data), content_type='application/json')
        gabarito = UserTag.objects.filter(Q(user__first_name=self.user.first_name) | Q(tag__name=self.tag.name))
        self.assertEqual(len(response.data), len(gabarito))

    def test_filter_first_name_not_exact(self):
        list = [
            ['user__first_name', self.user.first_name, EXACT, AND],
            ['tag__name', self.tag.name, EXACT, NOT]
        ]
        data = [{'fields':self.aux_build_case_test(list)}]

        response = self.client.post(reverse('filter'), json.dumps(data), content_type='application/json')
        gabarito = UserTag.objects.filter(Q(user__first_name=self.user.first_name) & ~Q(tag__name=self.tag.name))
        self.assertEqual(len(response.data), len(gabarito))

    def test_filter_first_name_nor_exact(self):
        list = [
            ['user__first_name', self.user.first_name, EXACT, AND],
            ['tag__name', self.tag.name, EXACT, NOR]
        ]
        data = [{'fields':self.aux_build_case_test(list)}]

        response = self.client.post(reverse('filter'), json.dumps(data), content_type='application/json')
        gabarito = UserTag.objects.filter(Q(user__first_name=self.user.first_name) | ~Q(tag__name=self.tag.name))
        self.assertEqual(len(response.data), len(gabarito))

    def test_filter_first_name_and_contains(self):
        size_string = len(self.user.first_name)
        name = self.user.first_name[1:size_string-2]
        list = [
            ['user__first_name', name, CONTAINS, AND],
            ['tag__name', self.tag.name, EXACT, AND]
        ]
        data = [{'fields':self.aux_build_case_test(list)}]

        response = self.client.post(reverse('filter'), json.dumps(data), content_type='application/json')
        gabarito = UserTag.objects.filter(Q(user__first_name__icontains=name) & Q(tag__name=self.tag.name))
        self.assertEqual(len(response.data), len(gabarito))

    def test_filter_first_name_or_contains(self):
        size_string = len(self.user.first_name)
        name = self.user.first_name[1:size_string-2]
        list = [
            ['user__first_name', name, CONTAINS, AND],
            ['tag__name', self.tag.name, EXACT, OR]
        ]
        data = [{'fields':self.aux_build_case_test(list)}]

        response = self.client.post(reverse('filter'), json.dumps(data), content_type='application/json')
        gabarito = UserTag.objects.filter(Q(user__first_name__icontains=name) | Q(tag__name=self.tag.name))
        self.assertEqual(len(response.data), len(gabarito))

    def test_filter_first_name_not_contains(self):
        size_string = len(self.user.first_name)
        name = self.user.first_name[1:size_string-2]
        list = [
            ['user__first_name', name, CONTAINS, AND],
            ['tag__name', self.tag.name, EXACT, NOT]
        ]
        data = [{'fields':self.aux_build_case_test(list)}]

        response = self.client.post(reverse('filter'), json.dumps(data), content_type='application/json')
        gabarito = UserTag.objects.filter(Q(user__first_name__icontains=name) & ~Q(tag__name=self.tag.name))
        self.assertEqual(len(response.data), len(gabarito))

    def test_filter_first_name_nor_contains(self):
        size_string = len(self.user.first_name)
        name = self.user.first_name[1:size_string-2]
        list = [
            ['user__first_name', name, CONTAINS, AND],
            ['tag__name', self.tag.name, EXACT, NOR]
        ]
        data = [{'fields':self.aux_build_case_test(list)}]

        response = self.client.post(reverse('filter'), json.dumps(data), content_type='application/json')
        gabarito = UserTag.objects.filter(Q(user__first_name__icontains=name) | ~Q(tag__name=self.tag.name))
        self.assertEqual(len(response.data), len(gabarito))

    def test_filter_first_name_and_startswith(self):
        name = self.user.first_name[0]
        list = [
            ['user__first_name', name, STARTS_WITH, AND],
            ['tag__name', self.tag.name, EXACT, AND]
        ]
        data = [{'fields':self.aux_build_case_test(list)}]

        response = self.client.post(reverse('filter'), json.dumps(data), content_type='application/json')
        gabarito = UserTag.objects.filter(Q(user__first_name__startswith=name) & Q(tag__name=self.tag.name))
        self.assertEqual(len(response.data), len(gabarito))

    def test_filter_first_name_or_startswith(self):
        name = self.user.first_name[0]
        list = [
            ['user__first_name', name, STARTS_WITH, AND],
            ['tag__name', self.tag.name, EXACT, OR]
        ]
        data = [{'fields':self.aux_build_case_test(list)}]

        response = self.client.post(reverse('filter'), json.dumps(data), content_type='application/json')
        gabarito = UserTag.objects.filter(Q(user__first_name__startswith=name) | Q(tag__name=self.tag.name))
        self.assertEqual(len(response.data), len(gabarito))

    def test_filter_first_name_not_startswith(self):
        name = self.user.first_name[0]
        list = [
            ['user__first_name', name, STARTS_WITH, AND],
            ['tag__name', self.tag.name, EXACT, NOT]
        ]
        data = [{'fields':self.aux_build_case_test(list)}]

        response = self.client.post(reverse('filter'), json.dumps(data), content_type='application/json')
        gabarito = UserTag.objects.filter(Q(user__first_name__startswith=name) & ~Q(tag__name=self.tag.name))
        self.assertEqual(len(response.data), len(gabarito))

    def test_filter_first_name_nor_startswith(self):
        name = self.user.first_name[0]
        list = [
            ['user__first_name', name, STARTS_WITH, AND],
            ['tag__name', self.tag.name, EXACT, NOR]
        ]
        data = [{'fields':self.aux_build_case_test(list)}]

        response = self.client.post(reverse('filter'), json.dumps(data), content_type='application/json')
        gabarito = UserTag.objects.filter(Q(user__first_name__startswith=name) | ~Q(tag__name=self.tag.name))
        self.assertEqual(len(response.data), len(gabarito))

    def test_filter_first_name_and_endswith(self):
        name = self.user.first_name[-1]
        list = [
            ['user__first_name', name, END_WITH, AND],
            ['tag__name', self.tag.name, EXACT, AND]
        ]
        data = [{'fields':self.aux_build_case_test(list)}]

        response = self.client.post(reverse('filter'), json.dumps(data), content_type='application/json')
        gabarito = UserTag.objects.filter(Q(user__first_name__endswith=name) & Q(tag__name=self.tag.name))
        self.assertEqual(len(response.data), len(gabarito))

    def test_filter_first_name_or_endswith(self):
        name = self.user.first_name[-1]
        list = [
            ['user__first_name', name, END_WITH, AND],
            ['tag__name', self.tag.name, EXACT, OR]
        ]
        data = [{'fields':self.aux_build_case_test(list)}]

        response = self.client.post(reverse('filter'), json.dumps(data), content_type='application/json')
        gabarito = UserTag.objects.filter(Q(user__first_name__endswith=name) | Q(tag__name=self.tag.name))
        self.assertEqual(len(response.data), len(gabarito))

    def test_filter_first_name_not_endswith(self):
        name = self.user.first_name[-1]
        list = [
            ['user__first_name', name, END_WITH, AND],
            ['tag__name', self.tag.name, EXACT, NOT]
        ]
        data = [{'fields':self.aux_build_case_test(list)}]

        response = self.client.post(reverse('filter'), json.dumps(data), content_type='application/json')
        gabarito = UserTag.objects.filter(Q(user__first_name__endswith=name) & ~Q(tag__name=self.tag.name))
        self.assertEqual(len(response.data), len(gabarito))

    def test_filter_first_name_nor_endswith(self):
        name = self.user.first_name[-1]
        list = [
            ['user__first_name', name, END_WITH, AND],
            ['tag__name', self.tag.name, EXACT, NOR]
        ]
        data = [{'fields':self.aux_build_case_test(list)}]

        response = self.client.post(reverse('filter'), json.dumps(data), content_type='application/json')
        gabarito = UserTag.objects.filter(Q(user__first_name__endswith=name) | ~Q(tag__name=self.tag.name))
        self.assertEqual(len(response.data), len(gabarito))

    def test_filter_first_name_and_date(self):
        name = {MIN_DATE:'1980-01-01', MAX_DATE:'2010-01-01'}
        list = [
            ['user__birth_date', name, DATE, AND],
            ['tag__name', self.tag.name, EXACT, AND]
        ]
        data = [{'fields':self.aux_build_case_test(list)}]

        response = self.client.post(reverse('filter'), json.dumps(data), content_type='application/json')
        gabarito = UserTag.objects.filter(Q(user__birth_date__gte=name[MIN_DATE],
                                            user__birth_date__lte=name[MAX_DATE])
                                          & Q(tag__name=self.tag.name))
        self.assertEqual(len(response.data), len(gabarito))

    def test_filter_first_name_or_date(self):
        name = {MIN_DATE:'1980-01-01', MAX_DATE:'2010-01-01'}
        list = [
            ['user__birth_date', name, DATE, AND],
            ['tag__name', self.tag.name, EXACT, OR]
        ]
        data = [{'fields':self.aux_build_case_test(list)}]

        response = self.client.post(reverse('filter'), json.dumps(data), content_type='application/json')
        gabarito = UserTag.objects.filter(Q(user__birth_date__gte=name[MIN_DATE],
                                            user__birth_date__lte=name[MAX_DATE])
                                          | Q(tag__name=self.tag.name))
        self.assertEqual(len(response.data), len(gabarito))

    def test_filter_first_name_not_date(self):
        name = {MIN_DATE:'1980-01-01', MAX_DATE:'2010-01-01'}
        list = [
            ['user__birth_date', name, DATE, AND],
            ['tag__name', self.tag.name, EXACT, NOT]
        ]
        data = [{'fields':self.aux_build_case_test(list)}]

        response = self.client.post(reverse('filter'), json.dumps(data), content_type='application/json')
        gabarito = UserTag.objects.filter(Q(user__birth_date__gte=name[MIN_DATE],
                                            user__birth_date__lte=name[MAX_DATE])
                                          & ~Q(tag__name=self.tag.name))
        self.assertEqual(len(response.data), len(gabarito))

    def test_filter_first_name_nor_date(self):
        name = {MAX_DATE:'2010-01-01'}
        list = [
            ['user__birth_date', name, DATE, AND],
            ['tag__name', self.tag.name, EXACT, NOR]
        ]
        data = [{'fields':self.aux_build_case_test(list)}]

        response = self.client.post(reverse('filter'), json.dumps(data), content_type='application/json')
        gabarito = UserTag.objects.filter(Q(user__birth_date__lte=name[MAX_DATE])
                                          | ~Q(tag__name=self.tag.name))
        self.assertEqual(len(response.data), len(gabarito))

    def test_filter_first_name_nor_date_or_and_first_name(self):
        name = {MIN_DATE:'1980-01-01', MAX_DATE:'2010-01-01'}
        list = [
            ['user__birth_date', name, DATE, AND],
            ['tag__name', self.tag.name, EXACT, NOR]
        ]
        list_2 = [
            ['user__first_name', self.user.first_name, EXACT, AND],
        ]
        data = [{'fields':self.aux_build_case_test(list)}, {'fields':self.aux_build_case_test(list)}]

        response = self.client.post(reverse('filter'), json.dumps(data), content_type='application/json')
        gabarito = UserTag.objects.filter(Q(Q(user__birth_date__gte=name[MIN_DATE],
                                            user__birth_date__lte=name[MAX_DATE])
                                          | ~Q(tag__name=self.tag.name))
                                          | Q(user__first_name=self.user.first_name))
        self.assertEqual(len(response.data), len(gabarito))