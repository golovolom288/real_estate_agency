from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField


class Flat(models.Model):
    owner = models.CharField('ФИО владельца', max_length=200)
    owners_phonenumber = models.CharField('Номер владельца', max_length=20, default=0, null=True, blank=True)
    owner_pure_phone = PhoneNumberField(
        verbose_name='Номер нормализованный владельца',
        blank=True,
    )

    created_at = models.DateTimeField(
        'Когда создано объявление',
        default=timezone.now,
        db_index=True)

    description = models.TextField('Текст объявления', blank=True)
    price = models.IntegerField('Цена квартиры', db_index=True)
    new_building = models.BooleanField(verbose_name='Новостройка', default=None, null=True)
    town = models.CharField(
        'Город, где находится квартира',
        max_length=50,
        db_index=True)
    town_district = models.CharField(
        'Район города, где находится квартира',
        max_length=50,
        blank=True,
        help_text='Чертаново Южное')
    address = models.TextField(
        'Адрес квартиры',
        help_text='ул. Подольских курсантов д.5 кв.4')
    floor = models.CharField(
        'Этаж',
        max_length=3,
        help_text='Первый этаж, последний этаж, пятый этаж')

    rooms_number = models.IntegerField(
        'Количество комнат в квартире',
        db_index=True)
    living_area = models.IntegerField(
        'количество жилых кв.метров',
        null=True,
        blank=True,
        db_index=True)

    has_balcony = models.NullBooleanField('Наличие балкона', db_index=True)
    active = models.BooleanField('Активно-ли объявление', db_index=True)
    construction_year = models.IntegerField(
        'Год постройки здания',
        null=True,
        blank=True,
        db_index=True)
    likes = models.ManyToManyField(
        User,
        verbose_name='Лайки',
        blank=True,
    )

    def __str__(self):
        return f'{self.town}, {self.address} ({self.price}р.)'


class Report(models.Model):
    username = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="Кто жаловался",
        related_name="Жалобы")
    flat = models.ForeignKey(
        Flat,
        on_delete=models.CASCADE,
        verbose_name="Квартира на которую жаловались",
        related_name="Жалобы"
    )
    report = models.TextField()

    def __str__(self):
        return f'{self.username}, {self.flat}'


class Owner(models.Model):
    full_name = models.CharField(blank=True, null=True, default='', max_length=50, verbose_name="ФИО")
    owners_phonenumber = models.CharField('Номер владельца', max_length=20, default=0, null=True, blank=True)
    owner_pure_phone = PhoneNumberField(
        verbose_name='Номер нормализованный владельца',
        blank=True,
    )
    flats = models.ForeignKey(
        Flat,
        on_delete=models.CASCADE,
        verbose_name="Квартиры в собственности",
        related_name="Собственник"
    )
