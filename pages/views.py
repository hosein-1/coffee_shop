from django.shortcuts import render
from django.views.generic import TemplateView


class AboutUsView(TemplateView):
    template_name = 'pages/about.html'


class ContactUsView(TemplateView):
    template_name = 'pages/contact_us.html'
