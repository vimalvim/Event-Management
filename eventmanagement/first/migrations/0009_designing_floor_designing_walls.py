# Generated by Django 4.0.7 on 2023-02-28 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0008_alter_details_message'),
    ]

    operations = [
        migrations.AddField(
            model_name='designing',
            name='floor',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='designing',
            name='walls',
            field=models.CharField(max_length=50, null=True),
        ),
    ]