from django.urls import path
from . import views
urlpatterns = [
    path('',views.index),
    path('index.html',views.index),
    path('biswa',views.mandal),
    path('home',views.index),
    path('contact.html',views.contact),
    path('products.html',views.product),
    path('product-details.html',views.productDetails),
    path('cart.html',views.cart),
    path('account.html',views.account),
    path('about.html',views.about),
]
