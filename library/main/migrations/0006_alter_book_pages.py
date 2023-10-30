# Generated by Django 4.2.5 on 2023-10-09 16:20

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_book_visitor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='pages',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1)]),
        ),
    ]
