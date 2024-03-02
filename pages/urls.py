from django.urls import path

from . import views


urlpatterns = [
    path('about/', views.AboutUsView.as_view(), name='about'),
    path('contact-us/', views.ContactUs.as_view(), name='contact_us'),
]