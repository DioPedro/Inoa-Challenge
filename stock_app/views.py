from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Person, Stocks
from .forms import CreateNewStock
from .scrap import stockPrice
from django import template

# TODO: look here https://stackoverflow.com/questions/21062560/django-variable-in-base-html for looking at a way to put a global variable into settings.py to make stocks button href work

# Create your views here.
def hello(request):
    return render(request, 'stock_app/home.html')

def stocks(request, person):
    stocks = Stocks.objects.filter(person__name = person)
    return render(request, 'stock_app/stocks.html', {'stocks':stocks, 'person':person})

# TODO: Create done, but still needs to edit and delete stocks from an account
def create(request):
    if request.method == "POST":
        form = CreateNewStock(request.POST)

        if form.is_valid():
            name = 'dio' #TODO: make the logged user info come here to auto attach stock to user
            p = Person.objects.get(name = name)

            stock = form.cleaned_data['stock_code'] #TODO: Check if the stock alredy exists
            if Stocks.objects.filter(stock_code = stock):
                print("Company alredy exists in database")
                return HttpResponseRedirect(f'/stock/{name}')
            
            price = stockPrice(stock)

            # This means the request failed, which means it's an invalid company
            if price != -1:
                sell = form.cleaned_data['sell_at']
                buy = form.cleaned_data['buy_at']
                time = form.cleaned_data['time_to_search']
                s = Stocks(person = p, stock_code = stock, sell_at = sell, buy_at = buy,
                        cur_price = price, time_to_search = time)
                s.save()
                return HttpResponseRedirect(f'/stock/{name}')
            
            else:
                return HttpResponseRedirect(f'/error') # TODO: Test if failed requests redirect to right place

    else:
        form = CreateNewStock()

    return render(request, "stock_app/create.html", {'form': form})

def invalidRequest(request):
    return render(request, 'stock_app/error.html')