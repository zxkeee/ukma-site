from django.shortcuts import render
from exchange.models import ExchangeProgram


# Create your views here.


def programs(request):
    progs = ExchangeProgram.objects.all()
    return render(request, 'exchange/programs.html', {'programs': progs})
