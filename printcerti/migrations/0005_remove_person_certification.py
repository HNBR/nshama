# Generated by Django 3.0.4 on 2020-03-28 23:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('printcerti', '0004_auto_20200329_0224'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='certification',
        ),
    ]
