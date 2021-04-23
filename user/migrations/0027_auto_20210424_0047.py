# Generated by Django 3.2 on 2021-04-23 19:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0024_auto_20210422_2329'),
        ('user', '0026_alter_team_first_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='rawmaterialbuy',
            name='quantity_3',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='rawmaterialbuy',
            name='quantity_4',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='rawmaterialbuy',
            name='raw_material_3',
            field=models.ForeignKey(blank=True, limit_choices_to={'raw_material': True}, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='RawMaterial3', to='home.item'),
        ),
        migrations.AddField(
            model_name='rawmaterialbuy',
            name='raw_material_4',
            field=models.ForeignKey(blank=True, limit_choices_to={'raw_material': True}, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='RawMaterial4', to='home.item'),
        ),
    ]