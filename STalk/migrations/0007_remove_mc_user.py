# Generated by Django 2.2 on 2019-04-27 16:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('STalk', '0006_auto_20190423_0922'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mc',
            name='user',
        ),
    ]
