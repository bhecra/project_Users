"""platzigram URL Configuration"""

from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static #Para media, imagenes
from django.urls import path, include
from tienda import views as local_views
from posts import views as post_views
from webservices import views as webservices_views
from webservices import urls



urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello-world/',local_views.hello_world_view),
    path('sorted/',local_views.sort_view),
    path('hi/<str:name>/<int:age>/', local_views.say_hi_view),

    path('post/', post_views.list_post),
    path('', include('webservices.urls')),
       
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)