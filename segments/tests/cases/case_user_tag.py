import random

from segments.models import UserTag, User, Tag
from segments.tests.cases.case_singleton import SingletonCase


class UserTagCase(metaclass=SingletonCase):
    def __init__(self, users, tags):
        for user in users:
            tag = random.choice(tags)
            UserTag.objects.create(
                    user=user,
                    tag=tag
            )
