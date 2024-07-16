import django.utils
from django.db import models
from django.conf import settings
from django.core.mail import send_mail
from .scrap import stockPrice

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length = 255)
    email = models.CharField(max_length = 255, primary_key = True)
    
class Stocks(models.Model):
    person = models.ForeignKey(Person, on_delete = models.CASCADE)
    stock_code = models.CharField(max_length = 10)
    stock_img = models.CharField(max_length = 1000)
    sell_at = models.FloatField()
    buy_at = models.FloatField()
    cur_price = models.FloatField()
    time_to_search = models.IntegerField()
    time = models.DateTimeField(default = django.utils.timezone.now)

    def updateMarketPrice(self):
        # Updating the market value of the stock
        self.cur_price = stockPrice(self.stock_code)[0]

        # Update the time value for counting until update again
        self.time = django.utils.timezone.now()

        # Call checkLimits to check if emails should be send
        self.checkLimitsPrice()

        # Saving the update
        self.save()

    def checkLimitsPrice(self):
        if self.cur_price >= self.sell_at:
            self.sendEmail(
                f'Hello {self.person.name}, stocks for {self.stock_code} are now above the defined target price.\nCurrent price: R$ {self.cur_price}\nNow is a good time to sell your stocks!'
            )

        if self.cur_price <= self.buy_at:
            self.sendEmail(
                f'Hello {self.person.name}, stocks for {self.stock_code} are now under the defined target price.\nCurrent price: R$ {self.cur_price}\nNow is a good time to buy your stocks!'    
            )
            
    def sendEmail(self, msg):
        send_mail(
            f'Alert for your stock {self.stock_code}',
            msg,
            settings.EMAIL_HOST_USER,
            [self.person.email],
            fail_silently = False
        )