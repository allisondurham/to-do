# Generated by Django 3.2.9 on 2021-11-26 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_alter_todo_due_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='created_date',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='todo',
            name='due_date',
            field=models.TextField(blank=True, null=True),
        ),
    ]
