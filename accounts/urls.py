from . import views
from django.urls import path
urlpatterns = [
    path('logout/', views.logout_view, name='auth_logout'),
    path('login/', views.login_view, name='auth_login'),
    path('register/',views.registration_view, name ='auth_register'),
]
