from django.urls import path
from django.views.generic import TemplateView
from landing import views

urlpatterns = [
    path('', views.MainFormView.as_view(), name='main'),
    path('thanks', TemplateView.as_view(template_name="thanks.html"), name='thanks_page'),

]
