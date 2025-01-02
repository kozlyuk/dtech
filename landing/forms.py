from django import forms
from django.core.mail import send_mail
from django.conf import settings

from .models import Message

class ContactForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['name', 'email', 'phone', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': "Ваше ім'я"}),
            'email': forms.TextInput(attrs={'placeholder': 'Ваш E-mail'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Ваш телефон'}),
            'message': forms.Textarea(attrs={'rows':5, 'placeholder': 'Текст повідомлення'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    def send_email(self):
        subject = 'Повідомлення від ' +  self.cleaned_data['name']
        message = "Ім'я: " + self.cleaned_data['name']
        message += 'Телефон: ' + (self.cleaned_data['phone'] or '')
        message += 'e-mail: ' + self.cleaned_data['email']
        message += 'Текст звернення: ' + self.cleaned_data['message'] or ''

        send_mail(
            subject,
            message,
            settings.DEFAULT_FROM_EMAIL,
            [settings.DEFAULT_TO_EMAIL],
            fail_silently=True,
        )