# Generated by Django 4.0 on 2022-12-01 14:58

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_finotchet_alter_film_id_alter_greatq_id'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='finotchet',
            options={},
        ),
        migrations.RemoveField(
            model_name='finotchet',
            name='article',
        ),
        migrations.RemoveField(
            model_name='finotchet',
            name='kvv',
        ),
        migrations.RemoveField(
            model_name='finotchet',
            name='logistics_amount',
        ),
        migrations.RemoveField(
            model_name='finotchet',
            name='reward',
        ),
        migrations.RemoveField(
            model_name='finotchet',
            name='selling_price',
        ),
        migrations.RemoveField(
            model_name='finotchet',
            name='type',
        ),
        migrations.RemoveField(
            model_name='finotchet',
            name='wb_price',
        ),
        migrations.AlterField(
            model_name='finotchet',
            name='date',
            field=models.DateField(default=datetime.datetime(2022, 12, 1, 14, 58, 10, 449252)),
        ),
        migrations.CreateModel(
            name='FinOtchetStats',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article', models.IntegerField(verbose_name='Артикул')),
                ('avarage_price', models.FloatField(blank=True, null=True, verbose_name='Средняя Цена ')),
                ('logistics_avarage', models.FloatField(blank=True, null=True, verbose_name='Средняя цен логистики')),
                ('logistics_return_avarage', models.FloatField(blank=True, null=True, verbose_name='Средняя цена возратов')),
                ('logistics_return_amount', models.IntegerField(verbose_name='Количество возратов')),
                ('logistics_amount', models.IntegerField(verbose_name='Количество доставок')),
                ('buyout_amount', models.IntegerField(verbose_name='Количество выкупов')),
                ('finotchet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.finotchet')),
            ],
        ),
        migrations.CreateModel(
            name='FinOtchetRows',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article', models.IntegerField(verbose_name='Артикул')),
                ('type', models.CharField(blank=True, max_length=10000, null=True, verbose_name='')),
                ('date', models.DateTimeField(blank=True, null=True, verbose_name='Дата')),
                ('wb_price', models.CharField(blank=True, max_length=10000, null=True, verbose_name='Цена на вб')),
                ('selling_price', models.CharField(blank=True, max_length=10000, null=True, verbose_name='Цена по которой продал вб')),
                ('kvv', models.FloatField(blank=True, max_length=10000, null=True, verbose_name='Размер комисии')),
                ('reward', models.CharField(blank=True, max_length=10000, null=True, verbose_name='К перечислению продавцу')),
                ('logistics_amount', models.FloatField(blank=True, null=True, verbose_name='Цена логистики')),
                ('stat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.finotchetstats')),
            ],
            options={
                'verbose_name': 'Otchet',
                'verbose_name_plural': 'Отчеты',
            },
        ),
    ]
