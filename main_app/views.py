from django.shortcuts import render

def home(request):
    return render(request, 'main_app/home.html')

def dengue_graph(request):
    return render(request, 'main_app/dengue_graph.html')

def geomap(request):
    return render(request, 'main_app/geomap.html')

def bunos(request):
    return render(request, 'main_app/bunos.html')