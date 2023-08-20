# hello/scheduler.py
from apscheduler.schedulers.background import BackgroundScheduler
#import Customuser
from users.models import CustomUser
#import timezone
from django.utils import timezone



def Block_users():
    #block user that ended_at<now and not has right sign
    blockeduser=CustomUser.objects.filter(ended_at__lt=timezone.now(),has_right_sign=False)
    for user in blockeduser:
        user.is_blocked=True
        user.save()
  

def hello():
    print("hello")
    
    
def start_scheduler():
    scheduler = BackgroundScheduler()
    #every day
    scheduler.add_job(Block_users, 'interval', days=1)
    scheduler.start()

