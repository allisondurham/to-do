# Generated by Django 3.2.9 on 2021-11-19 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_rename_text_todo_task'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='due_date',
            field=models.TextField(blank=True, null=True),
        ),
    ]
