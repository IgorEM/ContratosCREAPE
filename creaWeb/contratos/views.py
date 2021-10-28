from django.contrib.auth.models import User
from django.shortcuts import render, HttpResponse, redirect
from creaWeb.contratos.models import Contratos
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http.response import Http404,JsonResponse

#Página de Login
def login_user(request):
   return render(request, 'login.html')

#Página de Logout
def logout_user(request):
    logout(request)
    return redirect('/')

#Pagina que lista os eventos
@login_required(login_url='/login/')
def lista_eventos(request):
    todosContratos = Contratos.objects.all()
    dados = {'contratos': todosContratos}
    return render(request, 'contratos.html', dados)

