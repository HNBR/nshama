# Generated by Django 3.0.4 on 2020-04-01 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('printcerti', '0015_auto_20200401_1519'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='w_name',
            field=models.CharField(default='', max_length=18, verbose_name='اسمك الكامل'),
        ),
    ]
