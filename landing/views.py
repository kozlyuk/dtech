from django.views.generic.base import TemplateView


class MainView(TemplateView):
    template_name = 'index.html'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['news'] = News.objects.filter(is_active=True)
    #     context['partners'] = Partner.objects.all()
    #     context['solutions'] = Solution.objects.all()
    #     return context