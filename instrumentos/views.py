from django.shortcuts import render
from .forms import InstrumentoForm
from .models import Instrumento
from django.urls import reverse_lazy
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView,
)



# Paso 2: ListView
class InstrumentoListView(ListView):
    model = Instrumento
    template_name = 'instrumentos/instrumento_list.html'
    context_object_name = 'instrumentos'

    def get_queryset(self):
        # JOIN con Categoria en UNA sola consulta (evita el problema N+1).
        return Instrumento.objects.select_related('categoria').order_by('nombre')


# Paso 3: DetailView
class InstrumentoDetailView(DetailView):
    # Usa get_object_or_404 internamente: pk inexistente -> 404 automático.
    model = Instrumento
    template_name = 'instrumentos/instrumento_detail.html'
    context_object_name = 'instrumento'

    def get_queryset(self):
        return Instrumento.objects.select_related('categoria')


# Paso 4: Create y Update
class InstrumentoCreateView(CreateView):
    model = Instrumento
    form_class = InstrumentoForm
    template_name = 'instrumentos/instrumento_form.html'
    success_url = reverse_lazy('instrumentos:lista')


class InstrumentoUpdateView(UpdateView):
    model = Instrumento
    form_class = InstrumentoForm
    template_name = 'instrumentos/instrumento_form.html'
    success_url = reverse_lazy('instrumentos:lista')


# Paso 5: Delete
class InstrumentoDeleteView(DeleteView):
    model = Instrumento
    template_name = 'instrumentos/instrumento_confirm_delete.html'
    context_object_name = 'instrumento'
    success_url = reverse_lazy('instrumentos:lista')

