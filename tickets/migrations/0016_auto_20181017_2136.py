# Generated by Django 2.1.2 on 2018-10-17 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0015_ticket_payments'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='payments',
            field=models.IntegerField(default=0),
        ),
    ]
