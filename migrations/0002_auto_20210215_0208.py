# Generated by Django 3.1.6 on 2021-02-15 13:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='age',
        ),
        migrations.RemoveField(
            model_name='student',
            name='gender',
        ),
        migrations.RemoveField(
            model_name='student',
            name='section',
        ),
    ]