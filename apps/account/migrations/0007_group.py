# Generated by Django 2.2 on 2020-04-16 14:35

import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
        ('account', '0006_auto_20200401_1547'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('group_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='auth.Group')),
            ],
            bases=('auth.group',),
            managers=[
                ('objects', django.contrib.auth.models.GroupManager()),
            ],
        ),
    ]
