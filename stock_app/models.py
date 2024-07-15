from django.db import models
import datetime

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length = 255)
    email = models.CharField(max_length = 255, primary_key = True)

    # def __str__(self):
    #     return self.name
    
class Stocks(models.Model):
    person = models.ForeignKey(Person, on_delete = models.CASCADE)
    stock_code = models.CharField(max_length = 10)
    stock_img = models.CharField(max_length = 1000)
    sell_at = models.FloatField()
    buy_at = models.FloatField()
    cur_price = models.FloatField()
    time_to_search = models.IntegerField()
    time = models.DateTimeField(default = datetime.datetime.now())

    # def __str__(self):
        # return self.Person | self.stock_code | self.sell_at | self.buy_at | self.cur_price