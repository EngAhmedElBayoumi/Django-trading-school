from django.urls import path
# import views
from . import views
#app_name
app_name = 'contact'

urlpatterns = [
    path('contact/',views.contact,name='contact'),

]
