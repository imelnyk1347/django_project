# Generated by Django 3.1 on 2020-08-22 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=200)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('body', models.TextField(blank=True, db_index=True)),
                ('date_public', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
