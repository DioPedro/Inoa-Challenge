from django import forms

# Creating a class to user create an stock
class CreateNewStock(forms.Form):
    stock_code = forms.CharField(label = "Stock Code", max_length = 10)
    sell_at = forms.FloatField(label = "Price to sell stock")
    buy_at = forms.FloatField(label = "Price to buy stock")
    time_to_search = forms.IntegerField(label = "Time to research the stock in seconds")