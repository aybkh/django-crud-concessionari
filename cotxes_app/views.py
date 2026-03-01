from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Marca

# 1. Llegir: Mostra la llista de totes les marques
class MarcaListView(ListView):
    model = Marca
    template_name = 'cotxes_app/marca_list.html'
    context_object_name = 'marques'

# 2. Crear: Formulari per afegir una nova marca
class MarcaCreateView(CreateView):
    model = Marca
    fields = ['nom', 'pais']
    template_name = 'cotxes_app/marca_form.html'
    success_url = reverse_lazy('marca_list')

# 3. Actualitzar: Formulari per editar una marca existent
class MarcaUpdateView(UpdateView):
    model = Marca
    fields = ['nom', 'pais']
    template_name = 'cotxes_app/marca_form.html'
    success_url = reverse_lazy('marca_list')

# 4. Esborrar: Pàgina de confirmació per eliminar
class MarcaDeleteView(DeleteView):
    model = Marca
    template_name = 'cotxes_app/marca_confirm_delete.html'
    success_url = reverse_lazy('marca_list')
