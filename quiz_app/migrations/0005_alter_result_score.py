# Generated by Django 3.2.4 on 2021-06-17 23:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz_app', '0004_result_mod_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='result',
            name='score',
            field=models.FloatField(default=0),
        ),
    ]
