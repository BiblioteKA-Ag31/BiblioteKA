# Generated by Django 4.2.2 on 2023-07-11 15:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0012_alter_copy_number_received'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='copy',
            name='number_received',
        ),
    ]
