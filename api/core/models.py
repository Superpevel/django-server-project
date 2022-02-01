from django.db import models
from django.db import models
from django.utils.translation import gettext_lazy as _


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