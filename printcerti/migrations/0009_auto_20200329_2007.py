# Generated by Django 3.0.4 on 2020-03-29 17:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('printcerti', '0008_auto_20200329_1945'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='image',
        ),
        migrations.CreateModel(
            name='Certificate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='images')),
                ('person', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='printcerti.Person')),
            ],
        ),
    ]
