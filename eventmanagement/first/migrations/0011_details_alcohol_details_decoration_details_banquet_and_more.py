# Generated by Django 4.0.7 on 2023-03-03 04:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0010_designing_electricity_designing_structure_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='details',
            name='Alcohol',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='details',
            name='Decoration',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='details',
            name='banquet',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='details',
            name='beverages',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='details',
            name='drinks',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='details',
            name='rooms',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='details',
            name='service',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='details',
            name='skirting',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='details',
            name='table',
            field=models.CharField(max_length=150, null=True),
        ),
    ]