from django.db import models

from accounts.models import User


class Requisites(models.Model):
    name = models.CharField('Назва', max_length=50, unique=True)
    full_name = models.CharField('Повна назва', max_length=100, blank=True)
    edrpou = models.CharField('ЄДРПОУ', max_length=10, blank=True)
    city = models.CharField('Місто', max_length=30, blank=True)
    legal = models.CharField('Опис контрагента', max_length=255, blank=True)
    legal_description = models.CharField('Організаційно-правова форма', max_length=255, blank=True)
    regulations = models.CharField('Діє на підставі', max_length=100, blank=True)
    signatory_person = models.CharField('Підписант', max_length=50, blank=True)
    signatory_position = models.CharField('Посада підписанта', max_length=255, blank=True)
    requisites = models.TextField('Реквізити', blank=True)
    bank_requisites = models.TextField('Банківські реквізити', blank=True)

    class Meta:
        abstract = True
        

class Customer(Requisites):
    contact_person = models.CharField('Контактна особа', max_length=50)
    phone = models.CharField('Телефон', max_length=13)
    email = models.EmailField('Email')
    debtor_term = models.PositiveSmallIntegerField('Термін післяоплати', blank=True, null=True)
    user = models.OneToOneField(User, on_delete=models.SET_NULL, blank=True, null=True)
    active = models.BooleanField('Активний', default=True)

    class Meta:
        verbose_name = 'Замовник'
        verbose_name_plural = 'Замовники'

    def __str__(self):
        return self.name


class Company(Requisites):
    TAXATION_CHOICES = (
        ('wvat', 'З ПДВ'),
        ('wovat', 'Без ПДВ'),
    )
    chief = models.ForeignKey(User, verbose_name='Керівник', related_name='company_chiefs', on_delete=models.PROTECT)
    accountant = models.ForeignKey(User, verbose_name='Бухгалтер', related_name='company_accountant', on_delete=models.PROTECT)
    taxation = models.CharField('Система оподаткування', max_length=5, choices=TAXATION_CHOICES, default='wvat')
    active = models.BooleanField('Активний', default=True)

    class Meta:
        verbose_name = 'Компанія'
        verbose_name_plural = 'Компанії'

    def __str__(self):
        return self.name


class Contractor(models.Model):
    name = models.CharField('Назва', max_length=50, unique=True)
    edrpou = models.CharField('ЄДРПОУ', max_length=10, blank=True)
    contact_person = models.CharField('Контактна особа', max_length=50, blank=True)
    phone = models.CharField('Телефон', max_length=13, blank=True)
    email = models.EmailField('Email', blank=True)
    requisites = models.TextField('Реквізити', blank=True)
    active = models.BooleanField('Активний', default=True)

    class Meta:
        verbose_name = 'Контрагент'
        verbose_name_plural = 'Контрагенти'

    def __str__(self):
        return self.name
