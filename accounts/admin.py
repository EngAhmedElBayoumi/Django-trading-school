from django.contrib import admin
#import membership
from .models import MemberShip,Profile
#search on membership,Profile
class MemberShipAdmin(admin.ModelAdmin):
    #search fields
    search_fields = ['name','price']

#Profile search
class ProfileAdmin(admin.ModelAdmin):
    search_fields = ['name','address','birth_date','coin']


#register
admin.site.register(MemberShip,MemberShipAdmin)
admin.site.register(Profile,ProfileAdmin)
