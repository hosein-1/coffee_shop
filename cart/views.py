from django.shortcuts import get_object_or_404, render
from django.views.decorators.http import require_POST
from django.http import JsonResponse

from products.models import Product
from .cart import Cart


@require_POST
def add_to_cart(request, product_id):
    print(request.session.get('cart'))
    try:
        cart = Cart(request)
        product = get_object_or_404(Product, id=product_id)

        cart.add(product)

        context = {
            'item_count': len(cart),
            # 'total_price': cart.get_total_price()
        }
        return JsonResponse(context)

    except:
        return JsonResponse({'error': 'invalid request'})


def cart_detail(request):
    cart = Cart(request)

    context = {
        'cart': cart,
    }
    return render(request, 'cart/cart_detail.html', context)
