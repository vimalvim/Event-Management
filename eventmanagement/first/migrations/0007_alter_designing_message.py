# Generated by Django 4.0.7 on 2023-02-27 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0006_designing_feet'),
    ]

    operations = [
        migrations.AlterField(
            model_name='designing',
            name='message',
            field=models.CharField(max_length=150, null=True),
        ),
    ]