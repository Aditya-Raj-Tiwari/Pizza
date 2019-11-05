from django.shortcuts import render
from .forms import PizzaForm


def home(request):
    return render(request, 'home.html')


def order(request):
    if request.method == 'POST':
        filled_form = PizzaForm(request.POST)
        if filled_form.is_valid():
            note = 'Your %s %s and %s pizza is on its way! Thank you for visiting us.' % (
                filled_form.cleaned_data['size'], filled_form.cleaned_data['topping1'],
                filled_form.cleaned_data['topping2'])
            new_form = PizzaForm()
            context = {'pizzaform': new_form,
                       'note': note}
            return render(request, 'order.html', context)
    else:
        form = PizzaForm()
        context = {'pizzaform': form}
        return render(request, 'order.html', context)
