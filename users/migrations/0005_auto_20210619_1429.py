# Generated by Django 3.2.4 on 2021-06-19 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20210619_1418'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='result',
            name='department',
        ),
        migrations.RemoveField(
            model_name='result',
            name='level',
        ),
        migrations.AddField(
            model_name='profile',
            name='department',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='level',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
