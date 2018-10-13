from django.urls import path
from . import views

urlpatterns=[
	path('cart',views.cart_home,name='cart-home'),
	path('cart-update',views.cart_update,name='update'),
	path('checkout',views.checkout_home,name='checkout'),
]