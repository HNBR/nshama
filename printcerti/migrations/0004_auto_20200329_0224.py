# Generated by Django 3.0.4 on 2020-03-28 23:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('printcerti', '0003_auto_20200328_0612'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='certification',
            field=models.ImageField(blank=True, upload_to='certification'),
        ),
    ]
