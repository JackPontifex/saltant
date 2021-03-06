# Generated by Django 2.0.6 on 2018-07-02 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0019_auto_20180630_2208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskinstance',
            name='state',
            field=models.CharField(choices=[('CREATED', 'created'), ('PUBLISHED', 'published'), ('RUNNING', 'running'), ('SUCCESSFUL', 'successful'), ('FAILED', 'failed'), ('REVOKED', 'revoked')], default='CREATED', max_length=10),
        ),
    ]
