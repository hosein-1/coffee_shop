from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from django.db.models import Prefetch
from cart.cart import Cart
from .forms import OrderForm
from .models import OrderItem, Order


@login_required
def order_create_view(request):
    order_form = OrderForm()
    cart = Cart(request)

    if len(cart) == 0:
        messages.warning(request, 'سبد خرید شما خالی است، لطفا محصولی را به سبد خرید اضافه کنید.')
        return redirect('products:products_list')

    if request.method == 'POST':
        order_form = OrderForm(request.POST)

        if order_form.is_valid():
            order_object = order_form.save(commit=False)
            order_object.user = request.user
            order_object.save()

            for item in cart:
                product = item['product_obj']
                OrderItem.objects.create(
                    order=order_object,
                    product=product,
                    quantity=item['quantity'],
                    price=product.price,
                )

            cart.clear()

            request.session['order_id'] = order_object.id
            return redirect('payment:payment_process')

    return render(request, 'orders/order_create.html', {'form': order_form})


class UserOrdersList(LoginRequiredMixin,ListView):
    template_name = 'orders/user_orders.html'
    context_object_name = 'orders'
    paginate_by = 3
    
    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)\
        .prefetch_related(Prefetch(
            'items',
             queryset=OrderItem.objects.select_related('product'))).all()\
        .order_by('-datetime_created')
