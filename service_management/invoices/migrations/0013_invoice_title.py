# Generated by Django 2.2.5 on 2020-01-13 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoices', '0012_auto_20191119_1018'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='title',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
