from django.db.models import F, ExpressionWrapper, DurationField 
from .models import Stocks
import datetime

def update():
    now = datetime.datetime.now(datetime.timezone.utc)
    
    # Check which stocks have completed their time to update the value
    stocks_to_update = Stocks.objects.annotate(
        time_diff = ExpressionWrapper(
            now - F('time'),
            output_field = DurationField()
        )
    ).filter(time_diff__gte = F('time_to_search') * datetime.timedelta(minutes = 1))
    
    for stock in stocks_to_update:
        stock.updateMarketPrice()