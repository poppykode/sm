# Generated by Django 2.2.5 on 2019-10-09 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enquiries', '0018_comment_user'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-timestamp']},
        ),
        migrations.AlterField(
            model_name='enquiry',
            name='status',
            field=models.CharField(choices=[('new', 'New'), ('open', 'Open'), ('lost', 'Lost'), ('won', 'Won')], default='new', max_length=255),
        ),
    ]
