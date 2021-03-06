# Generated by Django 3.2.4 on 2022-01-06 23:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20220107_0236'),
    ]

    operations = [
        migrations.AlterField(
            model_name='film',
            name='desciption',
            field=models.IntegerField(blank=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='film',
            name='link',
            field=models.CharField(blank=True, max_length=100, verbose_name='Ссылка на фильм'),
        ),
        migrations.AlterField(
            model_name='film',
            name='sourse',
            field=models.CharField(max_length=100, verbose_name='Ресурс фильма'),
        ),
        migrations.AlterField(
            model_name='film',
            name='year',
            field=models.IntegerField(blank=True, verbose_name='Год'),
        ),
    ]
