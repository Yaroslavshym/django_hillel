# Generated by Django 4.2.5 on 2023-10-09 15:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_visitor_book_visitor'),
    ]

    operations = [
        migrations.RenameField(
            model_name='author',
            old_name='has_bad_moode',
            new_name='has_bad_temper',
        ),
    ]
