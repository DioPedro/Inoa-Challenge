import requests, os
from django.conf import settings

token = settings.API_KEY

def stockPrice(stock):
    url = f'https://brapi.dev/api/quote/{stock}?token={token}'
    request = requests.get(url)
    if request.status_code == 200:
        data = requests.get(url).json()['results'][0]
        return [data['regularMarketPrice'], data['logourl']]
    else:
        return []
    
def getStockList():
    file_path = os.path.join(os.path.dirname(__file__), 'stocks.txt')
    data = []
    with open(file_path, 'r') as fp:
        lines = fp.read().strip().split('\n')

    for line in lines:
        line = line.split(',')
        data.append({'stock_code':line[0], 'img_url':line[1]})

    return data