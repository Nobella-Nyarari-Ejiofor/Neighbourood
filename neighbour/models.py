from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Neighbourhood(models.Model):
  neighbourhood_name = models.CharField(max_length=30 , null=False)
  neighbourhood_location = models.CharField(max_length=30, null=False)
  occupants_count = models.IntegerField()


  def create_neighbourhood(self):
    """
    A function that saves profile 
    """
    self.save()

  def delete_neighbourhood(self):
    """
    A function that deletes a profile 
    """
    Neighbourhood.objects.filter(id = self.id).delete()

  def find_neighbourhood(self, id):
    """
    A function that gets the neighbourhood by id
    """
    Neighbourhood.objects.filter(id=self.id)




class Profile(models.Model):
  """
  A model that contains user's info for the profile
  """
  user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile', null=True)
  bio = models.TextField(max_length=500 , blank= True , null=True)
  photo=models.ImageField(upload_to="profile/" , blank=True)
  profile_email=models.EmailField(max_length = 100, blank=True ,null= True)
  location = models.CharField(max_length=30 , blank=True)
  neighbourhood_name = models.ForeignKey(Neighbourhood,on_delete=models.CASCADE)
  def __str__(self):
    return f'{self.user.username}'

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
     if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
     instance.profile.save()




class Business(models.Model):
  business_name = models.CharField(max_length = 50, null=False)
  profile = models.ForeignKey(Profile,on_delete=models.CASCADE)
  neighbourhood= models.ForeignKey(Neighbourhood,on_delete=models.CASCADE)
  business_email = models.EmailField(max_length=100)

  def create_business(self):
    self.save()

  def delete_business(self):
    Business.objects.filter(id = self.id).delete()

  def find_business(self):
    Business.objects.filter(id =self.id).first()

  def update_business(self):
    """
    A function thta updates the business
    """









  