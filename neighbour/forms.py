from django.contrib.auth.models import User
from django import forms
from .models import Profile , Neighbourhood , Posts

class ProfileForm(forms.ModelForm):
  class Meta:
    model = Profile
    exclude = ['user']

class NeighbourhoodForm(forms.ModelForm):
  class Meta:
    model = Neighbourhood
    exclude = ['occupants_count']

class PostForm(forms.ModelForm):
  class Meta:
    model = Posts
    exclude= ['profile','neighbourhood']