from django import forms

from . models import ShippingAddress



class ShippingForm(forms.ModelForm):

    class Meta:

        model = ShippingAddress

        fields = ['full_name', 'email', 'address1', 'address2', 'city', 'wojewodztwo', 'zipcode']
        exclude = ['user',]

        labels = {
            'full_name': 'Imię i Nazwisko',
            'email': 'Adres email',
            'address1': 'Adres 1',
            'address2': 'Adres 2',
            'city': 'Miasto',
            'wojewodztwo': 'Województwo',
            'zipcode': 'Kod pocztowy',
        }






