# Generated by Django 4.0.7 on 2023-02-24 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0005_designing'),
    ]

    operations = [
        migrations.AddField(
            model_name='designing',
            name='feet',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
