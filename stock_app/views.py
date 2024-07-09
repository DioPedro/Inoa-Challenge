from django.shortcuts import render
from .models import Person, Stocks

# Create your views here.
def hello(request):
    return render(request, 'home.html')

def stocks(request, person):
    stocks = Stocks.objects.filter(person__name = person)
    print(stocks)
    return render(request, 'stocks.html', {'stocks':stocks, 'person':person})