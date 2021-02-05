from django.shortcuts import render

def home(request):
    return render(request, 'writeapp/home.html')

def querier(request):
    return render(request, 'writeapp/querier.html')

def blackfield(request):
    return render(request, 'writeapp/blackfield.html')

def feline(request):
    return render(request, 'writeapp/feline.html')

def htbj(request):
    return render(request, 'writeapp/htbj.html')

def baby_international(request):
    return render(request, 'writeapp/baby_international.html')

def babysql(request):
    return render(request, 'writeapp/babysql.html')

def passage(request):
    return render(request, 'writeapp/passage.html')
