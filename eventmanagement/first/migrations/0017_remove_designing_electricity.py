# Generated by Django 4.0.7 on 2023-03-04 07:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0016_remove_detail_rooms'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='designing',
            name='electricity',
        ),
    ]
