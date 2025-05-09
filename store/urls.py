from django.contrib import admin
from django.urls import path
from .views.signup import Signup
from .views.login import Login, logout
from .views.home import Index
from .views.cart import Cart
from .views.checkout import CheckOut
from .views.orders import OrderView
from .middlewares.auth import auth_middleware

urlpatterns = [
    path('', Index.as_view(), name='homepage'),
    path('login', Login.as_view(), name='login'),
    path('signup', Signup.as_view(), name='signup'),
    path('logout', logout, name='logout'),
    path('cart', Cart.as_view(), name='cart'),
    path('check-out', auth_middleware(CheckOut.as_view()), name='checkout'),
    path('orders', auth_middleware(OrderView.as_view()), name='orders'),
]