# Generated by Django 4.2.7 on 2023-12-09 11:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_sub_email_sent'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sub',
            name='email_sent',
        ),
    ]