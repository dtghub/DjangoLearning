# Generated by Django 2.2.5 on 2022-03-22 18:52

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('starting_date', models.DateField(default=datetime.date.today)),
                ('course_description', models.CharField(max_length=512)),
            ],
        ),
    ]
