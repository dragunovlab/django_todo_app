# Generated by Django 5.1.6 on 2025-02-20 05:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Название задачи')),
                ('completed', models.BooleanField(default=False, verbose_name='Выполнено')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
            ],
        ),
        migrations.CreateModel(
            name='SubTask',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Название подзадачи')),
                ('completed', models.BooleanField(default=False, verbose_name='Выполнено')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='advanced_todo_list.task')),
            ],
        ),
    ]
