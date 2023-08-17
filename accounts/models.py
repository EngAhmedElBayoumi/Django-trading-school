from django.db import models
#import validation error
from django.core.exceptions import ValidationError
#import custom_user from users.models
from users.models import CustomUser


# Create your models here.
#membership model with field name , price
class MemberShip(models.Model):
    name=models.CharField(max_length=100)
    price=models.FloatField()
        #validate price must be mod(50)
    def clean(self):
        if self.price % 50 != 0:
            raise ValidationError('price must be (50,100,150,....)')
    def __str__(self):
        return self.name

#profile model every profile related to user and must has membership plane 
class Profile(models.Model):
    user=models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    membership=models.ForeignKey(MemberShip,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    birth_date=models.DateField(null=True,blank=True)
    coin=models.IntegerField(default=0)
    image=models.ImageField(upload_to='static/users/',null=True,blank=True)
    #new field marketing_avilable
    marketing_avilable=models.BooleanField(default=False)
    #new field rank
    rank=models.IntegerField(default=0)
    
    def __str__(self):
        return self.name    
    
        # # Check if there are any records in the Membership table
        # if MemberShip.objects.count() == 0:
        #     # Create a default Membership record
        #     default_membership = MemberShip.objects.create(name='basic', price=50)
        #     extra_fields['membership'] = default_membership