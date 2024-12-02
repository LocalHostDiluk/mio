from django.urls import path, include
from .views import *

urlpatterns = [
    path('', login_user, name='login'),
    path('registro/', registro, name='registro'),
    path('inicio/', inicio, name='inicio'),
    path('logout/', logout_user, name='logout'),
]
