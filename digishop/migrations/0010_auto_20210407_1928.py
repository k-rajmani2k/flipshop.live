# Generated by Django 3.1.5 on 2021-04-07 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('digishop', '0009_product_linkt'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='thumbnail',
            field=models.ImageField(null=True, upload_to='uploads/thumbnail'),
        ),
    ]
