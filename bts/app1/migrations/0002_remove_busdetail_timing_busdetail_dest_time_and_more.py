# Generated by Django 4.0.2 on 2022-03-08 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='busdetail',
            name='timing',
        ),
        migrations.AddField(
            model_name='busdetail',
            name='dest_time',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='busdetail',
            name='source_time',
            field=models.TimeField(blank=True, null=True),
        ),
    ]
