# import path
from django.urls import path
# import views
from . import views

#app_name
app_name = 'accounts'

urlpatterns = [
    path('login/',views.log_in,name='login'),
    path('logout/',views.log_out,name='logout'),
    path('profile/',views.profile,name='profile'),
    path('add_new_member/',views.add_new_member,name='add_new_member'),
    path('send_coin/',views.send_coin,name='send_coin'),
    path('forget_pass/',views.forget_pass,name='forget_pass'),
    path('team_profile/<int:id>/',views.team_profile,name='team_profile'),
    
]
