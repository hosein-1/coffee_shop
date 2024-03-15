

class Cart:
    def __init__(self, request):
        self.request = request
        self.session = request.session

        cart = self.session.get('cart')
        if not cart:
            cart = self.session['cart'] = {}
            self.cart = cart

    def add(self, product):
        product_id = str(product)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 1, 'price': product.price}
        else:
            self.cart[product_id]['quantity'] += 1

        self.save()

    def reduce(self, product):
        product_id = str(product)
        if self.cart[product_id]['quantity'] > 0:
            self.cart[product_id]['quantity'] -= 1

        self.save()

    def remove(self, product):
        product_id = str(product)
        if product_id in self.cart:
            del self.cart[product_id]

        self.save()

    def clear(self):
        del self.session['cart']

        self.save()

    def get_total_price(self):
        return sum(item['price'] * item['quantity'] for item in self.cart.values())

    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())

    def save(self):
        self.session.modified = True
