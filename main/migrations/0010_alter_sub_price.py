# Generated by Django 5.0 on 2023-12-10 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_sub_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sub',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=7),
        ),
    ]
