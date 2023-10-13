from django import forms


class FloatInput(forms.TextInput):
    input_type = 'number'


class FormMedicine(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'name': 'name',
        'placeholder': 'Nombre del Medicamento'
    }))
    description = forms.CharField(max_length=500, widget=forms.Textarea(attrs={
        'class': 'form-control',
        'name': 'description',
        'placeholder': 'Descripcion'
    }))
    price = forms.FloatField(widget=FloatInput(attrs={
        'class': 'form-control',
        'name': 'price',
        'placeholder': 'Precio'
    }))
    stock = forms.IntegerField(widget=forms.NumberInput(attrs={
        'class': 'form-control',
        'name': 'stock',
        'placeholder': 'Stock'
    }))
    expiration_date = forms.DateField(widget=forms.DateInput(attrs={
        'class': 'form-control',
        'name': 'expiration_date',
        'placeholder': 'Fecha de Expiración',
        'type': 'date'  # Esto establece el tipo de entrada como 'date' para un selector de fecha en el navegador.
    }))
    category = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'name': 'category',
        'placeholder': 'Categoria'
    }))
    brand = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'name': 'brand',
        'placeholder': 'Marca'
    }))
    supplier = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'name': 'supplier',
        'placeholder': 'Proveedor'
    }))
