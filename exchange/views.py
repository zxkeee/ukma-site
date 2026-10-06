import datetime

from django.shortcuts import render
from exchange.models import ExchangeProgram


def programs(request):
    progs = ExchangeProgram.objects.all()
    today = datetime.date.today()
    return render(request, 'exchange/programs.html', {'programs': progs, 'today': today})