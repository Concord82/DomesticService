# Generated by Django 3.0.2 on 2020-02-03 14:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogs', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='gdscategories',
            old_name='parents',
            new_name='parent',
        ),
    ]
