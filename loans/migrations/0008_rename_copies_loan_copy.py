# Generated by Django 4.2.2 on 2023-07-12 12:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('loans', '0007_alter_loan_copies'),
    ]

    operations = [
        migrations.RenameField(
            model_name='loan',
            old_name='copies',
            new_name='copy',
        ),
    ]