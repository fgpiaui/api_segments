from django.test import TestCase

from segments.tests.cases.case_tag import TagCase
from segments.tests.cases.case_user import UserCase
from segments.tests.cases.case_user_tag import UserTagCase


class BaseCase(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.users = UserCase().return_values()
        cls.tags = TagCase().return_values()

        UserTagCase(cls.users, cls.tags)

    @classmethod
    def tearDownClass(cls):
        pass

