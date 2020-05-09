from django.shortcuts import render
from django.urls import reverse_lazy 
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from catalogos.models import Categoria
from catalogos.forms import  CategoriaForm
from generales.views import  SinPrivilegios

# Create your views here.

class CategoriaView(LoginRequiredMixin, generic.ListView):
    model = Categoria
    template_name = "catalogos/categoria_list.html"
    context_object_name = "obj" 
    login_url='generales:login'

class CategoriaNew(LoginRequiredMixin, SinPrivilegios, generic.CreateView):
    permission_required="catalogos.add_categoria"
    model=Categoria
    template_name="catalogos/categoria_form.html"
    context_object_name = 'obj'
    form_class = CategoriaForm
    success_url = reverse_lazy("catalogos:categoria_list")
    #login_url='generales:login'

class CategoriaEdit(LoginRequiredMixin, SinPrivilegios, generic.UpdateView):
    permission_required="catalogos.change_categoria"
    model=Categoria
    template_name="catalogos/categoria_form.html"
    context_object_name = 'obj'
    form_class = CategoriaForm
    success_url = reverse_lazy("catalogos:categoria_list")
    #login_url='generales:login'

class CategoriaDel(LoginRequiredMixin, generic.DeleteView):
    model=Categoria
    template_name="catalogos/catalogos_del.html"
    context_object_name = 'obj'    
    success_url = reverse_lazy("catalogos:categoria_list")
    login_url='generales:login'

