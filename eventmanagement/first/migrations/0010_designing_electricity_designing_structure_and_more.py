# Generated by Django 4.0.7 on 2023-03-01 03:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0009_designing_floor_designing_walls'),
    ]

    operations = [
        migrations.AddField(
            model_name='designing',
            name='electricity',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='designing',
            name='structure',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='designing',
            name='ventilation',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='designing',
            name='windows',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
