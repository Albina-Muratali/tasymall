from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.conf import settings

from core.models import *

from django.http import HttpResponse

def set_cookie(request):
    response = HttpResponse("Cookie is set")
    response.set_cookie('my_cookie', 'cookie_value', samesite='None', secure=True)
    return response

@login_required(login_url="/sign-in/?next=/courier/")
def home (request):
    return redirect(reverse('courier:available_jobs'))


@login_required(login_url="/sign-in/?next=/courier/")
def available_jobs_page (request):
    return render(request, 'courier/available_jobs.html',{
        "GOOGLE_MAP_API_KEY": settings.GOOGLE_MAP_API_KEY
    })


@login_required(login_url="/sign-in/?next=/courier/")
def available_job_page (request,id):
    job=Job.objects.filter(id=id, status=Job.PROCESSING_STATUS).last()

    if not job:
         return render(reverse,('courier/available_jobs'))

    return render(request, 'courier/available_job.html'),{
        "job":job
    }







