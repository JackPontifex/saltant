# Generated by Django 2.0.6 on 2018-07-04 22:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0021_auto_20180703_2358'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskinstance',
            name='task_queue',
            field=models.ForeignKey(default=1, help_text='The queue this instance runs on. If left blank, then the default queue is used.', on_delete=django.db.models.deletion.PROTECT, to='tasks.TaskQueue'),
            preserve_default=False,
        ),
    ]