from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    # return HttpResponse("Olá, Rango!")
    context_dict = {'boldmessage': 'Dun dun!'}

    return render(request, 'rango/index.html', context_dict)


def about(request):
    dados = {'qualquer': 'informação qualquer!'}

    return render(request, 'rango/about.html', dados)