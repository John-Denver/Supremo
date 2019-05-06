from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, include


urlpatterns = [
    path('admin/', admin.site.urls),
    url('soundke/', include('STalk.urls')),

]


admin.site.site_header = "SOUND ADMIN"
admin.site.index_title = "Sound KE"


if settings.DEBUG:

    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

