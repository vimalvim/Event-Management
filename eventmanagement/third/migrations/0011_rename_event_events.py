# Generated by Django 4.0.7 on 2023-03-06 09:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('third', '0010_event_report_interior_report'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='event',
            new_name='events',
        ),
    ]
