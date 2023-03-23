# Generated by Django 4.0.7 on 2023-03-03 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('third', '0002_event'),
    ]

    operations = [
        migrations.CreateModel(
            name='interior',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('table', models.CharField(max_length=150)),
                ('kitchen', models.CharField(max_length=150)),
                ('dining', models.CharField(max_length=150)),
                ('kids', models.CharField(max_length=150)),
                ('living', models.CharField(max_length=150)),
                ('quantity', models.CharField(max_length=150)),
            ],
        ),
    ]
