from django.shortcuts import render

def index(request):
    return render(request, 'pages/index.html')

def detail(request, id):
    return render(request, 'pages/detail.html')