# Generated by Django 5.0 on 2023-12-10 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_alter_sub_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='sub',
            name='d_remain',
            field=models.IntegerField(default=0),
        ),
    ]
