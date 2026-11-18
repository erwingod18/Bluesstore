from django import forms
from .models import Instrumento
from django.contrib.auth.forms import AuthenticationForm

class InstrumentoForm(forms.ModelForm):
    class Meta:
        model = Instrumento
        fields = ['categoria', 'nombre', 'descripcion', 'precio',
                'fecha_ingreso', 'disponible']
        widgets = {
            'categoria': forms.Select(attrs={'class': 'form-select'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: Guitarra eléctrica'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'precio': forms.NumberInput(attrs={'class': 'form-control', 'min': 0}),
            'fecha_ingreso': forms.DateInput(
                format='%Y-%m-%d',
                attrs={'class': 'form-control', 'type': 'date'},
            ),
            'disponible': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'