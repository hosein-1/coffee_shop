from django.shortcuts import redirect, reverse, render
from django.shortcuts import get_object_or_404
from django.conf import settings
from django.http import HttpResponse
from django.contrib import messages

from orders.models import Order
import requests
import json


def payment_process_sandbox(request):
    # get order id from session
    order_id = request.session.get('order_id')
    order = get_object_or_404(Order, id=order_id)
    toman_total_price = order.get_total_price()
    rial_total_price = toman_total_price * 10

    zarinpal_request_url = 'https://sandbox.zarinpal.com/pg/rest/WebGate/PaymentRequest.json'

    request_header = {
        'accept': 'application/json',
        'content-type': 'application/json',
    }
    request_data = {
        'MerchantID': 'abcABCabcABCabcABCabcABCabcABCabcABC',
        'Amount': rial_total_price,
        'Description': f'#{order.id}: {order.user.first_name} {order.user.last_name}',
        # 'callback_url': 'http://127.0.0.1:8000' + reverse('payment:payment_callback'),
        'CallbackURL': request.build_absolute_uri(reverse('payment:payment_callback')),
    }

    response = requests.post(url=zarinpal_request_url, data=json.dumps(request_data), headers=request_header)

    data = response.json()
    print(data)
    authority = data['Authority']
    order.zarinpal_authority = authority
    order.save()

    if 'errors' not in data or len(data['errors']) == 0:
        return redirect('https://sandbox.zarinpal.com/pg/StartPay/{authority}'.format(authority=authority))
    else:
        print(response.json())
        return HttpResponse('errors from zarinpal')


def payment_callback_sandbox(request):
    payment_authority = request.GET.get('Authority')
    payment_status = request.GET.get('Status')

    order = get_object_or_404(Order, zarinpal_authority=payment_authority)
    toman_total_price = order.get_total_price()
    rial_total_price = toman_total_price * 10

    if payment_status == 'OK':
        request_header = {
            'accept': 'application/json',
            'content-type': 'application/json',
        }

        request_data = {
            'MerchantID': 'abcABCabcABCabcABCabcABCabcABCabcABC',
            'Amount': rial_total_price,
            'Authority': payment_authority,
        }

        response = requests.post(url='https://sandbox.zarinpal.com/pg/rest/WebGate/PaymentVerification.json',
                                 data=json.dumps(request_data),
                                 headers=request_header)

        if 'errors' not in response.json():
            data = response.json()
            payment_cod = data['Status']

            if payment_cod == 100:
                order.is_paid = True
                order.zarinpal_ref_id = data['RefID']
                order.zarinpal_data = data
                order.save()
                messages.success(request, 'پرداخت شما موفق بود.')
                return render(request, 'payment/successful_purchase.html')

            elif payment_cod == 101:
                messages.warning(request, 'این پرداخت قبلا ثبت شده است.')
                return render(request, 'payment/transaction_registration.html')

            else:
                messages.error(request, 'پرداخت شما ناموفق بود.')
                return render(request, 'payment/unsuccessful_purchase.html')

    else:
        messages.error(request, 'پرداخت شما ناموفق بود.')
        return render(request, 'payment/unsuccessful_purchase.html')