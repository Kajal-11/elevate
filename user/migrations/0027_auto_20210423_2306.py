# Generated by Django 3.0.7 on 2021-04-23 17:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0026_auto_20210423_2247'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rawmaterialbuy',
            name='quantity_3',
        ),
        migrations.RemoveField(
            model_name='rawmaterialbuy',
            name='quantity_4',
        ),
        migrations.RemoveField(
            model_name='rawmaterialbuy',
            name='raw_material_3',
        ),
        migrations.RemoveField(
            model_name='rawmaterialbuy',
            name='raw_material_4',
        ),
    ]