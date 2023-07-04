from django.shortcuts import render
from testapp.models import HydJobs, BangaloreJobs, PuneJobs
import datetime

datetime = datetime.datetime.now()

# Create your views here.


def homepage_view(request):
    time = {"time": datetime}
    return render(request, "testapp/index.html", time)


# this function communicating with database it will bring data and display to the end user
# this request object pointing to http request object request variable is not mandatory if you are use x below also you use x
def hydjobs_view(request):
    jobs_list = HydJobs.objects.all()
    my_dict = {"jobs_list": jobs_list}
    return render(request, "testapp/hydjobs.html", my_dict)


def bengalurujobs_view(request):
    jobs_list = BangaloreJobs.objects.all()
    my_dict = {"jobs_list": jobs_list}
    return render(request, "testapp/bengalurujobs.html", my_dict)


def pune_jobs_view(request):
    jobs_list = PuneJobs.objects.all()
    my_dict = {"jobs_list": jobs_list}
    return render(request, "testapp/punejobs.html", my_dict)
