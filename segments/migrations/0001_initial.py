# Generated by Django 3.2.9 on 2021-11-09 01:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=100)),
                ('birth_date', models.DateField()),
                ('admission_date', models.DateField()),
                ('last_sign_in', models.DateTimeField()),
                ('is_active', models.BooleanField(default=True)),
                ('sex', models.CharField(choices=[('male', 'male'), ('female', 'female')], max_length=6)),
            ],
        ),
        migrations.CreateModel(
            name='UserTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='segments.tag')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='segments.user')),
            ],
        ),
    ]