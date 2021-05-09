# Generated by Django 3.1.6 on 2021-02-09 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('varsity_id', models.IntegerField()),
                ('age', models.FloatField()),
                ('blood_group', models.CharField(max_length=10)),
                ('section', models.CharField(max_length=10)),
                ('email', models.CharField(max_length=20)),
                ('gender', models.CharField(max_length=10)),
                ('phone', models.CharField(max_length=15)),
            ],
        ),
    ]
