# Generated by Django 3.1.5 on 2021-01-20 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sentence',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('japanese', models.TextField()),
                ('english', models.TextField()),
            ],
        ),
    ]
