from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from cart.cart import Cart
from .forms import OrderForm
from .models import OrderItem


@login_required
def order_create_view(request):
    order_form = OrderForm()
    cart = Cart(request)

    if len(cart) == 0:
        messages.warning(request, 'سبد خرید شما خالی است، لطفا محصولی را به سبد خرید اضافه کنید.')
        return redirect('products:products_list')

    if request.method == 'POST':
        print(request.POST)
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
