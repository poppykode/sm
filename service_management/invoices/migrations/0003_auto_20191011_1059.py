# Generated by Django 2.2.5 on 2019-10-11 08:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('invoices', '0002_invoice'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='invoice',
            name='description',
        ),
        migrations.RemoveField(
            model_name='invoice',
            name='quantity',
        ),
        migrations.RemoveField(
            model_name='invoice',
            name='unit_price',
        ),
        migrations.CreateModel(
            name='LineItems',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('quantity', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.TextField()),
                ('unit_price', models.CharField(blank=True, max_length=255, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('invoice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='invoices.Invoice')),
            ],
        ),
    ]
