from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Person, Stocks
from .forms import CreateNewStock
from .scrap import stockPrice, getStockList
from django import template

# Create your views here.
def hello(request):
    return render(request, 'stock_app/hello.html')

def stocks(request, person):
    stocks = Stocks.objects.filter(person__name = person)
    return render(request, 'stock_app/stocks.html', {'stocks':stocks, 'person':person})

@login_required
def create(request):
    if request.method == "POST":
        form = CreateNewStock(request.POST)

        if form.is_valid():
            name = request.user
            p = Person.objects.get(name = name)

            stock = form.cleaned_data['stock_code']
            if Stocks.objects.filter(stock_code = stock):
                return HttpResponseRedirect(f'/error/Company alredy exists in database')

            stock_data = stockPrice(stock)

            # This means the request failed, which means it's an invalid company
            if len(stock_data) >= 2:
                sell = form.cleaned_data['sell_at']
                buy = form.cleaned_data['buy_at']
                # Time to update can only be 30min or more  because of the API
                time = form.cleaned_data['time_to_search']
                if time < 1800000:
                    time = 1800000
                s = Stocks(person = p, stock_code = stock, stock_img = stock_data[1], sell_at = sell, buy_at = buy,
                        cur_price = stock_data[0], time_to_search = time)
                s.save()
                return HttpResponseRedirect(f'/stock/{name}')
            
            else:
                return HttpResponseRedirect(f'/error/The stock code you entered isn\'t valid')
    else:
        form = CreateNewStock()

    return render(request, "stock_app/create.html", {'form': form})

@login_required
def edit(request, id):
    old_stock = Stocks.objects.get(id = id)
    old_stock_code = old_stock.stock_code
    person_name = old_stock.person.name
    
    # Prevent users to edit stocks from other users
    if person_name != request.user:
        return HttpResponseRedirect(f'/error/This stock is not yours to change')

    if request.method == "POST":
        new_stock = CreateNewStock(request.POST, instance = old_stock)
        if new_stock.is_valid():
            stock_code = new_stock.cleaned_data['stock_code']

            if new_stock.cleaned_data['time_to_search'] < 1800000:
                return HttpResponseRedirect(f'/error/Time need to be bigger than 1800000, remember time should be in seconds')
            
            # The user is updating the same stock alert
            if old_stock_code == stock_code:
                new_stock.save()
                return HttpResponseRedirect(f'/stock/{request.user}')
            
            else:
                return HttpResponseRedirect(f'/error/You can\'t change the stock code, try deleting the old stock and creating a new alert for the new stock')

    else:
        new_stock = CreateNewStock(instance = old_stock)

    return render(request, "stock_app/edit.html", {'form': new_stock, "id":id})

# In thesis we need to get the instance and then instance.delete()
def delete(request, id):
    stock = Stocks.objects.get(id = id)
    stock.delete()
    return HttpResponseRedirect(f'/stock/{request.user}')

@login_required
def invalidRequest(request, error_msg):
    return render(request, 'stock_app/error.html', {'error_msg': error_msg})

# This page makes a lot of requests because of the images, so it's pretty slow
def stockList(request):
    data = getStockList()
    return render(request, "stock_app/valid_stocks.html", {'stocks': data})