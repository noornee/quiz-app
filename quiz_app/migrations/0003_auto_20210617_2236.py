# Generated by Django 3.2.2 on 2021-06-17 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz_app', '0002_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='result',
            name='score',
            field=models.IntegerField(default=0),
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
