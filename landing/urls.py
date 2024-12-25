from django.urls import path
from landing import views

urlpatterns = [
    path('', views.MainView.as_view(), name='main'),
    # path('about_us/', views.AboutUs.as_view(), name='about_us'),
    # path('contact/', views.ContactFormView.as_view(), name='contact_form'),
    # path('thanks/', TemplateView.as_view(template_name="thanks.html"), name='thanks_page'),
    # path('news/', views.NewsList.as_view(), name='news_list'),
    # path('new/<int:pk>/detail/', views.NewsDetail.as_view(), name='news_detail'),
    # path('projects/', views.ProjectList.as_view(), name='project_list'),
    # path('project/<int:pk>/detail/', views.ProjectDetail.as_view(), name='project_detail'),
]
