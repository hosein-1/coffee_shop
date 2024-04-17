from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView
from django.contrib.messages.views import SuccessMessageMixin

from .models import Contact

class AboutUsView(TemplateView):
    template_name = 'pages/about.html'


class ContactUsView(TemplateView):
    template_name = 'pages/contact_us.html'


class ContactUsCreateView(SuccessMessageMixin ,CreateView):
    model = Contact
    fields = ['full_name', 'phone_number', 'title', 'content']
    success_url = reverse_lazy('pages:contact_us')
    success_message = 'نظر شما با موفقیت برای ما ارسال شد.'

