# Generated by Django 2.2.5 on 2019-11-06 08:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('faulty_logging', '0004_auto_20191105_1102'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('decription', models.TextField(blank=True, null=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('fault', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='faulty_logging.FaultyLogging')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_content_type', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
