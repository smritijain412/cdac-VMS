from django.db import models
from django.db.models.signals import post_save

class UserProfile(models.Model):
    face_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    address = models.CharField(max_length = 100)
    phone = models.CharField(max_length =  10)
   
    def __str__(self):
        return self.name
class Userform(models.Model):
    face_id=models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    date=models.DateTimeField()
