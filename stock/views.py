from django.shortcuts import render

from .models import UserStock

# Create your views here.


def all_stocks(request):
    stocks = UserStock.objects.all()

    return render(request, "stock/stocks.html", {'stocks': stocks})
