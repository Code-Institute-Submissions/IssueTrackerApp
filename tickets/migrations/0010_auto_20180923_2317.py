# Generated by Django 2.1.1 on 2018-09-23 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0009_ticket_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='author',
            field=models.CharField(default='', max_length=150),
        ),
    ]
