from django import forms
from django.contrib.admin.widgets import AdminDateWidget

from purchase.models import Order
from product.models import Event

class DateInput(forms.DateInput):
    input_type = 'date'
    
class ChangeOrderForm(forms.Form):
    _selected_action = forms.CharField(widget=forms.MultipleHiddenInput)
    order = forms.ModelChoiceField(queryset=Order.objects.all(), label='Нове замовлення')
    

class AddEventForm(forms.Form):
    event = forms.ChoiceField(choices=Event.EVENT_CHOICES, label='Тип подія')
    date = forms.DateField(widget=DateInput, label='Дата події')
    comment = forms.CharField(label='Коментар')