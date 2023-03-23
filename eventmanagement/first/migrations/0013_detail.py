# Generated by Django 4.0.7 on 2023-03-03 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0012_delete_details'),
    ]

    operations = [
        migrations.CreateModel(
            name='detail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=150)),
                ('phonenumber', models.CharField(max_length=12)),
                ('address', models.CharField(max_length=12)),
                ('city', models.CharField(max_length=12)),
                ('country', models.CharField(max_length=12)),
                ('events', models.CharField(max_length=12)),
                ('food', models.CharField(max_length=12)),
                ('attendees', models.CharField(max_length=12)),
                ('date', models.CharField(max_length=12)),
                ('Time', models.CharField(max_length=12)),
                ('message', models.CharField(max_length=150)),
                ('table', models.CharField(max_length=150, null=True)),
                ('drinks', models.CharField(max_length=150, null=True)),
                ('beverages', models.CharField(max_length=150, null=True)),
                ('Alcohol', models.CharField(max_length=150, null=True)),
                ('banquet', models.CharField(max_length=150, null=True)),
                ('service', models.CharField(max_length=150, null=True)),
                ('Decoration', models.CharField(max_length=150, null=True)),
                ('skirting', models.CharField(max_length=150, null=True)),
                ('rooms', models.CharField(max_length=150, null=True)),
                ('report', models.BooleanField(default=False, null=True)),
            ],
        ),
    ]
