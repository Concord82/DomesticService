# Generated by Django 3.0.2 on 2020-02-03 16:07

from django.db import migrations
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ('catalogs', '0002_auto_20200203_1436'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goods',
            name='gdsCategories',
            field=mptt.fields.TreeForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogs.gdsCategories'),
        ),
    ]
