# Generated by Django 4.0.7 on 2023-03-17 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0022_detail_specialized'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detail',
            name='Events',
            field=models.CharField(max_length=50, null=True),
        ),
    ]