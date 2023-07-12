# Generated by Django 4.2.2 on 2023-07-12 14:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Loan',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date_exit', models.DateField(auto_now_add=True)),
                ('date_devolution', models.DateField(null=True)),
                ('returned', models.BooleanField(default=False)),
                ('copy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='loans_copies', to='books.copy')),
            ],
        ),
    ]
