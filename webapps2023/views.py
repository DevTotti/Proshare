from django.views.generic import TemplateView


class Homeview(TemplateView):
    template_name = "accounts/home.html"
