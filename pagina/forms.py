from django import forms
from .models import *

class EventoForm(forms.ModelForm):

    CATEGORIES_CHOICES = [
        ('Cultura', 'Cultura'),
        ('Fiesta', 'Fiesta'),
        ('Tecnología', 'Tecnología'),
        ('Feria', 'Feria'),
        ('Evento', 'Evento'),
        ('Conferencia', 'Conferencia'),
        ('Concierto', 'Concierto'),
        ('Deporte', 'Deporte'),
        ('Taller', 'Taller'),
        ('Exposición', 'Exposición'),
        ('Actividad', 'Actividad'),
        ('Gastronomía', 'Gastronomía'),
        ('Networking', 'Networking'),
        ('Celebración', 'Celebración'),
        ('Caridad', 'Caridad'),
        ('Teatro', 'Teatro'),
        ('Reunión temática', 'Reunión temática'),
    ]
    class Meta:
        model = Evento
        fields = ['nombre', 'ubicacion', 'fechaInicio', 'fechaFin', 'descripcion', 'precio', 'capacidad', 'categorias', 'etiquetas', 'imagen']

    def __init__(self, *args, **kwargs):
        super(EventoForm, self).__init__(*args, **kwargs)

        # Campos obligatorios y opcionales
        self.fields['nombre'].required = True
        self.fields['ubicacion'].required = True
        self.fields['fechaInicio'].required = True
        self.fields['fechaFin'].required = False
        self.fields['descripcion'].required = False
        self.fields['precio'].required = False
        self.fields['capacidad'].required = False
        self.fields['categorias'] = forms.ChoiceField(choices=self.CATEGORIES_CHOICES, required=True)
        self.fields['etiquetas'].required = False

        self.fields['nombre'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Nombre del evento'
        })
        self.fields['ubicacion'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Ubicación del evento'
        })
        self.fields['fechaInicio'].widget.attrs.update({
            'class': 'form-control datepicker',
            'placeholder': 'Fecha de inicio (YYYY-MM-DD)'
        })
        self.fields['fechaFin'].widget.attrs.update({
            'class': 'form-control datepicker',
            'placeholder': 'Fecha de finalización (YYYY-MM-DD)'
        })
        self.fields['descripcion'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Descripción del evento'
        })
        self.fields['precio'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Precio del evento'
        })
        self.fields['capacidad'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Capacidad del evento'
        })
        self.fields['categorias'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Categorías del evento'
        })
        self.fields['etiquetas'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Etiquetas del evento'
        })
        self.fields['imagen'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Sube una imagen del evento'
        })


class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['texto']
        widgets = {
            'texto': forms.Textarea(attrs={'rows': 1}),
        }