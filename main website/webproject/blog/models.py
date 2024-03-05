from django.db import models
from django.utils.timezone import now

# Create your models here.
class Post(models.Model):
    sno =models.AutoField(primary_key=True)
    title =models.CharField(max_length=50)
    author =models.CharField(max_length=13)
    Content =models.TextField()
    Content2 =models.TextField()
    head0 =models.CharField(max_length=50)
    para0 =models.TextField()
    para1 =models.TextField()
    timeStamp = models.DateTimeField(blank=True)
    slug = models.CharField(max_length=150)
    image = models.ImageField(upload_to="blog/images",default="")

    def __str__(self):
          return  self.title +'by'+ " "+ self.author   