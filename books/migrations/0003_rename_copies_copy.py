# Generated by Django 4.2.2 on 2023-07-03 15:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('loans', '0001_initial'),
        ('books', '0002_copies'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Copies',
            new_name='Copy',
        ),
    ]