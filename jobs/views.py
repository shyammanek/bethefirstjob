from django.shortcuts import render

# Create your views here.
from jobs.models import joblist

def home(request):
    all_jobs = joblist.objects.all
    return render(request,'home.html',{'all_jobs':all_jobs})
