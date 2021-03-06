# Generated by Django 2.1.3 on 2019-01-07 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('detail', models.TextField()),
                ('city_map', models.TextField(blank=True)),
                ('sal_delay', models.IntegerField(default=400)),
                ('img', models.CharField(max_length=200)),
            ],
        ),
    ]
