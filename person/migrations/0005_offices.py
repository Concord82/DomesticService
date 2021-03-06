# Generated by Django 3.0.2 on 2020-02-03 21:06

from django.db import migrations, models
import person.models


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0004_user_address'),
    ]

    operations = [
        migrations.CreateModel(
            name='Offices',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='office name')),
                ('short_code', models.CharField(help_text='Set Short code for current office', max_length=5, verbose_name='Short Code')),
                ('phone', models.CharField(blank=True, max_length=12, unique=True, validators=[person.models.validate_phone], verbose_name='Phone Number')),
                ('address', models.CharField(max_length=128, verbose_name='address')),
                ('address_api', models.TextField(blank=True, verbose_name='address API')),
                ('enabled', models.BooleanField(default=False, verbose_name='enabled')),
                ('start_time', models.TimeField(blank=True, verbose_name='Start work time')),
                ('start_out', models.TimeField(blank=True, verbose_name='Start orders out')),
                ('end_time', models.TimeField(blank=True, verbose_name='End work time')),
            ],
            options={
                'verbose_name': 'Office',
                'verbose_name_plural': 'Offices',
            },
        ),
    ]
