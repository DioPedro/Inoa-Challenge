from django.urls import path
from . import views

urlpatterns = [
    path('home', views.hello),
    path('stock/<str:person>', views.stocks),
    path('create', views.create)
]