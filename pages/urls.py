from django.urls import path

from . import views

app_name = 'pages'

urlpatterns = [
    path('about/', views.AboutUsView.as_view(), name='about'),
    path('contact-us/', views.ContactUsView.as_view(), name='contact_us'),
]