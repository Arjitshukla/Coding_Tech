from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static


admin.site.site_header ="👉 ARJITECH LEARNING ❤️"
admin.site.site_title ="ARJITECH LEARNING Admin Panel"
admin.site.index_title ="Welcome to `ARJITECH LEARNING ' 🙏"
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('blog/', include('blog.urls')),
    path('contact/', include('contact.urls')),
    path('courses/', include('courses.urls')),
    path('about/', include('about.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
