from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from rango.models import Category, Page

# Create your views here.
def index(request):
    # return HttpResponse("Olá, Rango!")
    #context_dict = {'boldmessage': 'Dun dun!'}
    #return render(request, 'rango/index.html', context_dict)

    category_list = Category.objects.order_by('-likes')[:5]
    context_dict  = {'categories': category_list}
    return render(request, 'rango/index.html', context_dict)


def about(request):
    dados = {'qualquer': 'informação qualquer!'}

    return render(request, 'rango/about.html', dados)


def category(request, category_name_slug):
    context_dict = {}

    try:
        category = Category.objects.get(slug=category_name_slug)
        context_dict['category_name'] = category.name

        pages = Page.objects.filter(category=category)
        context_dict['pages'] = pages

        context_dict['category'] = category

    except Category.DoesNotExist:
        pass

    return render(request, 'rango/category.html', context_dict)
