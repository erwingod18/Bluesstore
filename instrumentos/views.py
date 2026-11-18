from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView,
)

from .forms import InstrumentoForm
from .models import Instrumento


# ListView y DetailView quedan públicos (catálogo abierto).
class InstrumentoListView(ListView):
    model = Instrumento
    template_name = 'instrumentos/instrumento_list.html'
    context_object_name = 'instrumentos'

    def get_queryset(self):
        # JOIN con Categoria en UNA sola consulta (evita el problema N+1).
        return Instrumento.objects.select_related('categoria').order_by('nombre')


class InstrumentoDetailView(DetailView):
    # pk inexistente -> 404 automático.
    model = Instrumento
    template_name = 'instrumentos/instrumento_detail.html'
    context_object_name = 'instrumento'

    def get_queryset(self):
        return Instrumento.objects.select_related('categoria')


# Mutaciones: LoginRequiredMixin SIEMPRE a la izquierda (MRO).
class InstrumentoCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Instrumento
    form_class = InstrumentoForm
    template_name = 'instrumentos/instrumento_form.html'
    success_url = reverse_lazy('instrumentos:lista')
    success_message = 'Instrumento "%(nombre)s" creado correctamente.'


class InstrumentoUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Instrumento
    form_class = InstrumentoForm
    template_name = 'instrumentos/instrumento_form.html'
    success_url = reverse_lazy('instrumentos:lista')
    success_message = 'Instrumento "%(nombre)s" actualizado correctamente.'


class InstrumentoDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Instrumento
    template_name = 'instrumentos/instrumento_confirm_delete.html'
    context_object_name = 'instrumento'
    success_url = reverse_lazy('instrumentos:lista')

    def get_success_message(self, cleaned_data):
        # El form de borrado no tiene campos: se usa self.object en vez de %(nombre)s.
        return f'Instrumento "{self.object.nombre}" eliminado correctamente.'