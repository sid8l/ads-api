# Generated by Django 3.0.1 on 2020-01-12 14:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20200112_1425'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='main_photo',
        ),
    ]
