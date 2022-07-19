
from django.contrib import admin
from django.urls import path,include
from projects import  urls as projectst_url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(projectst_url))
]
