from django.shortcuts import render
#import login 
from django.contrib.auth import authenticate, login,logout
# import login_required
from django.contrib.auth.decorators import login_required
#import redirct
from django.shortcuts import redirect
#import message
from django.contrib import messages
#import customsuer from users.models
from users.models import CustomUser
#import profile , membership from .models
from .models import Profile,MemberShip
#import timezone
from django.utils import timezone

#timedelta
from datetime import timedelta
# Create your views here.

#log_in 
def log_in(request):
    #login 
    if request.method == 'POST':
        #get username and password from form
        username = request.POST.get('username')
        password = request.POST.get('password')
        #authenticate user
        user = authenticate(request, username=username, password=password)
        access=False
        
        if user is not None:
            access=True
        else:
            #send message
            messages.error(request, 'the login data not correct')
            return render(request,'index.html')
    #check if user is blocked
        if user.is_blocked:
            #send message
            messages.error(request, 'your account is blocked')
            return render(request,'index.html')
        
        
        #if access = True login
        if access:
            login(request, user)
            #redirct to profile 
            return redirect('accounts:profile')

    return render(request,'index.html')

#log_out
#login_required
@login_required
def log_out(request):
    logout(request)
    #redirct to login 
    return redirect('accounts:login')
    


#profile
@login_required
def profile(request):
    user = request.user
    user_profile = Profile.objects.get(user=user)
    membership = MemberShip.objects.get(id=user_profile.membership.id)
    memberships = MemberShip.objects.all()
    custom_user = CustomUser.objects.get(id=user.id)
    users = CustomUser.objects.filter(create_by=user)
    users_profiles = Profile.objects.filter(user__in=users)
    total_partners = 0
    for partner_profile in users_profiles:
        partner_count = Profile.objects.filter(user__create_by=partner_profile.user).count()
        partner_profile.partner_count = partner_count
        total_partners += partner_count

    my_partners = total_partners + users.count()
    
    context = {
        'profile': user_profile,
        'membership': membership,
        'memberships': memberships,
        'custom_user': custom_user,
        'users': users,
        'users_profiles': users_profiles,
        'total_partners': total_partners,
        'my_partners': my_partners
    }
    return render(request, 'profile.html', context)

#add_new_member
@login_required
def add_new_member(request):
    #if request.method==post get name , email , phone , address , password , birthdate , membership , image , create_by from request.user 
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        address=request.POST.get('address')
        password=request.POST.get('password')
        birthdate=request.POST.get('birthdate')
        membership=request.POST.get('membership')
        image=request.FILES.get('image')        
        create_by=request.user
         #check if email and phone unique
        if CustomUser.objects.filter(email=email).exists():
            #return message "email is exist"
            messages.error(request, 'email is exist')
            return redirect('accounts:profile')
        if CustomUser.objects.filter(phone=phone).exists():
            #return message "phone is exist"
            messages.error(request, 'phone is exist')
            return redirect('accounts:profile')
        
        #get membership.price        
        #check if profile.coin => membership.price
        profile = Profile.objects.get(user=create_by)
        membershipobject = MemberShip.objects.get(id=membership)
        if profile.coin < membershipobject.price:
            #message
            messages.error(request, 'you dont have enough coin for this membership')
            return redirect('accounts:profile')
        else:
            #profile.coin = profile.coin - membership.price
            profile.coin = profile.coin - membershipobject.price
            #profile.save()
            profile.save()

       
        
        # create user with fields phone , email , create_by
        user = CustomUser.objects.create_user(phone=phone,email=email,create_by=create_by)
        #set password for user
        user.set_password(password)
        #save user
        user.save()
        #get membership instance
        membershipobject = MemberShip.objects.get(id=membership)
        #create profile with fields name , address , birthdate , membership , image , user
        profileobject = Profile.objects.create(name=name,address=address,birth_date=birthdate,membership=membershipobject,image=image,user=user)
        #save profile
        profileobject.save()
        
        #get myprofile
        myprofile = Profile.objects.get(user=create_by)
        # myprofile rank +1
        myprofile.rank = myprofile.rank + 1
        #myprofile.save()
        myprofile.save()
        #if rank >= 50 then customuser.has_right_sign=true
        if myprofile.rank >= 50:
            create_by.has_right_sign = True
            create_by.save()
            
        
        
        
    #redirct to profile
    return redirect('accounts:profile')



#forget_pass
def forget_pass(request):
    #if request post message we have send link for you
    if request.method=='POST':
        #get phone from request
        email = request.POST.get('email')
        #check if phone exist
        if CustomUser.objects.filter(email=email).exists():
            #get user from phone
            user = CustomUser.objects.get(email=email)
            #check if user is blocked
            if user.is_blocked:
                #message
                messages.error(request, 'your account is blocked you can\'t change your password')
                return redirect('accounts:forget_pass')
            #check if user is blocked
            #message
            messages.success(request, 'we have send link for you. Check your email please')
            return redirect('accounts:forget_pass')
        else:
            #message
            messages.error(request, 'You Don\'t have an Account')
            return redirect('accounts:forget_pass')
    return render(request,'forget-pass.html')


#send coin
@login_required
def send_coin(request):
    #send coin from request.user to user that send phone in the requesr
    if request.method=='POST':
        #get phone , coin from request
        phone = request.POST.get('phone')
        coin = request.POST.get('coin')
        #check if phone exist
        if CustomUser.objects.filter(phone=phone).exists():
            #get user from phone
            user = CustomUser.objects.get(phone=phone)
            #get profile from user
            profile = Profile.objects.get(user=user)
            #get coin that request.user have
            #check if coin that request.user have => coin
            if request.user.profile.coin < int(coin):
                messages.error(request, 'you dont have enough coin')
                return redirect('accounts:profile')
            
            #check is not super user request.user.profile.coin-coin
            
            request.user.profile.coin = request.user.profile.coin - int(coin)
            request.user.profile.save()
             
            #profile.coin = profile.coin + coin
            profile.coin = profile.coin + int(coin)
            #profile.save()
            profile.save()
        
            #check if user isblocked
            if user.is_blocked:
                profile.coin = profile.coin - 50
                profile.save()
                #unblock
                user.is_blocked = False
                #ended_at +30 day
                user.ended_at = user.ended_at + timedelta(days=30)
                user.save()
            
            #message
            return redirect('accounts:profile')
        else:
            return redirect('accounts:profile')
        
    return redirect('accounts:profile')



@login_required
def team_profile(request,id):
    user = CustomUser.objects.get(id=id)
    user_profile = Profile.objects.get(user=user)
    membership = MemberShip.objects.get(id=user_profile.membership.id)
    memberships = MemberShip.objects.all()
    custom_user = CustomUser.objects.get(id=user.id)
    users = CustomUser.objects.filter(create_by=user)
    users_profiles = Profile.objects.filter(user__in=users)

    
    forign=1
    total_partners = 0
    for partner_profile in users_profiles:
        partner_count = Profile.objects.filter(user__create_by=partner_profile.user).count()
        partner_profile.partner_count = partner_count
        total_partners += partner_count

    my_partners = total_partners + users.count()
    
    context = {
        'profile': user_profile,
        'membership': membership,
        'memberships': memberships,
        'custom_user': custom_user,
        'users': users,
        'users_profiles': users_profiles,
        'total_partners': total_partners,
        'my_partners': my_partners,
        'forign':forign,
    }
    return render(request, 'profile.html', context)

