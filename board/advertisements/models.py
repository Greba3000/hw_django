from django.db import models

# Create your models here.


class Advertisement(models.Model):
    title = models.CharField(max_length=1500, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True)
    price = models.FloatField(verbose_name='Цена', default=0)
    views_count = models.IntegerField(verbose_name='Количество просмотров', default=0)
    status = models.ForeignKey('AdvertisementStatus', default=None, null=True, on_delete=models.CASCADE,
                               related_name='advertisements', verbose_name='Статус')
    type = models.ForeignKey('AdvertisementType', default=None, null=True, on_delete=models.CASCADE,
                             related_name='advertisements',  verbose_name='Тип объявления')
    author = models.ForeignKey('AdvertisementAuthor', default=None, null=True, on_delete=models.CASCADE,
                               related_name='advertisements', verbose_name='Автор')
    heading = models.ForeignKey('AdvertisementHeading', default=None, null=True, on_delete=models.CASCADE,
                                related_name='advertisements', verbose_name='Рубрика')

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'advertisements1'


class AdvertisementStatus(models.Model):
    name = models.CharField(max_length=100, default='', verbose_name='Статус')

    def __str__(self):
        return self.name


class AdvertisementType(models.Model):
    type = models.CharField(max_length=100, default='', verbose_name='Тип')

    def __str__(self):
        return self.type


class AdvertisementHeading(models.Model):
    heading = models.CharField(max_length=100, default='')

    def __str__(self):
        return self.heading


class AdvertisementAuthor(models.Model):
    name = models.CharField(max_length=100, default='')
    email = models.CharField(max_length=100, default='')
    tel = models.CharField(max_length=100, default='')

    def __str__(self):
        return self.name
