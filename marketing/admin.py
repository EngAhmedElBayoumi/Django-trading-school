from django.contrib import admin
#import courses lecture
from .models import Marketing_Lecture , Marketing_Course
# Register your models here.

#search
class Marketing_LectureAdmin(admin.ModelAdmin):
    search_fields = ['title']
    class Meta:
        model = Marketing_Lecture
        
#search
class Marketing_CourseAdmin(admin.ModelAdmin):
    search_fields = ['title']
    class Meta:
        model = Marketing_Course
        

admin.site.register(Marketing_Lecture,Marketing_LectureAdmin)
admin.site.register(Marketing_Course,Marketing_CourseAdmin)