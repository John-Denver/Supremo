# Generated by Django 2.2 on 2019-04-19 16:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('STalk', '0003_auto_20190418_0537'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='deejay',
            name='contacts',
        ),
        migrations.RemoveField(
            model_name='deejay',
            name='email',
        ),
    ]
