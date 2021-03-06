# Generated by Django 2.2.5 on 2019-10-02 16:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('enquiries', '0003_auto_20191002_1848'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enquiry',
            name='channel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='channel', to='enquiries.Channel'),
        ),
        migrations.AlterField(
            model_name='enquiry',
            name='service',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='enquiries.Service'),
        ),
        migrations.AlterField(
            model_name='enquiry',
            name='service_mode',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='service_mode', to='enquiries.Channel'),
        ),
    ]
