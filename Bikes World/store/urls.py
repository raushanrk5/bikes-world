from django.urls import path
from store.views import home, signup, login, cart, orders,checkout
from store.middlewares.auth import auth_middleware

urlpatterns = [
    path('',home.Index.as_view(), name='home'),
    path('signup/',signup.signup.as_view(), name='register'),
    path('login/',login.Login.as_view(), name='login'),
    path('logout/',login.logout, name='logout'),
    path('cart/',cart.Cart.as_view(),name='cart'),
    path('checkout',checkout.Checkout.as_view(),name='checkout'),
    path('orders', auth_middleware(orders.myOrder.as_view()), name='orders'), #using auth middleware to orders
]
