# Generated by Django 3.0.4 on 2020-03-29 02:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('printcerti', '0005_remove_person_certification'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='first_name',
            field=models.CharField(max_length=30, verbose_name='First names'),
        ),
        migrations.AlterField(
            model_name='person',
            name='last_name',
            field=models.CharField(max_length=30, verbose_name='Last name'),
        ),
        migrations.AlterField(
            model_name='person',
            name='medium_name',
            field=models.CharField(max_length=30, verbose_name='Middle name'),
        ),
    ]
