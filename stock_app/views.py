from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Person, Stocks
from .forms import CreateNewStock
from .scrap import stockPrice
from django import template

# Create your views here.
def hello(request):
    return render(request, 'stock_app/home.html')

def stocks(request, person):
    stocks = Stocks.objects.filter(person__name = person)
    return render(request, 'stock_app/stocks.html', {'stocks':stocks, 'person':person})

def create(request):
    if request.method == "POST":
        form = CreateNewStock(request.POST)

        if form.is_valid():
            name = request.user
            p = Person.objects.get(name = name)

            stock = form.cleaned_data['stock_code']
            if Stocks.objects.filter(stock_code = stock):
                return HttpResponseRedirect(f'/error/Company alredy exists in database')

            
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
                return HttpResponseRedirect(f'/error')
    else:
        form = CreateNewStock()

    return render(request, "stock_app/create.html", {'form': form})

def edit(request, id):
    stock = Stocks.objects.get(id = id)

    if request.method == "POST":
        form = CreateNewStock(request.POST, instance = stock)
        if form.is_valid():
            stock = form.cleaned_data['stock_code']
            print(form.cleaned_data)

            if Stocks.objects.filter(stock_code = stock):
                return HttpResponseRedirect(f'/error/Company alredy exists in database')
            
            form.save()
            return HttpResponseRedirect(f'/stock/{request.user}')
    else:
        form = CreateNewStock(instance = stock)

    return render(request, "stock_app/edit.html", {'form': form, "id":id})

# def delete(request, id):

def invalidRequest(request, error_msg):
    return render(request, 'stock_app/error.html', {'error_msg': error_msg})