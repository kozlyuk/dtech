from django.views.generic import CreateView
from django.urls import reverse_lazy

from .forms import ContactForm


class MainFormView(CreateView):
    template_name = 'index.html'
    form_class = ContactForm
    success_url = reverse_lazy('thanks_page')

# def form_valid(self, form):
#   form.instance.created_by = self.request.user
#   return super().form_valid(form)