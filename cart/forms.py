from django import forms

PRODUCT_QUANTITY = [(i, str(i)) for i in range(1,20)]

class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY, label='Количество', coerce=int)
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)