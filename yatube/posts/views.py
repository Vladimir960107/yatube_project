from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def index(request):    
    #return HttpResponse('Главная страница')

    template = 'posts/index.html'
    return render(request, template)

def group_posts(request, slug):
    return HttpResponse(f'Неглавная страница {slug}')
