# Generated by Django 2.2.25 on 2022-02-01 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_alter_film_desciption'),
    ]

    operations = [
        migrations.CreateModel(
            name='GreatQ',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Автор')),
                ('quote', models.CharField(blank=True, max_length=10000, null=True, verbose_name='Описание')),
                ('year', models.IntegerField(blank=True, null=True, verbose_name='Год')),
            ],
            options={
                'verbose_name': 'Цитата',
                'verbose_name_plural': 'Цитаты',
            },
        ),
        migrations.AlterField(
            model_name='film',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]