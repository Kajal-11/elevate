# Generated by Django 3.0.7 on 2021-04-23 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0024_auto_20210422_2329'),
    ]

    operations = [
        migrations.AddField(
            model_name='industry',
            name='number',
            field=models.IntegerField(default=0),
        ),
    ]
