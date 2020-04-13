from django.shortcuts import render
from django.http import HttpResponse

from django.views import generic

# Create your views here.
class HomePage(generic.View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('Pagina de Inicio')


class Home(generic.TemplateView):
    template_name='generales/home.html'
    