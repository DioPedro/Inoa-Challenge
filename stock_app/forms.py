from django import forms
from .models import Stocks

# Creating a class to user create an stock
class CreateNewStock(forms.ModelForm):
    class Meta:
        model = Stocks
        fields = ['stock_code', 'sell_at', 'buy_at', 'time_to_search']