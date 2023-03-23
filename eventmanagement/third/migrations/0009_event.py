# Generated by Django 4.0.7 on 2023-03-06 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('third', '0008_delete_event'),
    ]

    operations = [
        migrations.CreateModel(
            name='event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('table', models.CharField(max_length=150)),
                ('quantity', models.CharField(max_length=150)),
                ('projector', models.CharField(max_length=150)),
                ('quantity1', models.CharField(max_length=150)),
                ('mike', models.CharField(max_length=150)),
                ('quantity2', models.CharField(max_length=150)),
                ('Tv', models.CharField(max_length=150)),
                ('quantity3', models.CharField(max_length=150)),
                ('conditions', models.CharField(max_length=150)),
                ('quantity4', models.CharField(max_length=150)),
                ('led', models.CharField(max_length=150)),
                ('quantity5', models.CharField(max_length=150)),
                ('value', models.CharField(max_length=150)),
            ],
        ),
    ]
