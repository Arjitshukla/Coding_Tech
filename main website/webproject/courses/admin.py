from django.contrib import admin
from courses.models import Course,Webtemplate

# Register your models here.

admin.site.register((Course,Webtemplate))