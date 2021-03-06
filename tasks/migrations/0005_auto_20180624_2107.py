# Generated by Django 2.0.6 on 2018-06-24 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0004_auto_20180624_0356'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskinstance',
            name='uuid',
            field=models.CharField(editable=False, help_text='The UUID for the running job', max_length=36, null=True, verbose_name='UUID'),
        ),
    ]
