# Generated by Django 4.1.6 on 2023-02-28 10:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restapp', '0004_staff'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctor',
            name='image',
        ),
    ]
