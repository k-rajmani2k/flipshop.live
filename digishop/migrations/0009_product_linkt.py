# Generated by Django 3.1.5 on 2021-04-07 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('digishop', '0008_auto_20210219_1701'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='linkt',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]