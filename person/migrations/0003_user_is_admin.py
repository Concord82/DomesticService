# Generated by Django 3.0.2 on 2020-02-02 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0002_user_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_admin',
            field=models.BooleanField(default=False),
        ),
    ]