# Generated by Django 4.1.3 on 2022-11-04 19:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0003_task_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='date',
        ),
    ]