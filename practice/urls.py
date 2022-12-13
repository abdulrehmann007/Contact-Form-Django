from django.contrib import admin
from django.urls import path, include

admin.site.site_header  =  "AJU Backend Services"  
admin.site.site_title  =  "AJU Admin Site"
admin.site.index_title  =  "AJU Backend Services Admin"

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include('home.urls'))
]
