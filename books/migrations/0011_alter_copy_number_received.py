# Generated by Django 4.2.2 on 2023-07-11 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0010_alter_book_quant_copies_alter_book_quant_pag_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='copy',
            name='number_received',
            field=models.PositiveIntegerField(default=1),
        ),
    ]