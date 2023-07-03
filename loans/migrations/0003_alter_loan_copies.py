# Generated by Django 4.2.2 on 2023-07-03 15:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_alter_copy_book'),
        ('loans', '0002_loan_copies'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loan',
            name='copies',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='loans_book_copies', to='books.copy'),
        ),
    ]
