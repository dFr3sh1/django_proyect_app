from django.contrib import admin
from authentication.models import Appointments
from django.contrib.auth.models import AbstractUser, User
from django.conf import settings


class AppointmentsAdmin(admin.ModelAdmin):
    """To display the coordonates in the admin appointments' vue

    Args:
        admin (_type_): heritance form the model admin
    """
    list_display = ('name', 'phone', 'email', 'date', 'schedules')

class UserAdmin(admin.ModelAdmin):
    list_displayc = ('name', 'phone', 'Rôle')
    
# class UserAdmin(admin.ModelAdmin):
#     def save_model(self, request, obj, form, change):
#         if request.user.is_superuser:
#             obj.is_staff = True
#             obj.save()
#  User, UserAdmin
admin.site.register(Appointments, AppointmentsAdmin)
admin.site.register(User, UserAdmin)

# Register your models here.
