from django.shortcuts import render, redirect
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
            return redirect('/home')

    else:
        form = RegisterForm()

    return render(request, 'register/register.html', {'form':form})