# Generated by Django 5.2.3 on 2025-06-23 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('travel_class', models.CharField(max_length=20)),
                ('origin', models.CharField(max_length=10)),
                ('destination', models.CharField(max_length=10)),
                ('departure_time', models.DateTimeField()),
                ('arrival_time', models.DateTimeField()),
                ('flight_numbers', models.JSONField()),
                ('legs', models.JSONField()),
                ('last_seen', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='TaskResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_id', models.CharField(max_length=255, unique=True)),
                ('status', models.CharField(max_length=50)),
                ('result', models.TextField()),
                ('date_done', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
