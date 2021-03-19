# Generated by Django 2.2.5 on 2020-01-13 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0007_task_completed'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['timestamp']},
        ),
        migrations.AlterField(
            model_name='projectinstallationassessement',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('in-progress', 'In progress'), ('on-hold', 'On hold'), ('completed', 'completed'), ('abandoned', 'Abandoned')], default='pending', max_length=255),
        ),
        migrations.AlterField(
            model_name='projectinstallationassessement',
            name='type',
            field=models.CharField(choices=[('assement', 'Assessement'), ('project', 'Project'), ('installation', 'Installation')], max_length=255),
        ),
    ]