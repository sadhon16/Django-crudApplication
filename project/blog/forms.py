from django import forms
from django.core import validators
from .models import Login

class User(forms.ModelForm):
    class Meta:
        model=Login
        fields=['FirstName','LastName','Email']
        widgets={
            'FirstName':forms.TextInput(attrs={'class':'form-control'}),
            'LastName': forms.TextInput(attrs={'class': 'form-control'}),
            'Email': forms.EmailInput(attrs={'class': 'form-control'}),
        }

        def clean(self):
            data = self.cleaned_data

            FirstName = data.get('FirstName')
            LastName = data.get('LastName')
            Email = data.get('Email')
            return data

