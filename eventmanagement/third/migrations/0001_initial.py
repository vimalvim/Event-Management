# Generated by Django 4.0.7 on 2023-02-21 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='tevents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=150)),
                ('phonenumber', models.CharField(max_length=12)),
                ('gender', models.CharField(max_length=10)),
                ('password', models.CharField(max_length=150)),
            ],
        ),
    ]
