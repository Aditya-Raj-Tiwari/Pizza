from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def order(request):
    return render(request, 'order.html')
