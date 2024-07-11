import requests
token = '8VZJGvnyNJYsqRqY3ZdHt2'

def stockPrice(stock):
    url = f'https://brapi.dev/api/quote/{stock}?token={token}'
    request = requests.get(url)
    if request.status_code == 200:
        return requests.get(url).json()['results'][0]['regularMarketPrice']
    else:
        return -1