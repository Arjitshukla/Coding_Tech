from django.shortcuts import render
from contact.models import Contact    
from django.contrib import messages
# Create your views here.
def contact(request):
  if request.method =="POST":
        name=request.POST['name']
        Email=request.POST['email']
        phone=request.POST['phone']
        Content =request.POST['content']
        if len(name)<3 or len(Email)<3 or len(phone)<10 or not phone.isdigit() or len(Content)<5:
            messages.error(request, "Kindly complete the form with accurate information.")
        else:
            contact=Contact(name=name, Email=Email, phone=phone, Content=Content)
            contact.save()
            messages.success(request, "Your message has been received. Thank you for contacting us! ")
  return render (request,"htmlfile/contact.html") 