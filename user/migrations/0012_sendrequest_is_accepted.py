# Generated by Django 3.0.7 on 2021-04-14 23:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0011_sendrequest'),
    ]

    operations = [
        migrations.AddField(
            model_name='sendrequest',
            name='is_accepted',
            field=models.BooleanField(default=False),
        ),
    ]