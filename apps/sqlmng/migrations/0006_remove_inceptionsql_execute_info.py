# Generated by Django 2.2 on 2020-04-08 06:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sqlmng', '0005_auto_20200406_2029'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inceptionsql',
            name='execute_info',
        ),
    ]
