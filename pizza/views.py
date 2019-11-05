from django.shortcuts import render
from .forms import PizzaForm


def home(request):
    return render(request, 'home.html')


def order(request):
    form = PizzaForm()
    context = {'pizzaform': form}
    return render(request, 'order.html', context)
