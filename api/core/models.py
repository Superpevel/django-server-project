from django.db import models
from django.db import models
from django.utils.translation import gettext_lazy as _
import datetime


class Film(models.Model):

    name = models.CharField(
        _('Номер договора'),
        max_length=255
    )

    year  =  models.IntegerField(_('Год'), blank=True,null=True)
    desciption  =  models.CharField(_('Описание'), blank=True,null=True,max_length=10000)

    link  =  models.CharField(_('Ссылка на фильм'), blank=True, max_length=100,null=True)

    sourse = models.CharField(_('Ресурс фильма'), blank=False, max_length=100,null=False)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = _('Фильм')
        verbose_name_plural = _('Фильмы')
# Create your models here.
class GreatQ(models.Model):

    name = models.CharField(
        _('Автор'),
        max_length=255
    )
    quote  =  models.CharField(_('Описание'), blank=True,null=True,max_length=10000)
    year  =  models.IntegerField(_('Год'), blank=True,null=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = _('Цитата')
        verbose_name_plural = _('Цитаты')

class FinOtchet(models.Model):
    date = models.DateField(default=datetime.datetime.now())

class FinOtchetStats(models.Model):

    article = models.IntegerField( _('Артикул'))
    avarage_price = models.FloatField(_('Средняя Цена '), blank=True,null=True)
    logistics_avarage = models.FloatField(_('Средняя цен логистики'), blank=True,null=True)
    logistics_return_avarage = models.FloatField(_('Средняя цена возратов'), blank=True,null=True)
    logistics_return_amount = models.IntegerField(_('Количество возратов'))
    logistics_amount = models.IntegerField(_('Количество доставок'))
    buyout_amount = models.IntegerField(_('Количество выкупов'))
    finotchet = models.ForeignKey(FinOtchet, on_delete=models.CASCADE)

class FinOtchetRows(models.Model):

    article = models.IntegerField( _('Артикул'))
    type  =  models.CharField(_(''), blank=True,null=True,max_length=10000)
    date = models.DateTimeField(_('Дата'), blank=True,null=True)
    wb_price =  models.CharField(_('Цена на вб'), blank=True,null=True,max_length=10000)
    selling_price = models.CharField(_('Цена по которой продал вб'), blank=True,null=True,max_length=10000)
    kvv = models.FloatField(_('Размер комисии'), blank=True,null=True,max_length=10000)
    reward = models.CharField(_('К перечислению продавцу'), blank=True,null=True,max_length=10000)
    logistics_amount  = models.FloatField(_('Цена логистики'), blank=True,null=True)
    stat = models.ForeignKey(FinOtchetStats, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.id}'

    class Meta:
        verbose_name = _('Otchet')
        verbose_name_plural = _('Отчеты')