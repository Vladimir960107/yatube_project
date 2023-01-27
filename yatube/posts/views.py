from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def index(request):    
    #return HttpResponse('Главная страница')
    template = 'posts/index.html'
    title = 'Yatube'
    context = {
        'title': title,
        'text' : 'Это главная страница проекта Yatube'
    }
    return render(request, template, context)

def group_posts(request, slug):
    template = 'posts/group_list.html'
    title = 'Yatube'
    context = {
        'title': title,
        'text' : 'Здесь будет информацию о группах проекта Yatube'
    }
    return render(request, template, context)
