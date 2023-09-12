from django.contrib import admin
#import MemberShip, CustomUser
from .models import CustomUser
# Register your models here.

    
#search on customuser by name or email or phone 
class CustomUserAdmin(admin.ModelAdmin):
    #search fields
    search_fields = ['email','phone']

admin.site.register(CustomUser,CustomUserAdmin)
