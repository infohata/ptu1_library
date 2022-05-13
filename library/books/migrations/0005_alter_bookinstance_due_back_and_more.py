# Generated by Django 4.0.4 on 2022-05-13 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_alter_bookinstance_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookinstance',
            name='due_back',
            field=models.DateField(blank=True, db_index=True, null=True, verbose_name='grąžinama'),
        ),
        migrations.AlterField(
            model_name='bookinstance',
            name='status',
            field=models.CharField(blank=True, choices=[('a', 'administruojama'), ('p', 'paimta'), ('g', 'galima paimti'), ('r', 'rezervuota')], db_index=True, default='a', max_length=1, verbose_name='statusas'),
        ),
    ]
