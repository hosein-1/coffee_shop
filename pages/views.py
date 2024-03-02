from django.shortcuts import render
from django.views.generics import TemplateView


class AboutUsView(TemplateView):
    template_name = 'pages/about.html'


class ContactUs(TemplateView):
    template_name = 'pages/contact_us.html'
