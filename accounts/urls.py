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
    #upgrade_membership
    path('upgrade_membership/',views.upgrade_membership,name='upgrade_membership'),
    
    #================================AR============================================
    path('ar/login/',views.log_in_ar,name='login_ar'),
    path('ar/logout/',views.log_out_ar,name='logout_ar'),
    path('ar/profile/',views.profile_ar,name='profile_ar'),
    path('ar/add_new_member/',views.add_new_member_ar,name='add_new_member_ar'),
    path('ar/send_coin/',views.send_coin_ar,name='send_coin_ar'),
    path('ar/forget_pass/',views.forget_pass_ar,name='forget_pass_ar'),
    path('ar/team_profile/<int:id>/',views.team_profile_ar,name='team_profile_ar'),
    #upgrade_membership
    path('ar/upgrade_membership/',views.upgrade_membership_ar,name='upgrade_membership_ar'),
]
