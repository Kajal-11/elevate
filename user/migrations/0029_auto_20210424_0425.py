# Generated by Django 3.0.7 on 2021-04-23 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0028_merge_20210424_0359'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='first_name',
            field=models.CharField(blank=True, max_length=30, verbose_name='first name'),
        ),
    ]
