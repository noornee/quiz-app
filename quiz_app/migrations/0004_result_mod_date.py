# Generated by Django 3.2.2 on 2021-06-17 22:10

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('quiz_app', '0003_auto_20210617_2236'),
    ]

    operations = [
        migrations.AddField(
            model_name='result',
            name='mod_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
