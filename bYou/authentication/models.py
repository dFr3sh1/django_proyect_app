from django.contrib.auth import authenticate
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings
User = settings.AUTH_USER_MODEL
# from django.contrib.auth  import get_user_model
#User = get_user_model()

TIME_SLOTS = [('9:00', '9:00'),
              ('9:55', '9:55'),
              ('10:50', '10:50'),
              ('11:45', '11:45'),
              ('13:30', '13:30'),
              ('14:25', '14:25'),
              ('15:20', '15:20'),
              ('16:15', '16:15'),
              ('17:10', '17:10')
              ]


class Appointments(models.Model):
    def __str__(self):
        return f'{self.name}'
    # models.fields.CharField(max_length=50, null=True)
    name = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    phone = models.fields.IntegerField(blank=True, null=True)  
    email = models.fields.EmailField(blank=True, null=True)
    date = models.DateField()
    schedules = models.CharField(max_length=50, choices=TIME_SLOTS, default='Horaires')
    message = models.CharField(max_length=100, null=True)
    
    

class User(AbstractUser):
    """
    User class with an argument AbstractUseer
    Args:
        AbstractUser User type to assign rols for users
    """
    COACH = 'COACH'
    CUSTOMER = 'CUSTOMER'
    
    
    ROLE_CHOICES = (
        (COACH, 'Coach'),
        (CUSTOMER, 'Customer')        
        )
    name = models.CharField(max_length=70, blank=True, null=True)
    first_name = models.CharField(max_length=70, blank=True, null=True)
    last_name = models.CharField(max_length=70, blank=True, null=True)
    password = models.CharField(max_length=8)
    email = models.EmailField(blank=True, null=True)
    phone = models.fields.CharField(max_length=10, blank=True, null=True)
    role = models.CharField(max_length=30, choices=ROLE_CHOICES, verbose_name='Rôle', null=True )
    
