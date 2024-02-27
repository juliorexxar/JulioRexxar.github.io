from django import forms


class TransaccionForm(forms.Form):
    nombre = forms.CharField(max_length=100)
    email = forms.EmailField()
    codigo_descuento = forms.CharField(max_length=10, required=False)
