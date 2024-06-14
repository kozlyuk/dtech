""" Models for managing purchases """

from django.utils.translation import gettext_lazy as _
from django.db import models

from accounts.models import User
from structure.models import Customer

class Order(models.Model):
    """ Model contains Sales, Carts """
    Created = 'CR'
    InWork = 'IW'
    Accepted = 'AC'
    Sent = 'SE'
    STATUS_CHOICES = (
        (Created, _('Created')),
        (InWork, _('In work')),
        (Accepted, _('Accepted from producer')),
        (Sent, _('Sent to customer')),
    )
    
    customer = models.ForeignKey(Customer, verbose_name=_('Customer'), on_delete=models.CASCADE)
    deal_number = models.CharField(_('Deal number'), max_length=45)
    value = models.DecimalField(_('Price'), max_digits=8, decimal_places=2, default=0)
    status = models.CharField(_('Order status'), max_length=2, choices=STATUS_CHOICES, default=Created)
    number_of_devices = models.PositiveSmallIntegerField(_('Number of devices'), blank=True, null=True)
    comment = models.CharField(_('Comment'), max_length=255, blank=True)

    # Creating information
    creator = models.ForeignKey(User, verbose_name='Створив', related_name='order_creators', on_delete=models.PROTECT)
    creation_date = models.DateField(auto_now_add=True)


    class Meta:
        verbose_name = _('Order')
        verbose_name_plural = _('Orders')
        ordering = ['-creation_date', 'deal_number']

    def __str__(self):
        return self.deal_number

    # def save(self, *args, logging=True, **kwargs):
    #     if not self.pk:
    #         # Bulk create devices
    #         self.serial_number = Device.objects.aggregate(Max('serial_number'))['serial_number__max'] + 1
    #     super().save(*args, **kwargs)
                