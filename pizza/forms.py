from django import forms


class PizzaForm(forms.Form):
    topping1 = forms.CharField(label="Topping One: ", max_length=100)
    topping2 = forms.CharField(label="Topping Two: ", max_length=100)
    size = forms.ChoiceField(label="Sizes:",choices=[('small','small'),('medium','medium'),('large','large')])
