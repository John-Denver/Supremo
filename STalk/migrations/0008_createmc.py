# Generated by Django 2.2 on 2019-04-29 17:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('STalk', '0007_remove_mc_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='CreateMc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Mc_name', models.CharField(max_length=20)),
                ('mc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='STalk.Mc')),
            ],
        ),
    ]
