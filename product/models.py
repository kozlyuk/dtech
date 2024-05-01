""" Models for managing products """

from datetime import datetime
from django.db import models
from django.utils.translation import gettext_lazy as _
from .formatChecker import ContentTypeRestrictedFileField

from accounts.models import User


def docs_directory_path(filename):
    """  file will be uploaded to MEDIA_ROOT/invoices/Year/Month/<filename> """
    return 'docs/{0}/{1}/{2}'.format(filename, datetime.now().year, datetime.now().month)


    Created = 'CR'
    InWork = 'IW'
    Accepted = 'AC'
    Configured = 'CO'
    Tested = 'TE'
    Sent = 'SE'
    Rejected = 'RE'
    Fixed = 'FI'
    STATUS_CHOICES = (
        (Created, _('Created')),
        (InWork, _('In work')),
        (Accepted, _('Accepted from producer')),
        (Configured, _('Configured')),
        (Tested, _('Tested')),
        (Sent, _('Sent to customer')),
        (Rejected, _('Rejected')),
        (Fixed, _('Fixed')),
    )

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
    image = models.ImageField(_('Product image'), upload_to='product/')
    specifications_url = models.URLField(_('Specification'), blank=True, null=True)

    # Creating information
    creator = models.ForeignKey(User, verbose_name='Створив', related_name='task_creators', on_delete=models.PROTECT)
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
    image = models.ImageField(_('Product image'), upload_to='product/')
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
    creator = models.ForeignKey(User, verbose_name='Створив', related_name='configuration_creators', on_delete=models.PROTECT)
    creation_date = models.DateField(auto_now_add=True)
    
    class Meta:
        verbose_name = _('Configuration')
        verbose_name_plural = _('Configurations')
        ordering = ['id']

    def __str__(self):
        return self.name


class Device(models.Model):
    """ Model contains Devices """
    serial_number = models.CharField(_('Serial number'), max_length=32, unique=True)
    short_description = models.TextField(_('Short description'))
    configuration = models.ForeignKey(Configuration, on_delete=models.PROTECT)

    # Creating information
    creator = models.ForeignKey(User, verbose_name='Створив', related_name='device_creators', on_delete=models.PROTECT)
    creation_date = models.DateField(auto_now_add=True)
    
    class Meta:
        verbose_name = _('Device')
        verbose_name_plural = _('Devices')

    def __str__(self):
        return self.name


class Batch(models.Model):
    """ Model contains Batches """
    devices = models.ManyToManyField(Device)
    quantity = models.PositiveSmallIntegerField(_('Number of devices'))
    short_description = models.TextField(_('Short description'))

    # Creating information
    creator = models.ForeignKey(User, verbose_name='Створив', related_name='batch_creators', on_delete=models.PROTECT)
    creation_date = models.DateField(auto_now_add=True)
    
    class Meta:
        verbose_name = _('Batch')
        verbose_name_plural = _('Batches')

    def __str__(self):
        return self.name
