from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views.generic import TemplateView
from django.views import View
from django import forms
from decimal import Decimal
from .models import *
from .forms import *

class HomePage(TemplateView):
    template_name = 'home.html'
    def get(self, request):
        viewData = {}
        viewData["title"] = "Title of the view"
        viewData["subtitle"] =  "Subtitle of the view"
        viewData["events"] = Evento.objects.all()
        return render(request,self.template_name,viewData)
    

class EventIndexView(TemplateView):
    template_name = 'events_index.html'

    def get(self, request):
        viewData = {}
        viewData["title"] = "Title of the view"
        viewData["subtitle"] =  "Subtitle of the view"
        viewData["events"] = Evento.objects.all()

        return render(request, self.template_name, viewData)


class EventShowView(View):
    template_name = 'show_event.html'

    def get(self, request, id):
        view_data = {}
        view_data["event"] = get_object_or_404(Evento, pk=id)
        view_data["comentario_form"] = ComentarioForm()
        view_data["comentarios"] = Comentario.objects.filter(evento=view_data["event"])
        
        return render(request, self.template_name, view_data)

    def post(self, request, id):
        event = get_object_or_404(Evento, pk=id)
        form = ComentarioForm(request.POST)

        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.evento = event
            comentario.usuario = request.user
            comentario.save()
            messages.success(request, 'Comentario agregado con éxito.')
        else:
            messages.error(request, 'Error al agregar el comentario. Por favor, verifica el formulario.')

        return redirect('show_event', id=id)
    
class LikeEventView(View):
    def get(self, request, id):
        evento = get_object_or_404(Evento, id=id)

        # Verifica si el usuario ya dio "Me gusta" al evento
        like, created = Like.objects.get_or_create(evento=evento, usuario=request.user)

        if not created:
            # Si ya dio "Me gusta", elimina el "Me gusta"
            like.delete()
        else:
            # Si no ha dado "Me gusta", crea el "Me gusta"
            Like.objects.create(evento=evento, usuario=request.user)

        return redirect('show_event', id=id)

@method_decorator(login_required, name='dispatch')
class EditEventView(View):
    template_name = 'edit_event.html'

    def get(self, request, id):
        evento = get_object_or_404(Evento, id=id)
        
        # Verificar si el usuario actual es el organizador del evento
        if request.user != evento.organizador:
            return redirect('events_index')
        
        form = EventoForm(instance=evento)
        return render(request, self.template_name, {'form': form, 'evento': evento})

    def post(self, request, id):
        evento = get_object_or_404(Evento, id=id)
        
        # Verificar si el usuario actual es el organizador del evento
        if request.user != evento.organizador:
            return redirect('events_index')
        
        form = EventoForm(request.POST, instance=evento)
        if form.is_valid():
            form.save()
            return redirect('show_event', id=evento.id)
        return render(request, self.template_name, {'form': form, 'evento': evento})

class CreateEventView(LoginRequiredMixin, View):
    template_name = 'create_event.html'
    login_url = '/login/' 

    def get(self, request):
        form = EventoForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = EventoForm(request.POST)
        if form.is_valid():
            evento = form.save(commit=False)
            evento.organizador = request.user 
            evento.save()
            return redirect('show_event', id=evento.id)
        return render(request, self.template_name, {'form': form})


@method_decorator(login_required, name='dispatch')
class DeleteEventView(View):
    def get(self, request, id):
        evento = get_object_or_404(Evento, id=id)

        # Verificar si el usuario actual es el creador del evento
        if request.user == evento.organizador:
            evento.delete()
            messages.success(request, 'Evento eliminado con éxito.')
        else:
            messages.error(request, 'No tienes permisos para eliminar este evento.')

        return redirect('events_index')

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('home')

def user_signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

class UserEventsView(View):
    template_name = 'user_events.html'

    def get(self, request):
        user_events = Evento.objects.filter(organizador=request.user)
        return render(request, self.template_name, {'user_events': user_events})
