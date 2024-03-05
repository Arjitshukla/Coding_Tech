from django.shortcuts import render
from about.models import About
# Create your views here.

def about(request):
  alltext = About.objects.all()
  context ={ "alltext":alltext }
  return render (request,"htmlfile/about.html",context)

