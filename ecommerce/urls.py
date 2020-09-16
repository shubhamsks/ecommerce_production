"""ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from orders import views
from accounts import views as accounts_views
urlpatterns = [
    path('', include('products.urls')),
    path('sks/', admin.site.urls),
    path('cart/', include('cart.urls')),
    path('checkout/',views.checkout,name= 'checkout'),
    path('orders/', include('orders.urls')),
    path('accounts/', include('accounts.urls')),
    path('marketing/', include('marketing.urls')),
    path('coming_soon/',views.coming_soon, name = 'coming_soon'),
    path('ajax/add_user_address', accounts_views.add_user_address, name='add_user_address'),
    # path('payment/', views.stripe_payment_view, name='payment'),
    
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
