# Generated by Django 4.2.5 on 2023-10-09 15:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_author_authordetails_book_author'),
    ]

    operations = [
        migrations.CreateModel(
            name='Visitor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='visitor',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.RESTRICT, to='main.visitor'),
        ),
    ]
