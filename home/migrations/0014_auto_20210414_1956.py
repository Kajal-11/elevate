# Generated by Django 3.0.7 on 2021-04-14 14:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_delete_manufacture'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='product',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='item',
            name='raw_material',
            field=models.BooleanField(default=False),
        ),
        migrations.CreateModel(
            name='Manufacture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('product', models.ForeignKey(blank=True, limit_choices_to={'raw_material': True}, null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.Item')),
            ],
        ),
    ]