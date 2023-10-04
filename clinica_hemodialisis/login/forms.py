from django import forms


class FormLogin(forms.Form):
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
