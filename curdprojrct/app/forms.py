from .models import register
from django import forms


class data_register(forms.ModelForm):
    class Meta:
        model = register  # Ensure the model name matches your actual model
        fields = ('id', 'name', 'email', 'password',)
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
        }
