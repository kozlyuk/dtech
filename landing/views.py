from django.views.generic.edit import FormView
from django.urls import reverse_lazy

from .forms import ContactForm


class MainFormView(FormView):
    template_name = 'index.html'
    form_class = ContactForm
    success_url = reverse_lazy('thanks_page')

    def form_valid(self, form):
        form.save()
        form.send_email()
        return super().form_valid(form)