from datetime import date, datetime
from faker import Faker
from segments.constantes import MALE, FEMALE
from segments.models import User
from segments.tests.cases.case_singleton import SingletonCase

fake = Faker()

class UserCase(metaclass=SingletonCase):
    def __init__(self):
        self.list_names = []

        for i in range(500):
                User.objects.create(
                first_name=f"{fake.first_name()}_{i}",
                last_name=f"{fake.last_name()}_{i}",
                email=fake.email(),
                birth_date=fake.date_of_birth(),
                admission_date=date.today(),
                last_sign_in=datetime.now(),
                is_active=fake.boolean(),
                sex=FEMALE if fake.boolean() else MALE
                )

    def return_values(self):
        return User.objects.all()

