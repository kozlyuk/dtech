from django.db import models


class Message(models.Model):
    name = models.CharField("Ім'я", max_length=100)
    email = models.EmailField('E-mail')
    phone = models.CharField('Телефон', max_length=13)
    message = models.TextField('Повідомлення')
    created = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = 'Повідомлення'
        verbose_name_plural = 'Повідомлення'
        ordering = ['created']

    def __str__(self):
        return self.name