# Generated by Django 3.1.7 on 2021-03-01 03:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20210301_0314'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='nutrition',
            name='caffeine_mg',
        ),
        migrations.RemoveField(
            model_name='nutrition',
            name='protein_g',
        ),
        migrations.RemoveField(
            model_name='nutrition',
            name='saturated_fat_g',
        ),
        migrations.RemoveField(
            model_name='nutrition',
            name='size_fluid_ounce',
        ),
        migrations.RemoveField(
            model_name='nutrition',
            name='size_ml',
        ),
        migrations.RemoveField(
            model_name='nutrition',
            name='sodium_mg',
        ),
    ]
