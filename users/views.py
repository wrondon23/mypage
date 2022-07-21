from django.http import HttpRequest
from django.shortcuts import render
from .models import Profile

# Create your views here.

def ProfileUser(request):
    profile = Profile.objects.all()
    context ={'profile':profile}
    return render(request, 'users/profiles.html', context)
 