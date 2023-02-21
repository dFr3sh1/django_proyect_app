from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import  UserCreationForm
from django.contrib.auth.models import User
from agenda.models import Appointments

class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")
        
    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
    
                                
class LoginForm(forms.ModelForm):
    """
    Form class with one parameter from forms.

    Args:
        forms (_Form_): take two arguments to access user to the site
    """      
    username = forms.CharField(max_length=63, label='Nom d’utilisateur')
    password = forms.CharField(max_length=63, widget=forms.PasswordInput, label='Mot de passe')
    
class AppointmentsForm(forms.ModelForm):    
    class Meta:
        model = Appointments
        fields = ("__all__")

    
    
    

    
    