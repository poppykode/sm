# Generated by Django 2.2.5 on 2019-10-03 04:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('enquiries', '0004_auto_20191002_1851'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enquiry',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='enquiries.Status'),
        ),
    ]
