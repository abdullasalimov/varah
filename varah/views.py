import requests
from django.shortcuts import render
from datetime import date, timedelta


# Create your views here.
def index(request):
    
    datetime_today = date.today()      # get current date
    date_today = str(datetime_today)    # convert datetime class to string
    date_10daysago = str(datetime_today - timedelta(days=10))     # get date of today -10 days

    #api= 'https://api.coindesk.com/v1/bpi/historical/close.json?start=' + date_10daysago + '&end=' + date_today + '&currency=usd'

    # api = "https://api.coindesk.com/v1/bpi/historical/close.json?start=2019-08-10&end=2020-08-11&currency=usd"

    
    try:
        response = requests.get(api, timeout=2)    # get api response data from coindesk based on date range supplied by user
        response.raise_for_status()            # raise error if HTTP request returned an unsuccessful status code.
        prices = response.json()    #convert response to json format
        btc_price_range=prices.get("bpi")   # filter prices based on "bpi" values only
    except requests.exceptions.ConnectionError as errc:  #raise error if connection fails
        raise ConnectionError(errc)
    except requests.exceptions.Timeout as errt:   # raise error if the request gets timed out without receiving a single byte
        raise TimeoutError(errt)
    except requests.exceptions.HTTPError as err:   # raise a general error if the above named errors are not triggered 
        raise SystemExit(err)

    context = {
        'price':btc_price_range
    }
    return render(request, 'index.html', context)