from django.shortcuts import render

def index(request):
    return render(request, 'posts/index.html')

def detail(request, id):
    return render(request, 'posts/detail.html')