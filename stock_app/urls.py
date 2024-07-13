from django.urls import path
from . import views

urlpatterns = [
    path('home', views.hello),
    path('stock/<str:person>', views.stocks),
    path('create', views.create),
    path('edit/<int:id>', views.edit),
    # path('delete/<int:id>', views.delete),
    path('error/<str:error_msg>', views.invalidRequest)
]