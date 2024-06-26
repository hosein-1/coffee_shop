from django.urls import path

from . import views

app_name = 'cart'

urlpatterns = [

    path('add/<int:product_id>', views.add_to_cart, name='add_to_cart'),
    path('add/', views.add_to_cart, name='add_to_cart'),
    path('detail/', views.cart_detail, name='cart_detail'),
    path('update/', views.update_cart, name='update_cart'),
    path('remove-product/', views.remove_product, name='remove_product'),
]