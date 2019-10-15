from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
	path('', views.home, name = 'home'),
    path('products', views.all, name='products'),
    path('products/new', views.create_product, name = 'create_product'),
    path('products/<str:slug>/', views.single, name='single-product'),
    path('s/', views.search, name = 'search'),
    
]
