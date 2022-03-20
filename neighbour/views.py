from email import message
from django.shortcuts import render , redirect
from django.contrib.auth.decorators import login_required
from django.db import transaction
from neighbour.models import Profile , Business ,Neighbourhood
from .forms import ProfileForm , NeighbourhoodForm
from django.contrib import messages

# Create your views here.
@login_required(login_url="/accounts/login/")
def index(request):

  current_user = request.user
  if request.method == 'POST':
    upload_neighbourhood = NeighbourhoodForm(request.POST,request.FILES)

    if upload_neighbourhood.is_valid():
      neighbourhood = upload_neighbourhood.save(commit=False)
      neighbourhood.occupants_count = 500000
      neighbourhood.user = current_user
      neighbourhood.save()

      return redirect('index')
  
  else:
    upload_neighbourhood = NeighbourhoodForm()

  return render (request , 'neighbour/index.html',{"message":message , "form":upload_neighbourhood})



@transaction.atomic
@login_required(login_url ='/accounts/login')
def profile(request):
  current_user = request.user
  user_profile = Profile.objects.filter(id = current_user.id)
  business_near_me = Business.objects.filter(profile_id = current_user.id).all()


  if request.method == 'POST':
    create_profile = ProfileForm(request.POST ,request.FILES ,  instance = request.user.profile )

    if create_profile.is_valid():
      user_profile = create_profile.save(commit = False)
      user_profile.save()

      messages.success(request,('Your profile was successfully updated!'))
      return redirect('profile')
    
    else:
      messages.error(request,"please correct the error below")
  
  else:
     create_profile= ProfileForm(instance= request.user.profile)

    


  return render (request,'neighbour/profile.html', {"form" : create_profile})
