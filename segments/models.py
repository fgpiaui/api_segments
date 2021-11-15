from django.db import models

from segments.constantes import SEX


class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=100)
    birth_date = models.DateField()
    admission_date = models.DateField()
    last_sign_in = models.DateTimeField()
    is_active = models.BooleanField(default=True)
    sex = models.CharField(max_length=6, choices=SEX)

    class Meta:
        unique_together=('first_name', 'last_name')

class Tag(models.Model):
    name = models.CharField(max_length=50)

class UserTag(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)

