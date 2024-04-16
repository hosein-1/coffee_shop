from django.urls import path

from .views import payment_process_sandbox, payment_callback_sandbox

app_name = 'payment'

urlpatterns = [
    path('process/', payment_process_sandbox, name='payment_process'),
    path('callback/', payment_callback_sandbox, name='payment_callback')
]