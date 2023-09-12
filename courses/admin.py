from django.contrib import admin
#import courses lecture
from .models import Lecture , Course
# Register your models here.

#search
class LectureAdmin(admin.ModelAdmin):
    search_fields = ['title']
    class Meta:
        model = Lecture
        
#search
class CourseAdmin(admin.ModelAdmin):
    search_fields = ['title']
    class Meta:
        model = Course
        

admin.site.register(Lecture,LectureAdmin)
admin.site.register(Course,CourseAdmin)