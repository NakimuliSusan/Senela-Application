from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.user_login),
    path('register/', views.user_registration),
    path('users/', views.get_users),

]