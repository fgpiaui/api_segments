# Generated by Django 3.2.9 on 2021-11-15 02:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('segments', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='user',
            unique_together={('first_name', 'last_name')},
        ),
    ]
