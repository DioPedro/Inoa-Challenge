from django.db import models
import time

# Create your models here.
class Person(models.Model):
    
    name = models.CharField(max_length = 255)

    # def __str__(self):
    #     return self.name
    
class Stocks(models.Model):
    person = models.ForeignKey(Person, on_delete = models.CASCADE)
    stock_code = models.CharField(max_length = 10)
    sell_at = models.FloatField()
    buy_at = models.FloatField()
    cur_price = models.FloatField()
    time_to_search = models.IntegerField(default = '1800000') # Means 30min, the API only updates every 30min
    
    # def __str__(self):
        # return self.Person | self.stock_code | self.sell_at | self.buy_at | self.cur_price