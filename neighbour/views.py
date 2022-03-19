from email import message
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url="/accounts/loogin")
def index(request):
  message = "Love DJANGO!!"
  return render (request , 'neighbour/index.html',{"message":message})
