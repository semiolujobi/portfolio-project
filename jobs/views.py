from django.shortcuts import render
from .models import Job
#from .models import Extra

# Create your views here.
def home(request):
    jobs = Job.objects
    #extras = Extra.objects
    return render(request, 'jobs/home.html', {'jobs':jobs})