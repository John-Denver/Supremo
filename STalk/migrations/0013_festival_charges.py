# Generated by Django 2.2 on 2019-05-17 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('STalk', '0012_festival'),
    ]

    operations = [
        migrations.AddField(
            model_name='festival',
            name='charges',
            field=models.CharField(default=0, max_length=250),
        ),
    ]
