# Generated by Django 2.2.5 on 2019-11-04 20:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('faulty_logging', '0002_auto_20191104_2233'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='faultylogging',
            name='next_follow_up',
        ),
    ]
