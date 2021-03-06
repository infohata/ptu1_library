# Generated by Django 4.0.4 on 2022-05-24 10:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('books', '0011_bookreview'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookreview',
            name='book',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='book_reviews', to='books.book', verbose_name='knyga'),
        ),
        migrations.AlterField(
            model_name='bookreview',
            name='reviewer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='book_reviews', to=settings.AUTH_USER_MODEL, verbose_name='skaitytojas'),
        ),
    ]
