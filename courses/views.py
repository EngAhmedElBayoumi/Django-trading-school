from django.shortcuts import render
#import login_required
from django.contrib.auth.decorators import login_required
#import Profile from accounts
from accounts.models import Profile
#import course , lecture
from .models import Course , Lecture , Lecture_rate
#import redirct
from django.shortcuts import redirect
#import video file clip
from moviepy.editor import VideoFileClip, concatenate_videoclips


# Create your views here.

#courses_category
@login_required
def courses_category(request):
    user = request.user
    user_profile = Profile.objects.get(user=user)
    
    if user.has_right_sign:
        #get all course
         courses = Course.objects.all()
    else:
        #get course on user membership
        courses = Course.objects.filter(member_ship=user_profile.membership)
    
    #get number of all lecture in this course
    for course in courses:
        course.lectures_count = len(course.lecture_set.all())
    
    #get all couse duration 
    for course in courses:
        course.duration = 0
        for lecture in course.lecture_set.all():
            video = VideoFileClip(lecture.video.path)
            course.duration += video.duration
        course.duration = round(course.duration / 60,1)
        course.duration = str(course.duration) + ' min'
    
    #set fully_star and empty_star in course depend on course.rate
    for course in courses:
        course.fully_star = range(course.rate)
        course.empty_star = range(5-course.rate)
        
    
    

    context={
        'profile':user_profile,
        'courses':courses,
    }
    return render(request,'courses.html',context)

#courses_lect
@login_required
def courses_lect(request,id):
    user = request.user
    user_profile = Profile.objects.get(user=user)
    #get lecture 
    lectures = Lecture.objects.filter(course=id)
    #get all lectures video duration
    for lecture in lectures:
        video = VideoFileClip(lecture.video.path)
        lecture.duration = video.duration
        lecture.duration = round(lecture.duration / 60,1)
        lecture.duration = str(lecture.duration) + ' min'
    
    
    #set fully_star and empty_star in lecture depend on lecture.Lecture_rate
    for lecture in lectures:
        lecture.fully_star = range(lecture.rate)
        lecture.empty_star = range(5-lecture.rate)

    
    
    context={
        'profile':user_profile,
        'lectures':lectures,
    }
    return render(request,'course-lect.html',context)

#course_details
@login_required
def course_details(request,id):
    user = request.user
    user_profile = Profile.objects.get(user=user)
    #get lecture by id
    lecture = Lecture.objects.get(id=id)
     #get course for this lecture
    course = Course.objects.get(id=lecture.course.id)

    #rate if requect post 
    if request.method == "POST":
        star=int(request.POST['star'])
        
        #chech if this user  rate before in this  lecture 
        if Lecture_rate.objects.filter(user=user,lecture=lecture).exists(): 
            #get this user rate
            user_rate = Lecture_rate.objects.get(user=user,lecture=lecture)
            #update this user rate
            user_rate.star = star
            user_rate.save() 
        else:
            #create new rate
            Lecture_rate.objects.create(user=user,lecture=lecture,star=star)
        
        #get all lecture rate
        rates = Lecture_rate.objects.filter(lecture=lecture)
        #get all lecture rate count
        lecture.rate_count = len(rates)
        #get all lecture rate sum
        lecture.rate_sum = 0
        for rate in rates:
            lecture.rate_sum += rate.star
        #get all lecture rate avg
        if lecture.rate_count != 0:
            lecture.rate = round(lecture.rate_sum / lecture.rate_count) 
            lecture.save()
        else:
            lecture.rate = 0
            lecture.save() 
        
        #set course.rate depend on the lectures rate
        #get all course lectures
        lectures = Lecture.objects.filter(course=course)
        #get all course lectures rate count
        course.rate_count = 0
        for lecture in lectures:
            course.rate_count += 1
        #get all course lectures rate sum
        course.rate_sum = 0
        for lecture in lectures:
            course.rate_sum += lecture.rate
        #get all course lectures rate avg
        if course.rate_count != 0:
            course.rate = round(course.rate_sum / course.rate_count) 
            course.save()
        else:
            course.rate = 0
            course.save()
        
          
        

    context={
        'profile':user_profile,
        'lecture':lecture,
    }
    return render(request,'course-details.html',context)