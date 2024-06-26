from django.shortcuts import get_object_or_404, render
from django.views.decorators.http import require_POST
from django.http import JsonResponse

from products.models import Product
from products.serializers import ProductSerializer
from .cart import Cart


@require_POST
def add_to_cart(request, product_id=None):


    if product_id is None:
        product_id = request.POST.get('item_id')

    try:
        cart = Cart(request)
        product = get_object_or_404(Product, id=product_id)

        cart.add(product)
        products = Product.objects.filter(id__in=request.session['cart'])
        cart_ser = ProductSerializer(products, many=True)


        context = {
            'cart_ser': cart_ser.data,
            'item_count': len(cart),
            'cart_total_price': cart.get_total_price()
        }
    
        return JsonResponse(context)

    except:
        return JsonResponse(status=400, data={'error': 'invalid request'})


def cart_detail(request):
    cart = Cart(request)

    context = {
        'cart': cart,
    }
    return render(request, 'cart/cart_detail.html', context)


@require_POST
def update_cart(request):
    item_id = request.POST.get('item_id')
    action = request.POST.get('action')

    try:
        product = get_object_or_404(Product, id=item_id)
        cart = Cart(request)

        if action == 'add':
            cart.add(product)
        
        else:
            cart.reduce(product)

        context = {
            'item_count': len(cart),
            'cart_total_price': cart.get_total_price(),
            'quantity': cart.cart[item_id]['quantity'],
            'total_price_product': cart.cart[item_id]['price'] * cart.cart[item_id]['quantity'],
            'final_price': cart.get_total_price(),
            'success': True,
        }        

        return JsonResponse(context)
    except:
        return JsonResponse(status=404, data={'sucess': False, 'error': 'item not found'})


@require_POST
def remove_product(request):
    item_id = request.POST.get('item_id')


    try:
        product = get_object_or_404(Product, id=item_id)
        cart = Cart(request)
        cart.remove(product)
        products = Product.objects.filter(id__in=request.session['cart'])
        cart_ser = ProductSerializer(products, many=True)

        context = {
            'cart_ser': cart_ser.data,
            'item_count': len(cart),
            'cart_total_price': cart.get_total_price(),
            'final_price': cart.get_total_price(),
            'success': True,
        }

        return JsonResponse(context)
    except:
        return JsonResponse(status=404, data={'sucess': False, 'error': 'item not found'})