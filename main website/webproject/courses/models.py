from django.db import models
from django.utils.timezone import now

# Create your models here.
class Course(models.Model):
    sno =models.AutoField(primary_key=True)
    title =models.CharField(max_length=50)
    time= models.DateTimeField(blank=True)
    course_image = models.ImageField(upload_to="courses/images",default="")
    Content =models.TextField()
    file = models.FileField(upload_to="doc/course_download/", max_length=250,null="True",default='None')
 
    def __str__(self):
          return  self.title

class Webtemplate(models.Model):
    sno =models.AutoField(primary_key=True)
    title =models.CharField(max_length=50)
    time = models.DateTimeField(blank=True)
    web_image = models.ImageField(upload_to="c/images",default="")
    Content =models.CharField(max_length=50)
    sourcecode = models.FileField(upload_to="doc/course_download/", max_length=250,null="True",default='None')

    def __str__(self):
          return  self.title
