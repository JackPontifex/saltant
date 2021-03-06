# Generated by Django 2.0.6 on 2018-06-24 21:35

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0006_auto_20180624_2110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskinstance',
            name='arguments',
            field=django.contrib.postgres.fields.jsonb.JSONField(default=dict, help_text='A JSON dictionary of arguments, where the keys are the argument name and the values are their corresponding values'),
        ),
        migrations.AlterField(
            model_name='tasktype',
            name='default_arguments',
            field=django.contrib.postgres.fields.jsonb.JSONField(default=dict, help_text='A JSON dictionary of default arguments, where the keys are the argument names and the values are their corresponding default values'),
        ),
        migrations.AlterField(
            model_name='tasktype',
            name='required_arguments',
            field=django.contrib.postgres.fields.jsonb.JSONField(default=list, help_text='A JSON array of required argument names'),
        ),
    ]
