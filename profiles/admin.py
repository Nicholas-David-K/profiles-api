from django.contrib import admin
from profiles.models import UserProfile
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext as _

# Register your models here.
class AdminUser(UserAdmin):
  
   ordering = ['id']
   list_display = ['first_name', 'last_name', 'email']
   fieldsets = (
     (None, {'fields': ('email', 'password')}),
     (_('personal Info'), {'fields': ('first_name', 'last_name')}),
     (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser')}),
     (_('Inportant dates'), {'fields': ('last_login',)})
   )
   add_fieldsets = (
     (None, {'classes': ('wide',), 'fields': ('first_name', 'last_name', 'email', 'password1', 'password2')}),
   )

admin.site.register(UserProfile, AdminUser)
