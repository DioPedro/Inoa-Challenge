from django.urls import path
from . import views

urlpatterns = [
    path('home', views.hello),
    path('<str:person>', views.stocks)
]