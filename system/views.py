from django.http import HttpResponse
from django.shortcuts import render
from symtable import Symbol
import pandas as pd
import numpy as np
import requests
import math


def index(request):
    return render(request, "base.html")


def logout(request):
    return render(request, "base.html")


def dashboard_page(request):
    return render(request, "home.html")


def portfolio_page(request):
    return render(request, "portfolio.html")


def analytics_page(request):
    return render(request, "analytics.html")


def platform_page(request):
    return render(request, "platform.html")


def trades_page(request):
    return render(request, "trades.html")


def search_page(request):
    return render(request, "searchStock.html")


def validate(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        if username == 'charlie' and password == 'murray':
            return render(request, 'home.html')
        else:
            return render(request, "home.html")


def searchStock(request):
    if request.method == 'POST':
        try:
            symbol = request.POST['symbol']

            API_KEY = 'pk_c9d202a04afd4f45a1ffa4ec75e44e56'

            api_url = f'https://cloud.iexapis.com/stable/stock/{symbol}/quote?token={API_KEY}'
            data = requests.get(api_url).json()

            marketCap = "{:,}".format(data['marketCap'])

            dict= {
                'companyName': data['companyName'],
                'latestPrice': data['latestPrice'],
                'marketCap': marketCap,
                'changePercent': data['changePercent'],
                'week52High': data['week52High'],
                'week52Low': data['week52Low'],
                'volume': data['volume'],
                'open': data['open'],
                'close': data['close'],
            }
            return render(request, 'searchStock.html', dict)
        except:
            return render(request, 'searchStock.html')

