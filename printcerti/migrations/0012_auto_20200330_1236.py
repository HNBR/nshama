# Generated by Django 3.0.4 on 2020-03-30 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('printcerti', '0011_auto_20200329_2153'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certificate',
            name='image',
            field=models.ImageField(blank=True, default='D:\\nshama\\certi\\images\\test.jpeg', upload_to='images'),
        ),
        migrations.AlterField(
            model_name='person',
            name='w_name',
            field=models.CharField(default='', max_length=60, verbose_name='اسمك الكامل'),
        ),
    ]
