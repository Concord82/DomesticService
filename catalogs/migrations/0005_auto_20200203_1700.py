# Generated by Django 3.0.2 on 2020-02-03 17:00

from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ('catalogs', '0004_goods_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Operations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='Category Name')),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='catalogs.Operations')),
            ],
            options={
                'verbose_name': 'Operation',
                'verbose_name_plural': 'Operations',
            },
        ),
        migrations.AlterModelOptions(
            name='goods',
            options={'verbose_name': 'Good', 'verbose_name_plural': 'Goods'},
        ),
        migrations.AlterField(
            model_name='goods',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8, verbose_name='Price'),
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='Category Name')),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='catalogs.Products')),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
            },
        ),
        migrations.CreateModel(
            name='PriceOperations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=8, verbose_name='Price')),
                ('opearation', mptt.fields.TreeForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogs.Operations')),
                ('product', mptt.fields.TreeForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogs.Products')),
            ],
            options={
                'verbose_name': 'Price Operation',
                'verbose_name_plural': 'Price Operations',
            },
        ),
    ]
