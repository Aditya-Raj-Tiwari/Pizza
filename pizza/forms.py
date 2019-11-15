from django import forms
from .models import Pizza


# class PizzaForm(forms.Form):
#     topping1 = forms.CharField(label="Topping One: ", max_length=100)
#     topping2 = forms.CharField(label="Topping Two: ", max_length=100)
#     size = forms.ChoiceField(label="Sizes:",choices=[('small','small'),('medium','medium'),('large','large')])


class PizzaForm(forms.ModelForm):
    class Meta:
        model = Pizza
        fields = ['toppings1', 'toppings2', 'size']
