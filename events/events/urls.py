from django.contrib import admin
from django.urls import include, path, re_path
from django.views.static import serve
from django.conf import settings

urlpatterns = [
    path('', include('ticketApp.urls')),
    path('admin/', admin.site.urls),
    path('', include('django.contrib.auth.urls')),
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
]
