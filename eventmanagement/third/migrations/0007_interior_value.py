# Generated by Django 4.0.7 on 2023-03-06 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('third', '0006_interior_quantity1_interior_quantity2_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='interior',
            name='value',
            field=models.CharField(max_length=150, null=True),
        ),
    ]
