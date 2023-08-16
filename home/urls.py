from django.urls import path
# import views
from . import views
#app_name
app_name = 'home'

urlpatterns = [
    path('',views.home,name='home'),
]

