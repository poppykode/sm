# Generated by Django 2.2.5 on 2019-10-12 04:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoices', '0004_auto_20191011_2009'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='address',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='invoice',
            name='company_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='total',
            field=models.CharField(default='00,00', max_length=255),
        ),
    ]
