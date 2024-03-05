from django.shortcuts import render
from courses.models import Course,Webtemplate
# Create your views here.

def courses(request):
  allcourse = Course.objects.all()
  context ={'allCourse':allcourse}
  return render (request,"htmlfile/courses.html",context)

def temp(request):
  allweb = Webtemplate.objects.all()
  context ={'allweb':allweb}
  return render (request,"htmlfile/courses.html",context)

