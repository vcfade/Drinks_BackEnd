# Generated by Django 2.2.2 on 2019-06-04 16:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20190604_1216'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='rol',
            new_name='role_id',
        ),
    ]
