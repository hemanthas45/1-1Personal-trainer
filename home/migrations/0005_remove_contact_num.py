# Generated by Django 3.0.5 on 2021-12-29 09:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_contact'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='num',
        ),
    ]