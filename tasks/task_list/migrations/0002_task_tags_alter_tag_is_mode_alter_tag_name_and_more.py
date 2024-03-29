# Generated by Django 5.0.1 on 2024-02-02 07:17

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task_list', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='tags',
            field=models.ManyToManyField(blank=True, help_text='Tags or labels associated with the task.', related_name='tasks', to='task_list.tag', verbose_name='Tags'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='is_mode',
            field=models.BooleanField(default=False, help_text='Indicates if the tag is a mode.', verbose_name='Is Mode'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(help_text='Name of the tag.', max_length=100, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='task',
            name='complete',
            field=models.BooleanField(default=False, help_text='Indicates if the task is complete.', verbose_name='Complete'),
        ),
        migrations.AlterField(
            model_name='task',
            name='due_date',
            field=models.DateTimeField(help_text='Date when a task is due', verbose_name='Due Date'),
        ),
        migrations.AlterField(
            model_name='task',
            name='important',
            field=models.BooleanField(default=False, help_text='Indicates if the task is important', verbose_name='Important'),
        ),
        migrations.AlterField(
            model_name='task',
            name='name',
            field=models.CharField(help_text='Name of the task.', max_length=200, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='task',
            name='time_spent',
            field=models.IntegerField(blank=True, help_text='Time spent on the task.', null=True, verbose_name='Complete'),
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField(blank=True)),
                ('profile_picture', models.URLField(blank=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Tag_task',
        ),
    ]
