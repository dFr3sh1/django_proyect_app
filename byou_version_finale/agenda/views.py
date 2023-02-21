from django.shortcuts import render, redirect,  get_object_or_404
from django.forms import forms
from django.contrib.auth import authenticate, login
from agenda.forms import NewUserForm
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Appointments
from django.contrib.auth.views import LoginView, LogoutView
from datetime import datetime, timedelta
from django.contrib.auth.models import User
from django.contrib.auth.forms import  UserCreationForm




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
    
    


# def login(request):
#     form = LoginForm()
#     message = ''
#     if request.method == 'POST':
#         form = forms.LoginForm(request.POST)
#         if form.is_valid():
#             user = authenticate(
#                 username=form.cleaned_data['username'],
#                 password=form.cleaned_data['password'],
#             )
#             if user is not None:
#                 login(request, user)
#                 message = f'Bonjour, {user.username}! Vous êtes connecté.'
#             else:
#                 message = 'Identifiants invalides.'
#     return render(
#         request, 'agenda/login.html', context={'form': form, 'message': message})
    

class LoginView(LoginView):
    template_name = 'login.html'

def appointment(request):
    if request.method == 'POST':
        username = request.user
        first_name = username.first_name
        last_name = username.last_name
        email = username.email
        date_str = request.POST.get('date')
        date = datetime.fromisoformat(date_str)
        hour = date.time().hour
        minute = date.time().minute
        weekday = date.weekday()
        if weekday < 0 or weekday > 4:
            return render(request, 'appointment.html', {'error_message': 'Jours de RDV du lundi à vendredi'})
        if not ((9 <= hour < 12 and minute == 0) or (hour == 12 and minute ==  30) or (13 <= hour < 17)):
            return render( request, 'appointment.html', {'error_message': 'Horaire non  disponible'})
        time_hour_minute = date.replace(hour=hour, minute=minute)
        end_time = time_hour_minute + timedelta(minute=10)
        if Appointments.objects.filter(date__range=[time_hour_minute, end_time]).exists():
            return render(request, 'appointment.html', {'error_message': 'Horaire indisponible'})
        appointment = Appointments.objects.create(
            username = username,
            first_name = first_name,
            last_name = last_name,
            email = email,
            date = time_hour_minute,
            duree =10
        )
        return render('confirmation.html')
    return render(request, 'agenda/appointment.html')
            
        
        
        
    # form = AppointmentsForm()
    # message = ''
    # if request.method == 'POST':
    #     form = AppointmentsForm(request.POST)
    #     if form.is_valid():
    #         form = form.cleaned_data
    #         appointment = Appointments.objects.filter(date=form['date'], schedules=form['schedules']).exists()
    #         if appointment:
    #             form.add_error('date', 'Creénau est déjà pris. Veuillez choisir une autre date ou heure.')
    #             appointment.save()
    #         login(request)
    #         messages.success(request, "Rendez-vous enregistré.")
    #         return redirect("agenda/index.html")
    #     else:
    #         messages.error(request, "Votre enregistrement n'est pas validé. Merci de saisir à nouveau votre formulaire")
    # return render(request, "agenda/appointment.html", context={'form':form, 'messages':messages})

def historial(request):
    return HttpResponse('<h1>Votre historique</h1>')

class LogoutView(LogoutView):
    template_name = 'logout.html'
    
    # messages.info(request, "Vous êtes bien deconnecté")
    # return redirect('agenda/login.html')
# Create your views here.
