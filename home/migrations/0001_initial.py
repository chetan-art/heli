# Generated by Django 4.0.4 on 2022-04-14 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Polymodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('polygon1', models.JSONField(max_length=255)),
                ('polygon2', models.JSONField(max_length=255)),
            ],
        ),
    ]
