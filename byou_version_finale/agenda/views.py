from django.shortcuts import render, redirect
from django.forms import forms
from django.contrib.auth import authenticate, login, logout
from agenda.forms import NewUserForm, LoginForm, AppointmentsForm
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Appointments




def confirmation(request):
    return render(request, 'agenda/confirmation.html')

def index(request):
    return render(request, 'agenda/index.html')

def signup(request):
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Enregistrement validé.")
            return redirect("agenda/index.html")
        #messages.error(request, "Votre enregistrement n'est pas validé. Merci de saisir à nouveau votre formulaire")
    form = NewUserForm()
    return render(request, "agenda/signup.html", context={'form': form})

# class LoginPage(View):
#     form_class = forms.LoginForm()
#     template_name = "agenda/login.html"
#     def get(self, request):
#         form = self.form_class()
#         messages = ''
#         return render(request, self.template_name, context={'form': form, 'messages': messages})
    
#     def post(self, request):
#         form = self.form_class(request.POST)
#         messages = ''
#         if form.is_valid():
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password')
#             user = authenticate(username=username, password=password)
#             if user is not None:
#                 login(request, user)
#                 messages.info(request, f'Vous êtes connecté {username}.')
#                 return redirect('agenda:index')
#             else:
#                 messages.error(request, "Identifiants invalides.")
#         form = self.form_class()
#         return render(request, self.template_name, context={'form': form, 'messages': messages})
    
    

def login(request):
    form = LoginForm()
    message = ''
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                message = f'Bonjour, {user.username}! Vous êtes connecté.'
            else:
                message = 'Identifiants invalides.'
    return render(
        request, 'agenda/login.html', context={'form': form, 'message': message})
    

def appointment(request):
    form = AppointmentsForm()
    message = ''
    if request.method == 'POST':
        form = AppointmentsForm(request.POST)
        if form.is_valid():
            form = form.cleaned_data
            appointment = Appointments.objects.filter(date=form['date'], schedules=form['schedules']).exists()
            if appointment:
                form.add_error('date', 'Ce  crénau est déjà pris. Veuillez choisir une autre date ou heure.')
                appointment.save()
            login(request)
            messages.success(request, "Rendez-vous enregistré.")
            return redirect("agenda/index.html")
        else:
            messages.error(request, "Votre enregistrement n'est pas validé. Merci de saisir à nouveau votre formulaire")
    return render(request, "agenda/appointment.html", context={'form':form, 'messages':messages})

def historial(request):
    return HttpResponse('<h1>Votre historique</h1>')

def logout_user(request):
    logout(request)
    # messages.info(request, "Vous êtes bien deconnecté")
    return redirect('agenda/login.html')
# Create your views here.
