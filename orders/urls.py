from django.urls import path

from . import views

app_name = 'orders'

urlpatterns = [
    path('order-create/', views.order_create_view, name='order_create'),
    path('user_orders/', views.UserOrdersList.as_view(), name='user_orders'),
]