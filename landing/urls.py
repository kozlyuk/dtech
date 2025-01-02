from django.urls import path
from landing import views

urlpatterns = [
    path('', views.MainFormView.as_view(), name='main'),

]
