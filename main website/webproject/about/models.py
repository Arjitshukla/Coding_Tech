from django.db import models

# Create your models here.
class About(models.Model):
    sno =models.AutoField(primary_key=True)
    title =models.CharField(max_length=100)
    Content1 =models.TextField()
    img1 = models.ImageField(upload_to="about/img1",default="")
    Content2 =models.TextField()
    head0 =models.TextField()
    para0=models.TextField()
    img2 = models.ImageField(upload_to="about/img2",default="")

    def __str__(self):
          return  self.title 