# Stock Market App

# Overview

Stock Market App is a web interface to monitor the stock prices of [B3](b3.com.br) stocks. When the price of a stock is bellow the configured value of buying or is higher then the configured value to sell the user receives an email informing about those changes.

# Configuration and setup

This project uses [Brapi](https://brapi.dev/) API using their free license. You need to create an account and an api-key to make requests.

Into the settings.py file that is found [here](configuration/settings.py) you gotta save your api-key into the variable API_KEY in the end of the file, it will look like this.

```py
API_KEY = 'your-api-key'
```
Clone the repository into your machine and install the requeriments
```bash
pip install -r requirements.txt
```

# Running the server

How we are doing everything locally an email won't be really sent but we can't see them in two ways:

The first way is when the server is running to make it run:

```bash
py manage.py runserver
```

With the server running when you can access ```127.0.0.1:8000``` to use the site, register/login, create/edit stocks, we server will check the price an see if you should buy or sell it. Something like this will apper in your terminal:

```
Content-Type: text/plain; charset="utf-8"
MIME-Version: 1.0
Content-Transfer-Encoding: 7bit
Subject: Alert for your stock U1BE34
From: alert@stock_app.com
To: bigtechs@gmail.com
Date: Tue, 16 Jul 2024 17:00:02 -0000
Message-ID: <172114920297.31664.3569303168113739227@DioNote.>

Hello bigtechs, stocks for U1BE34 are now above the defined target price.
Current price: R$ 101.53
Now is a good time to sell your stocks!
------------------------------------------------------------------------------
```

But only doing this won't update the stocks as requests, for updating the stocks based on the time choice we need to configure a cron job

2. The cron job configuration
You can see in the [settings.py](configuration/settings.py) that we have a cron job configured for it, basically it look every minute if some stock alert need to have it's value updated and if the value is updated the server checks for the prices to warn you. How we are using the free license from [Brapi](https://brapi.dev/) the values will only update every 30min, so every stock alert need 30min as the minium time to update (when creating or add a stock alert this is alredy checked). To run the cron job we need to add it using the command:

```bash
py manage.py crontab add
```

Now with the cron job added if your server is still running you will see the emails "received" throgh there, but if you close the server the emails will be send to the [django_cron.log](stock_app/django_cron.log). You can see it as I've populated it with some email examples form different users.

If you want to see if the cron job is really running you can use the following commands:

```bash
py manage.py crontab show
```

An output like this should de shown:

```bash
Currently active jobs in crontab:
60dd730b2d0f80d9ff23f409a83bc86f -> ('* * * * *', 'stock_app.cron.update', '>> ~/Inoa-Challenge/stock_app/django_cron.log 2>&1')
```

To stop the cron job from running in the background you just need to remove it like this:

```bash 
py manage.py crontab remove
```

# Usage of the web interface

If you wish to check the examples alredy configured an with some stocks you can check the ready users in the [accounts file](accounts.txt). But you can also register a new user and create alerts for any stock you want.

Almost every page is acessible through the navbar but there's the valid_stocks page that shows every possible stock in the [Brapi](https://brapi.dev/) how there are many stocks the page is a little slow to load, that's why it isn't acessible through the navbar but you can go to ```127.0.0.1:8000/valid_stocks``` to see it.