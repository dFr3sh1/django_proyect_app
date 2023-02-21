from django.db import models
from django.contrib.auth.models import AbstractUser


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
    username = models.CharField(max_length=50, blank=True, null=True, unique=True)
    date = models.DateTimeField()
    schedules = models.CharField(max_length=50, choices=TIME_SLOTS, default='Horaires')
    message = models.CharField(max_length=100, null=True)
    
    

class User(AbstractUser):
    """
    User class with an argument AbstractUseer
    Args:
        AbstractUser User type to assign rols for users
    """
    username = models.CharField(max_length=50, blank=True, null=True, unique=True)
    email = models.EmailField(name='email address', unique=True, null=True)
    native_name = models.CharField(max_length=50, null=True)
    phone = models.CharField(max_length=12)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']
    def __str___(self):
        return "{}".format(self.email)# Create your models here.
