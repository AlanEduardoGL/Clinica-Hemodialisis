from django import forms
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

User = get_user_model()


class FormRegister(forms.Form):
    username = forms.CharField(max_length=20, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'name': 'username',
        'placeholder': 'Nombre de Usuario'
    }))
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'name': 'name',
        'placeholder': 'Nombres'
    }))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'name': 'last_name',
        'placeholder': 'Apellido'
    }))
    age = forms.IntegerField(widget=forms.NumberInput(attrs={
        'class': 'form-control',
        'name': 'age',
        'placeholder': 'Edad'
    }))
    cell_number = forms.IntegerField(widget=forms.NumberInput(attrs={
        'class': 'form-control',
        'name': 'cell_number',
        'placeholder': 'Número de Teléfono'
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'name': 'email',
        'placeholder': 'Correo Electrónico'
    }))
    password = forms.CharField(max_length=30, widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'name': 'password',
        'placeholder': 'Contraseña'
    }))
    confirm_password = forms.CharField(max_length=30, widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'name': 'confirm_password',
        'placeholder': 'Confirmar Contraseña'
    }))
    administrator_profile = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={
        'class': 'form-check-input',
        'id': 'flexSwitchCheckChecked',
    }))

    def clean_username(self):
        username = self.cleaned_data['username']

        # Verifica que el nombre de usuario no esté en uso
        if User.objects.filter(username=username).exists():
            raise ValidationError('El nombre de usuario ya está en uso.')

        return username
