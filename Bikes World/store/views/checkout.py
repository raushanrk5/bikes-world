from django.shortcuts import render,redirect
from django.contrib.auth.hashers import make_password,check_password
from store.models.products import Product
from store.models.customer import Customer
from django.views import View
from store.models.orders import Order
from store.middlewares.auth_checkout import checkout_middleware
from django.utils.decorators import method_decorator

class Checkout(View):
    @method_decorator(checkout_middleware)
    def post(self,request):
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        customer=request.session.get('customer')
        cart = request.session.get('cart')
        products=Product.get_products_by_id(list(cart.keys()))
        print(address,phone,customer,products)

        for product in products:
            print(cart.get(product.id))
            order = Order(customer= Customer(id=customer),
                          product=product,
                          price=product.price,
                          address=address,
                          phone=phone,
                          quantity=cart.get(str(product.id)),
                          )
            order.save()
            request.session['cart'] = {}

        return redirect('orders')
