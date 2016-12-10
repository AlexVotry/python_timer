from django.shortcuts import render
from .models import TimeTracker
from django.http import HttpResponse
# from .forms import TimeForm

def index(request):
    jobs = TimeTracker.objects.all()
    return render(request, 'index.html', { 'jobs': jobs })

# def post_timetracker(request):
#     form = Timetracker(request.POST)
#     if form.is_valid():
#         form.save(commit = true)
#     return HttpResponse("Your time has been saved")

# class Timetracker:
#     def __init__(self, name, job, time):
#         self.name = name
#         self.job = job
#         self.time = time
#         self.date = date
#
# jobTimes = [
#     TimeTracker('Kim', 'teaching', '5:34:03'),
#     TimeTracker('Kim', 'driving', '1:20:53'),
#     TimeTracker('Kim', 'preparing', '1:58:41'),
# ]
