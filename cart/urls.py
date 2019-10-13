from . import views
from django.urls import path
urlpatterns = [
    path('',views.cart_view, name ='cart'),
    path('<int:id>',views.remove_from_cart, name='remove_from_cart'),
    path('<str:slug>/',views.add_to_cart, name='add_to_cart')
]
