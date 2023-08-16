from django.shortcuts import render
# import login_required
from django.contrib.auth.decorators import login_required
# Create your views here.
#import profile from accounts
from accounts.models import Profile

#home
@login_required
def home(request):
    user = request.user
    user_profile = Profile.objects.get(user=user)
    
    
    
    
    context={
        'profile':user_profile,
    }
    return render(request,'home.html',context)


#error_404_view
@login_required
def error_404_view(request,exception):
    user = request.user
    user_profile = Profile.objects.get(user=user)
    
    
    
    
    context={
        'profile':user_profile,
    }
    return render(request,'404.html',context)
@login_required
def error_500_view(request):
    user = request.user
    user_profile = Profile.objects.get(user=user)
    
    
    
    
    context={
        'profile':user_profile,
    }
    return render(request,'404.html',context)



