# Generated by Django 4.0.4 on 2022-06-08 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0012_alter_bookreview_book_alter_bookreview_reviewer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='isbn',
            field=models.CharField(help_text='13 Simbolių<a href="https://www.isbn-international.org/content/what-isbn" target="_blank">ISBN kodas</a>', max_length=13, verbose_name='ISBN'),
        ),
    ]