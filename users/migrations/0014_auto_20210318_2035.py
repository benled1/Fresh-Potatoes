# Generated by Django 3.1.6 on 2021-03-19 03:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0013_auto_20210318_2032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='movies',
            field=models.CharField(default='', max_length=1000),
        ),
    ]
