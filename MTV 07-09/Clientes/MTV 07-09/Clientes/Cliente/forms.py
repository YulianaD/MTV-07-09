from django import forms

class ClientForm(forms.Form):
    nombre = forms.CharField(max_length=50)
    número = forms.IntegerField()
    email = forms.EmailField()
    
class FacturaForm(forms.Form):
    nombre = forms.CharField(max_length=50)
    número = forms.IntegerField()