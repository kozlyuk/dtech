""" Models for managing products """

from datetime import datetime
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.db.models import Max
from .formatChecker import ContentTypeRestrictedFileField
from crum import get_current_user

from accounts.models import User
from purchase.models import Order
from structure.models import Contractor


def docs_directory_path(filename):
    """  file will be uploaded to MEDIA_ROOT/invoices/Year/Month/<filename> """
    return 'docs/{0}/{1}/{2}'.format(filename, datetime.now().year, datetime.now().month)


class ComponentType(models.Model):
    """ Model contains Component Types """
    name = models.CharField(_('Component Type'), max_length=255, unique=True)

    class Meta:
        verbose_name = _('Component Type')
        verbose_name_plural = _('Component Types')

    def __str__(self):
        return self.name


class Component(models.Model):
    """ Model contains Components """
    name = models.CharField(_('Product title'), max_length=255, unique=True)
    short_description = models.TextField(_('Short description'))
    component_type = models.ForeignKey(ComponentType, on_delete=models.PROTECT)
    image = models.ImageField(_('Product image'), upload_to='product/', blank=True, null=True)
    specifications_url = models.URLField(_('Specification'), blank=True, null=True)

    # Creating information
    creator = models.ForeignKey(User, verbose_name='Created', related_name='task_creators', on_delete=models.PROTECT)
    creation_date = models.DateField(auto_now_add=True)
    
    class Meta:
        verbose_name = _('Component')
        verbose_name_plural = _('Components')

    def __str__(self):
        return self.name


class Configuration(models.Model):
    """ Model contains Configurations """
    name = models.CharField(_('Product title'), max_length=255, unique=True)
    short_description = models.TextField(_('Short description'))
    image = models.ImageField(_('Product image'), upload_to='product/', blank=True, null=True)
    components = models.ManyToManyField(Component)
    manual = ContentTypeRestrictedFileField(_('Product manual'), upload_to=docs_directory_path,
                                              content_types=['application/pdf',
                                                             'application/vnd.openxmlformats-officedocument.'
                                                             'spreadsheetml.sheet',
                                                             'application/vnd.openxmlformats-officedocument.'
                                                             'wordprocessingml.document'],
                                              max_upload_size=26214400,
                                              blank=True, null=True)
    specifications_url = models.URLField(_('Specification'), blank=True, null=True)

    # Creating information
    creator = models.ForeignKey(User, verbose_name=_('Creator'), related_name='configuration_creators', on_delete=models.PROTECT)
    creation_date = models.DateField(auto_now_add=True)
    
    class Meta:
        verbose_name = _('Configuration')
        verbose_name_plural = _('Configurations')
        ordering = ['id']

    def __str__(self):
        return self.name


class Device(models.Model):
    """ Model contains Devices """

    serial_number = models.IntegerField(_('Serial number'), blank=True, null=True, unique=True)
    executor = models.ForeignKey(Contractor, verbose_name=_('Executor'), on_delete=models.PROTECT)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    configuration = models.ForeignKey(Configuration, on_delete=models.PROTECT)
    status = models.CharField(_('Status'), max_length=30)

    # Creating information
    creation_date = models.DateField(auto_now_add=True)
    
    class Meta:
        verbose_name = _('Device')
        verbose_name_plural = _('Devices')

    def __str__(self):
        return str(self.serial_number)
    
    def save(self, *args, **kwargs):
        if not self.serial_number:
            self.serial_number = Device.objects.aggregate(Max('serial_number'))['serial_number__max'] + 1
        super().save(*args, **kwargs)
        last_event = self.event_set.last()
        self.status = last_event.get_event_display() if last_event else _('Issued for work')
        super().save(*args, **kwargs, update_fields=['status'])


class Event(models.Model):

    Issued = 'IS'
    FrameAssembly = 'FA'
    BasicAssembly = 'BA'
    FinalAssembly = 'FI'
    Accepted = 'AC'
    Configured = 'CO'
    Tested = 'TE'
    Sent = 'SE'
    Rejected = 'RE'
    Fixed = 'FX'
    Other = 'OT'
    EVENT_CHOICES = (
        (Issued, _('Issued for work')),
        (FrameAssembly, _('Frame assembly')),
        (BasicAssembly, _('Basic assembly')),
        (FinalAssembly, _('Final assembly')),
        (Accepted, _('Accepted from producer')),
        (Configured, _('Configured')),
        (Tested, _('Tested')),
        (Rejected, _('Rejected')),
        (Sent, _('Sent to customer')),
        (Fixed, _('Fixed')),
        (Other, _('Other')),
    )
    
    device = models.ForeignKey(Device, verbose_name= _('Device'), on_delete=models.PROTECT)
    date = models.DateField('Date')
    event = models.CharField(_('Event'), max_length=2, choices=EVENT_CHOICES, default=Issued)
    comment = models.CharField('Comment', max_length=255, blank=True, null=True)
    creator = models.ForeignKey(User, verbose_name= _('Creator'), null=True, on_delete=models.SET_NULL)

    class Meta:
        verbose_name = _('Event')
        verbose_name_plural = _('Events')
        ordering = ['date', 'pk']
        unique_together = ['device', 'event']

    def __str__(self):
        return f'{self.date} - {self.event}'
    
    def save(self, *args, **kwargs):
        if not self.pk:
            self.creator = get_current_user()
        super().save(*args, **kwargs)
        self.device.save()