from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import RegisterForm

# importing Person model from another folder
import sys
sys.path.insert(0, '/home/dio/Inoa-Challenge/stock_app')
from stock_app.models import Person

# Create your views here.
def register(request):
    if request.method == "POST":
        # TODO: Make user create a Person in the database when creating account
        form = RegisterForm(request.POST)
        
        if form.is_valid():
            # Creates an Person into the database with the same info for login
            name = form.cleaned_data['username']
            email = form.cleaned_data['email']
            p = Person(name = name, email = email)
            p.save()

            form.save()
            user = authenticate(username = name, password = form.cleaned_data['password1'])
            login(request, user)
            return redirect(f'/stock/{name}')

    else:
        form = RegisterForm()

    return render(request, 'register/register.html', {'form':form})