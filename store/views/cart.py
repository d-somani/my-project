from django.shortcuts import render , redirect

from django.contrib.auth.hashers import  check_password
from store.models.customer import Customer
from django.views import  View
from store.models.product import  Product

class Cart(View):
    def get(self, request):
        # Initialize cart as an empty dictionary if it doesn't exist
        if 'cart' not in request.session:
            request.session['cart'] = {}
        
        cart = request.session['cart']
        ids = list(cart.keys())
        products = Product.get_products_by_id(ids)
        return render(request, 'cart.html', {'products': products, 'cart': cart})