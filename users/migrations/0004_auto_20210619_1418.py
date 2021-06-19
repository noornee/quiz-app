# Generated by Django 3.2.4 on 2021-06-19 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20210619_1310'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='department',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='level',
        ),
        migrations.AddField(
            model_name='result',
            name='department',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='result',
            name='level',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]