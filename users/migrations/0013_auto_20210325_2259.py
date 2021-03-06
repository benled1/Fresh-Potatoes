# Generated by Django 3.1.7 on 2021-03-25 22:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_auto_20210309_2051'),
    ]

    operations = [
        migrations.CreateModel(
            name='WatchLaterEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('media_type', models.CharField(max_length=100)),
                ('movie_id', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='profile',
            name='watchlater',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.watchlaterentry'),
        ),
    ]
