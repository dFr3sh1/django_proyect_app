from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from django.views.generic import View
from . import forms
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from authentication.forms import LoginForm, AppointmentsForm
from django.core.mail import send_mail

def email_sent(request):
    message = 'Votre rendez vous a été bien enregistré'
    return render(request, 'authentication/confirmation.html')

def signup_page(request):
    return render(request, 'authentication/sign_up.html') 

def logout_user(request):
    logout(request)
    return redirect('login')

class LoginPage(View):
    form_class = forms.LoginForm
    template_name = 'authentication/login.html'
    
    def get(self, request):
        form = self.form_class()         
        message = ''        
        return render(request, self.template_name, context={'form':form, 'message': message})
    
    def post(self, request):
        form = self.form_class(request.POST)            
        message = ''
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                message = f'Bonjour, {user.username}! Vous êtes connecté.'
                # return render(request, 'authentication/login.html')
            else:
                message = 'Identifiants invalides.'
                # send_mail(
                #     subject=f'message from {form.cleaned_data["username"] or "anonyme"} via bYou Login View form',
                #     message=form.cleaned_data['message'],
                #     from_email=form.cleaned_data['email'],
                #     recipient_list=['admin@bYou.xyz'],
                # )
        return render(request, self.template_name, context={'form':form, 'message': message})


def home(request):
    return render(request, 'authentication/home.html')

def appointments(request):
    form = AppointmentsForm()
    return render(request, 'authentication/appointments.html')

# @login_required
def historique(request):
    return render(request, 'authentication/historique.html')
# Create your views here.
