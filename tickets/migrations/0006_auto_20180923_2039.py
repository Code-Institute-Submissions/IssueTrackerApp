# Generated by Django 2.1.1 on 2018-09-23 18:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0005_auto_20180923_1827'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ticket',
            old_name='tag',
            new_name='tags',
        ),
    ]
