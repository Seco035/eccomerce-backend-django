from django import forms
from .models import Contact
from django.forms import widgets

class ContactForm(forms.ModelForm):
    
    class Meta:
        model = Contact
        fields = '__all__'

        labels = {
            'first_name': 'İsim',
            'last_name': 'Soyisim',
            'email': 'Email',
            'subject': 'Konu',
            'message': 'Mesaj',
        }
        
        widgets = {
            'first_name': widgets.TextInput(attrs={'class':"form-control"}),
            'last_name': widgets.TextInput(attrs={'class':"form-control"}),
            'email': widgets.EmailInput(attrs={'class':"form-control"}),
            'subject': widgets.TextInput(attrs={'class':"form-control"}),
            'message': widgets.Textarea(attrs={'class':"form-control"}),
        }