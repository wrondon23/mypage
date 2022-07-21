
from django.contrib import admin
from django.urls import path,include
from projects import  urls as projectst_url
from users import urls as users_url
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('projects/', include(projectst_url)),
    path('', include(users_url))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)