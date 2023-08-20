
#import path
from django.urls import path

# import views
from . import views

#app_name
app_name = 'courses'

urlpatterns = [
    path('courses_category/',views.courses_category,name='courses_category'),
    path('courses_lect/<int:id>/',views.courses_lect,name='courses_lect'),
    path('course_details/<int:id>/',views.course_details,name='course_details'),
    
    #================================AR============================================
    
    path('ar/courses_category/',views.courses_category_ar,name='courses_category_ar'),
    path('ar/courses_lect/<int:id>/',views.courses_lect_ar,name='courses_lect_ar'),
    path('ar/course_details/<int:id>/',views.course_details_ar,name='course_details_ar'),
    
]
    